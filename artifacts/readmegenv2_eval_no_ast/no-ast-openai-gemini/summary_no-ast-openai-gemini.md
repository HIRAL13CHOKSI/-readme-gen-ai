# readmegenv2_no_ast evaluation: no-ast-openai-gemini

## Run configuration
- Generation: openai / gpt-4o-mini
- Judge: google / gemini-2.0-flash-exp
- Sample size: 18

## Aggregate metrics
| metric | avg | median | min | max |
| --- | --- | --- | --- | --- |
| Dependencies precision | 0.038 | 0.000 | 0.000 | 0.500 |
| Dependencies recall | 0.014 | 0.000 | 0.000 | 0.143 |
| CLI completeness | 0.565 | 1.000 | 0.000 | 1.000 |
| Description clarity | 3.611 | 4.000 | 3.000 | 4.000 |
| Description completeness | 2.944 | 3.000 | 2.000 | 4.000 |
| Description helpfulness | 3.500 | 4.000 | 2.000 | 4.000 |

## Key findings
- Dependency recovery is very poor (precision ~0.038, recall ~0.014), indicating that the LLM-only pipeline struggles to infer real installation dependencies without AST/static analysis.
- Description scores show meaningful spread across scripts, indicating the judge is using the rating scale more discriminatively.
- Average CLI flag coverage is ~0.565; scripts with clear --help output do better, but some tools still miss flags mentioned in the reference README.

## Signal insights
| bucket | sample size | clarity | completeness | helpfulness | CLI completeness | dep precision | dep recall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| has_cli_flags | 17 | 3.588 | 2.882 | 3.471 | 0.598 | 0.041 | 0.015 |
| no_cli_flags | 1 | 4.000 | 4.000 | 4.000 | 0.000 | 0.000 | 0.000 |
| has_imports | 18 | 3.611 | 2.944 | 3.500 | 0.565 | 0.038 | 0.014 |
| no_imports | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| no_ast | 18 | 3.611 | 2.944 | 3.500 | 0.565 | 0.038 | 0.014 |

- All samples in this run are LLM-only (no AST facts), so the 'no_ast' bucket matches the global averages by design.
- Scripts where CLI flags were inferred from help output ('has_cli_flags') show notably higher CLI completeness than scripts without any inferred flags.
- Even when imports are guessed from the source (has_imports), dependency precision/recall remain low, highlighting the limits of LLM-only analysis for installation guidance.

## Example highlights
### Top 3 scripts by description helpfulness
- **clippy.py** — strong README: dep P/R 0.000/0.000, CLI completeness 0.000, desc 4.0/3.0/4.0. Rationale: The generated README is relatively clear and helpful, providing a good overview of the application, installation instructions, and usage examples. However, it misses some key elements present in the reference README, su…
- **encrypt.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 4.0/4.0/4.0. Rationale: The generated README is generally good. It provides a clear overview, installation instructions, and usage examples. It's more detailed than the reference README. However, it could benefit from better formatting, such a…
- **fmi.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 4.0/3.0/4.0. Rationale: The generated README is pretty good, but it's missing some key elements that the reference README contains, such as the test status badge, information about forecast icons, and more comprehensive usage examples (e.g., u…

### Bottom 3 scripts by dependency recall
- **clippy.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 4.0/3.0/4.0. Rationale: The generated README is relatively clear and helpful, providing a good overview of the application, installation instructions, and usage examples. However, it misses some key elements present in the reference README, su…
- **CyberScraper.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 3.0/2.0/3.0. Rationale: The generated README provides a basic overview, installation, and usage instructions for the CyberScraper 2077 application. However, it lacks several key elements found in the reference README, such as badges indicating…
- **docker-db-auto-backup.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 1.000, desc 3.0/2.0/3.0. Rationale: The generated README is missing several key sections compared to the reference, most notably a Docker Compose example. It also lacks clear instructions on how to integrate with Docker, focusing instead on running the Py…

## Per-file results
| Script | Dep P | Dep R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clippy.py | 0.000 | 0.000 | 0.000 | 4.000 | 3.000 | 4.000 | ai | |
| currency_converter.py | 0.091 | 0.143 | 1.000 | 3.000 | 3.000 | 3.000 | ai | |
| CyberScraper.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |
| docker-db-auto-backup.py | 0.000 | 0.000 | 1.000 | 3.000 | 2.000 | 3.000 | ai | |
| encrypt.py | 0.000 | 0.000 | 1.000 | 4.000 | 4.000 | 4.000 | ai | |
| fileorganizer.py | 0.000 | 0.000 | 1.000 | 3.000 | 3.000 | 3.000 | ai | |
| fmi.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| Local-File-Organizer.py | 0.100 | 0.013 | 1.000 | 3.000 | 2.000 | 2.000 | ai | |
| lock_files.py | — | — | — | — | — | — | error | Description scoring failed: LLM judge failed to parse response: Invalid control character at: line 1 column 278 (char 27 |
| Multilingual_Text_to_Speech.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |
| Network_Scanner.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| password_generator.py | 0.000 | 0.000 | 0.000 | 4.000 | 4.000 | 4.000 | ai | |
| pdfmerger.py | 0.500 | 0.100 | 1.000 | 4.000 | 4.000 | 4.000 | ai | |
| PyCat.py | 0.000 | 0.000 | 0.167 | 4.000 | 3.000 | 4.000 | ai | |
| QR_Generator.py | 0.000 | 0.000 | 0.000 | 4.000 | 4.000 | 4.000 | ai | |
| resizeimage.py | — | — | — | — | — | — | error | Description scoring failed: LLM judge failed to parse response: Invalid control character at: line 1 column 311 (char 31 |
| seam_carver.py | 0.000 | 0.000 | 0.000 | 4.000 | 3.000 | 4.000 | ai | |
| Video_editor_bot.py | — | — | — | — | — | — | error | Description scoring failed: LLM judge failed to parse response: Invalid control character at: line 1 column 299 (char 29 |
| vpc_subnet_calculator.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| Watermark_bot.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| wisdom_tree.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |