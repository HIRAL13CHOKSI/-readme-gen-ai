# readmegenv2 evaluation

Samples evaluated: 20
Skipped due to errors: 1

## Aggregate metrics
- Dependencies precision: 1.000
- Dependencies recall: 0.875
- CLI completeness: 0.900
- Description clarity: 3.950
- Description completeness: 3.300
- Description helpfulness: 3.250

## Run configuration
- Generation: openai (gpt-4o-mini)
- Judge: google (gemini-2.0-flash-exp)
- Run label: ast-openai-gemini

## Signal insights
- Docstrings Present: clarity=3.800, completeness=2.900, helpfulness=2.900, cli=1.000 (n=10)
- Structured Cli: clarity=4.000, completeness=3.600, helpfulness=3.600, cli=1.000 (n=5)
- Sys Argv Only: clarity=4.000, completeness=3.000, helpfulness=3.000, cli=1.000 (n=1)
- Requirements Detected: clarity=3.950, completeness=3.300, helpfulness=3.250, cli=0.900 (n=20)

## Per-file metrics
| Script | Dep. P | Dep. R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Judge | Notes |
|---|---|---|---|---|---|---|---|---|---|
| clippy.py | 1.00 | 1.00 | 1.00 | 5 | 4 | 4 | ai | google | The candidate README is well-organized and clear, but lacks a demo and license information compared to the reference. |
| currency_converter.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | google | The candidate README is well-structured and includes helpful information like flags, troubleshooting, and examples, but it lacks information on using the tool as a module and running it in Docker, present in the reference. |
| CyberScraper.py | 1.00 | 0.56 | 0.00 | 4 | 3 | 3 | ai | google | flags: 0/1, The candidate README is concise and lists dependencies, but lacks the depth, features explanation, and illustrative examples of the reference README. |
| docker-db-auto-backup.py | 1.00 | 1.00 | 1.00 | 3 | 2 | 2 | ai | google | The candidate README lacks clarity in its purpose and completeness in its installation and usage instructions, making it less helpful overall. |
| encrypt.py | 1.00 | 1.00 | 1.00 | 5 | 4 | 4 | ai | google | The candidate README is well-structured and provides comprehensive information on setup, usage, and troubleshooting, though some sections are incomplete (Contributing, License). |
| fileorganizer.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README provides a good overview and installation instructions but lacks detail on supported file types and specific usage scenarios, making it less complete and helpful overall compared to the reference. |
| fmi.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | google | The candidate README is less clear due to its generic descriptions and lacks specific examples, and is less complete due to missing information on contributing and licensing, making it less helpful than the reference. |
| Local-File-Organizer.py | 1.00 | 0.28 | 1.00 | 3 | 2 | 2 | ai | google | The candidate README provides a basic overview but lacks detail, specific instructions, and context compared to the reference README, especially regarding AI integration and file type support. |
| lock_files.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README has a good overview and usage instructions, but it is missing key sections like OpenSSL compatibility details and the code explanation from the reference README. |
| Multilingual_Text_to_Speech.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | flags: 1/1, The candidate README provides a good overview and usage instructions but lacks some of the depth and context provided in the reference README, particularly regarding the specific models and datasets used. |
| Network_Scanner.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README is more organized but lacks specific details on saving known devices and assumes a docker environment without providing a Dockerfile. |
| password_generator.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The reference README is slightly better because it includes badges, configuration details, and examples of different generation methods, while the candidate README is missing some details and has incomplete sections. |
| pdfmerger.py | 1.00 | 1.00 | 1.00 | 4 | 5 | 5 | ai | google | The candidate README provides a more thorough and well-structured documentation, including sections for installation, usage, testing, troubleshooting, and future contribution. |
| PyCat.py | — | — | — | — | — | — | error | — | Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 30) |
| QR_Generator.py | 1.00 | 1.00 | 0.00 | 4 | 4 | 3 | ai | google | flags: 0/1, The candidate README is well-organized and includes sections for installation, usage, and troubleshooting, but lacks the crucial context of the original README's purpose as a Discord token grabber. |
| resizeimage.py | 1.00 | 0.67 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README is less clear due to the inclusion of irrelevant dependencies and missing information, and it is also less helpful because it lacks detailed API usage examples. |
| seam_carver.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | google | flags: 12/12, The candidate README is well-organized and provides clear instructions, but it includes some unnecessary packages in the dependencies and lacks a project description. |
| Video_editor_bot.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README is less clear, complete, and helpful due to missing key features, project structure, and deployment instructions compared to the reference README. |
| vpc_subnet_calculator.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | google | The candidate README is more detailed and includes sections like installation, usage, troubleshooting, and input/output, but the reference README has badges for build and coverage status, which offer immediate insights into the project's health. |
| Watermark_bot.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README is clearly written but lacks specific configuration details and practical usage examples compared to the reference. |
| wisdom_tree.py | 1.00 | 0.00 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README is clear but less complete and helpful compared to the reference, lacking usage examples and specific features. |
