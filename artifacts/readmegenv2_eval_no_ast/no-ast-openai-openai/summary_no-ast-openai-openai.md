# readmegenv2_no_ast evaluation: no-ast-openai-openai

## Run configuration
- Generation: openai / gpt-4o-mini
- Judge: openai / gpt-4o-mini
- Sample size: 21

## Aggregate metrics
| metric | avg | median | min | max |
| --- | --- | --- | --- | --- |
| Dependencies precision | 0.033 | 0.000 | 0.000 | 0.500 |
| Dependencies recall | 0.012 | 0.000 | 0.000 | 0.143 |
| CLI completeness | 0.579 | 1.000 | 0.000 | 1.000 |
| Description clarity | 3.619 | 4.000 | 3.000 | 4.000 |
| Description completeness | 2.714 | 3.000 | 2.000 | 3.000 |
| Description helpfulness | 3.143 | 3.000 | 3.000 | 4.000 |

## Key findings
- Dependency recovery is very poor (precision ~0.033, recall ~0.012), indicating that the LLM-only pipeline struggles to infer real installation dependencies without AST/static analysis.
- Description scores show meaningful spread across scripts, indicating the judge is using the rating scale more discriminatively.
- Average CLI flag coverage is ~0.579; scripts with clear --help output do better, but some tools still miss flags mentioned in the reference README.

## Signal insights
| bucket | sample size | clarity | completeness | helpfulness | CLI completeness | dep precision | dep recall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| has_cli_flags | 20 | 3.600 | 2.700 | 3.150 | 0.608 | 0.035 | 0.013 |
| no_cli_flags | 1 | 4.000 | 3.000 | 3.000 | 0.000 | 0.000 | 0.000 |
| has_imports | 21 | 3.619 | 2.714 | 3.143 | 0.579 | 0.033 | 0.012 |
| no_imports | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| no_ast | 21 | 3.619 | 2.714 | 3.143 | 0.579 | 0.033 | 0.012 |

- All samples in this run are LLM-only (no AST facts), so the 'no_ast' bucket matches the global averages by design.
- Scripts where CLI flags were inferred from help output ('has_cli_flags') show notably higher CLI completeness than scripts without any inferred flags.
- Even when imports are guessed from the source (has_imports), dependency precision/recall remain low, highlighting the limits of LLM-only analysis for installation guidance.

## Example highlights
### Top 3 scripts by description helpfulness
- **encrypt.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 4.0/3.0/4.0. Rationale: The generated README is clear and provides a good overview of the utility, including installation and usage instructions. However, it lacks some details found in the reference, such as specific examples of file names us…
- **lock_files.py** — strong README: dep P/R 0.000/0.000, CLI completeness 1.000, desc 4.0/3.0/4.0. Rationale: The generated README is clear and provides a good overview of the functionality of the script. However, it lacks some details present in the reference, such as specific command-line options and their descriptions, which…
- **pdfmerger.py** — strong README: dep P/R 0.500/0.100, CLI completeness 1.000, desc 4.0/3.0/4.0. Rationale: The generated README is clear and provides a good overview of the application, its features, and installation instructions. However, it lacks a visual element (like an image of the GUI) that could enhance user understan…

### Bottom 3 scripts by dependency recall
- **clippy.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 4.0/3.0/3.0. Rationale: The generated README is clear and provides a good overview of the application, its features, and basic usage instructions. However, it lacks a demo image, detailed installation instructions including the use of virtual …
- **CyberScraper.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 0.000, desc 3.0/2.0/3.0. Rationale: The generated README provides a basic overview and installation instructions but lacks several important details found in the reference. It misses sections on advanced features, Docker installation, and specific branch …
- **docker-db-auto-backup.py** — weak dependency coverage: dep P/R 0.000/0.000, CLI completeness 1.000, desc 3.0/2.0/3.0. Rationale: The generated README provides a basic overview and usage instructions but lacks clarity in certain areas, such as the installation requirements and the specific dependencies needed beyond just `pytest`. It also omits im…

## Per-file results
| Script | Dep P | Dep R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clippy.py | 0.000 | 0.000 | 0.000 | 4.000 | 3.000 | 3.000 | ai | |
| currency_converter.py | 0.091 | 0.143 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| CyberScraper.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |
| docker-db-auto-backup.py | 0.000 | 0.000 | 1.000 | 3.000 | 2.000 | 3.000 | ai | |
| encrypt.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| fileorganizer.py | 0.000 | 0.000 | 1.000 | 3.000 | 3.000 | 3.000 | ai | |
| fmi.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| Local-File-Organizer.py | 0.100 | 0.013 | 1.000 | 3.000 | 2.000 | 3.000 | ai | |
| lock_files.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| Multilingual_Text_to_Speech.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |
| Network_Scanner.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| password_generator.py | 0.000 | 0.000 | 0.000 | 4.000 | 3.000 | 3.000 | ai | |
| pdfmerger.py | 0.500 | 0.100 | 1.000 | 4.000 | 3.000 | 4.000 | ai | |
| PyCat.py | 0.000 | 0.000 | 0.167 | 4.000 | 3.000 | 3.000 | ai | |
| QR_Generator.py | 0.000 | 0.000 | 0.000 | 3.000 | 3.000 | 3.000 | ai | |
| resizeimage.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |
| seam_carver.py | 0.000 | 0.000 | 0.000 | 4.000 | 3.000 | 3.000 | ai | |
| Video_editor_bot.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| vpc_subnet_calculator.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| Watermark_bot.py | 0.000 | 0.000 | 1.000 | 4.000 | 3.000 | 3.000 | ai | |
| wisdom_tree.py | 0.000 | 0.000 | 0.000 | 3.000 | 2.000 | 3.000 | ai | |