"""Offline tests: no paid API calls and no execution of input scripts."""
import json
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from readmegenv2_no_ast.pipeline import generate_readme_for_file


class NoAstPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "input.py"
        self.marker = self.root / "executed"
        self.source.write_text(
            f"from pathlib import Path\nPath({str(self.marker)!r}).touch()\nimport requests\n",
            encoding="utf-8",
        )
        self.output = self.root / "nested" / "README.md"
        self.data = {
            "readme": "# Example\n\nUsage documentation.",
            "imports": {"third_party": ["requests", "requests"]},
            "cli": {"arguments": [{"flag": "--url", "alias": "-u", "aliases": []}]},
        }
        self.choose = patch("readmegenv2_no_ast.pipeline.choose_provider", return_value="openai").start()
        self.call = patch("readmegenv2_no_ast.pipeline.call_llm", return_value=json.dumps(self.data)).start()
        self.addCleanup(patch.stopall)

    def run_generation(self, **kwargs):
        return generate_readme_for_file(str(self.source), out_path=str(self.output), **kwargs)

    def test_writes_markdown_and_evaluator_metadata(self):
        output, mode, facts = self.run_generation()
        self.assertEqual(output, str(self.output))
        self.assertEqual(mode, "ai")
        self.assertTrue(self.output.read_text().endswith("\n"))
        self.assertEqual(facts["imports"]["third_party"], ["requests"])
        self.assertEqual(facts["cli"]["arguments"][0]["alias"], "-u")
        self.assertTrue(facts["no_ast"])

    def test_routes_source_model_and_provider_without_execution(self):
        self.choose.return_value = "google"
        keys = {"google": "fake-test-key"}
        _, _, facts = self.run_generation(
            provider="google", model="test-model", api_keys=keys, probe_help=True
        )
        args, kwargs = self.call.call_args
        self.assertEqual(args[:2], ("google", "test-model"))
        self.assertEqual(json.loads(args[2][1]["content"])["source"], self.source.read_text())
        self.assertEqual(kwargs["api_keys"], keys)
        self.assertTrue(facts["help_probe_requested"])
        self.assertFalse(facts["help_probe_executed"])
        self.assertFalse(self.marker.exists())

    def test_accepts_json_fence_and_empty_metadata(self):
        self.data["imports"]["third_party"] = []
        self.data["cli"]["arguments"] = []
        self.call.return_value = "```json\n" + json.dumps(self.data) + "\n```"
        _, _, facts = self.run_generation()
        self.assertEqual(facts["cli"]["arguments"], [])

    def test_invalid_responses_do_not_overwrite_existing_output(self):
        self.output.parent.mkdir()
        self.output.write_text("keep existing")
        bad = [
            "not json", "[]", json.dumps({"readme": ""}),
            json.dumps({**self.data, "imports": {"third_party": "requests"}}),
            json.dumps({**self.data, "cli": {"arguments": [{"flag": "invented"}]}}),
            json.dumps({**self.data, "cli": {"arguments": [{"flag": "--ok", "aliases": "bad"}]}}),
        ]
        for response in bad:
            with self.subTest(response=response):
                self.call.return_value = response
                with self.assertRaises(ValueError):
                    self.run_generation()
                self.assertEqual(self.output.read_text(), "keep existing")

    def test_api_error_propagates_without_writing(self):
        self.call.side_effect = RuntimeError("provider unavailable")
        with self.assertRaisesRegex(RuntimeError, "provider unavailable"):
            self.run_generation()
        self.assertFalse(self.output.exists())

    def test_provider_error_propagates_without_api_call(self):
        self.choose.side_effect = RuntimeError("no key")
        with self.assertRaisesRegex(RuntimeError, "no key"):
            self.run_generation()
        self.call.assert_not_called()

    def test_non_openai_requires_explicit_model(self):
        self.choose.return_value = "google"
        with self.assertRaisesRegex(ValueError, "explicit model"):
            self.run_generation()
        self.call.assert_not_called()

    def test_input_cannot_be_overwritten(self):
        original = self.source.read_text()
        with self.assertRaisesRegex(ValueError, "overwrite"):
            generate_readme_for_file(str(self.source), out_path=str(self.source))
        self.assertEqual(self.source.read_text(), original)
        self.call.assert_not_called()

    def test_default_output_path(self):
        output, _, _ = generate_readme_for_file(str(self.source))
        self.assertEqual(Path(output), self.root / "README.generated.md")

    def test_missing_input_fails_before_api_call(self):
        with self.assertRaises(FileNotFoundError):
            generate_readme_for_file(str(self.root / "missing.py"))
        self.call.assert_not_called()

    def test_existing_evaluator_consumes_baseline_output(self):
        runner = Path(__file__).with_name("run_readmegenv2_no_ast_eval.py")
        spec = importlib.util.spec_from_file_location("no_ast_evaluator", runner)
        evaluator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(evaluator)
        reference = self.root / "reference.md"
        reference.write_text("# Example\n\n## Dependencies\npip install requests\n\n## CLI options\n--url -u\n")
        scores = {"clarity": 4, "completeness": 4, "helpfulness": 4}
        with patch.object(evaluator, "_llm_description_scores", return_value=scores):
            result = evaluator.evaluate_script(
                self.source, reference, provider="openai", generation_model="test-model",
                judge_provider="openai", judge_model="test-judge", api_keys=None,
                generated_dir=self.root / "generated",
            )
        self.assertNotIn("error", result)
        self.assertEqual(result["dependencies"]["predicted"], ["requests"])
        self.assertEqual(result["cli"]["hits"], 2)
        self.assertTrue(result["signal_profile"]["no_ast"])
        self.assertFalse(self.marker.exists())


if __name__ == "__main__":
    unittest.main()

