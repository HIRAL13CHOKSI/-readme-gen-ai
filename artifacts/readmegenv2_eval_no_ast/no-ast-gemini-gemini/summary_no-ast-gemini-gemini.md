# readmegenv2_no_ast evaluation: no-ast-gemini-gemini

## Run configuration
- Generation: google / gemini-2.5-flash
- Judge: google / gemini-2.5-flash
- Sample size: 21

## Aggregate metrics
| metric | avg | median | min | max |
| --- | --- | --- | --- | --- |
| Dependencies precision | 0.033 | 0.000 | 0.000 | 0.500 |
| Dependencies recall | 0.012 | 0.000 | 0.000 | 0.143 |
| CLI completeness | 0.579 | 1.000 | 0.000 | 1.000 |
| Description clarity | 4.381 | 5.000 | 2.000 | 5.000 |
| Description completeness | 2.905 | 2.000 | 1.000 | 5.000 |
| Description helpfulness | 3.238 | 3.000 | 1.000 | 5.000 |

## Key findings
- Dependency recovery is very poor (precision ~0.033, recall ~0.012), indicating that the LLM-only pipeline struggles to infer real installation dependencies without AST/static analysis.
- Description scores show meaningful spread across scripts, indicating the judge is using the rating scale more discriminatively.
- Average CLI flag coverage is ~0.579; scripts with clear --help output do better, but some tools still miss flags mentioned in the reference README.

## Signal insights
| bucket | sample size | clarity | completeness | helpfulness | CLI completeness | dep precision | dep recall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| has_cli_flags | 20 | 4.350 | 2.950 | 3.300 | 0.608 | 0.035 | 0.013 |
| no_cli_flags | 1 | 5.000 | 2.000 | 2.000 | 0.000 | 0.000 | 0.000 |
| has_imports | 21 | 4.381 | 2.905 | 3.238 | 0.579 | 0.033 | 0.012 |
| no_imports | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| no_ast | 21 | 4.381 | 2.905 | 3.238 | 0.579 | 0.033 | 0.012 |

- All samples in this run are LLM-only (no AST facts), so the 'no_ast' bucket matches the global averages by design.
- Scripts where CLI flags were inferred from help output ('has_cli_flags') show notably higher CLI completeness than scripts without any inferred flags.
- Even when imports are guessed from the source (has_imports), dependency precision/recall remain low, highlighting the limits of LLM-only analysis for installation guidance.

## Example highlights
### Top 3 scripts by description helpfulness
- **encrypt.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 5.0/5.0/5.0. Rationale: The generated README is exceptionally clear, complete, and helpful when compared to the reference. It provides a detailed overview, a comprehensive list of features, and crucial installation instructions (including depe…
- **fileorganizer.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 5.0/5.0/5.0. Rationale: The generated README is exceptional. It provides a clear overview, detailed features, and most importantly, comprehensive installation and usage instructions. The inclusion of the `extensiondict.py` example content is i…
- **fmi.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 5.0/4.0/5.0. Rationale: The generated README is exceptionally clear and helpful, especially considering the context of `fmi.py` being a module requiring a companion `observation.py` file. It goes to great lengths to explain this dependency, pr…

### Bottom 3 scripts by dependency recall
- **clippy.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 5.0/2.0/3.0. Rationale: The generated README is exceptionally clear and well-written for the scope it covers – describing a single Python script. Its explanations of features, usage, examples, and limitations are professional-quality (Clarity:…
- **CyberScraper.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 2.0/1.0/1.0. Rationale: The generated README is severely incomplete and misleading compared to the human reference. Major sections are entirely missing, including the existence and details of the 'Scrapeless Integration Branch,' comprehensive …
- **docker-db-auto-backup.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 1.000, desc 5.0/3.0/3.0. Rationale: The generated README clearly and explicitly states that it is a README for a test suite (`docker-db-auto-backup.py`) and not the actual database backup utility itself (`db-auto-backup.py`). It makes this distinction upf…

## Per-file results
| Script | Dep P | Dep R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clippy.py | 0.000 | 0.000 | 0.000 | 5.000 | 2.000 | 3.000 | ai | |
| currency_converter.py | 0.091 | 0.143 | 1.000 | 5.000 | 2.000 | 2.000 | ai | |
| CyberScraper.py | 0.000 | 0.000 | 0.000 | 2.000 | 1.000 | 1.000 | ai | |
| docker-db-auto-backup.py | 0.000 | 0.000 | 1.000 | 5.000 | 3.000 | 3.000 | ai | |
| encrypt.py | 0.000 | 0.000 | 1.000 | 5.000 | 5.000 | 5.000 | ai | |
| fileorganizer.py | 0.000 | 0.000 | 1.000 | 5.000 | 5.000 | 5.000 | ai | |
| fmi.py | 0.000 | 0.000 | 1.000 | 5.000 | 4.000 | 5.000 | ai | |
| Local-File-Organizer.py | 0.100 | 0.013 | 1.000 | 4.000 | 2.000 | 2.000 | ai | |
| lock_files.py | 0.000 | 0.000 | 1.000 | 4.000 | 2.000 | 3.000 | ai | |
| Multilingual_Text_to_Speech.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 2.000 | ai | |
| Network_Scanner.py | 0.000 | 0.000 | 1.000 | 4.000 | 2.000 | 2.000 | ai | |
| password_generator.py | 0.000 | 0.000 | 0.000 | 5.000 | 2.000 | 2.000 | ai | |
| pdfmerger.py | 0.500 | 0.100 | 1.000 | 5.000 | 4.000 | 4.000 | ai | |
| PyCat.py | 0.000 | 0.000 | 0.167 | 5.000 | 5.000 | 5.000 | ai | |
| QR_Generator.py | 0.000 | 0.000 | 0.000 | 5.000 | 4.000 | 5.000 | ai | |
| resizeimage.py | 0.000 | 0.000 | 0.000 | 4.000 | 2.000 | 3.000 | ai | |
| seam_carver.py | 0.000 | 0.000 | 0.000 | 5.000 | 3.000 | 4.000 | ai | |
| Video_editor_bot.py | 0.000 | 0.000 | 1.000 | 3.000 | 2.000 | 2.000 | ai | |
| vpc_subnet_calculator.py | 0.000 | 0.000 | 1.000 | 5.000 | 4.000 | 5.000 | ai | |
| Watermark_bot.py | 0.000 | 0.000 | 1.000 | 5.000 | 3.000 | 3.000 | ai | |
| wisdom_tree.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 2.000 | ai | |