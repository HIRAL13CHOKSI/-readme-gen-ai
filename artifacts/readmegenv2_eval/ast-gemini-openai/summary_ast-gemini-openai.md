# readmegenv2 evaluation

Samples evaluated: 20
Skipped due to errors: 1

## Aggregate metrics
- Dependencies precision: 1.000
- Dependencies recall: 0.875
- CLI completeness: 0.900
- Description clarity: 3.650
- Description completeness: 3.050
- Description helpfulness: 3.200

## Run configuration
- Generation: google (gemini-2.0-flash-exp)
- Judge: openai (gpt-4o-mini)
- Run label: ast-gemini-openai

## Signal insights
- Docstrings Present: clarity=3.600, completeness=3.100, helpfulness=3.100, cli=1.000 (n=10)
- Structured Cli: clarity=4.200, completeness=3.400, helpfulness=3.600, cli=1.000 (n=5)
- Sys Argv Only: clarity=4.000, completeness=4.000, helpfulness=4.000, cli=1.000 (n=1)
- Requirements Detected: clarity=3.650, completeness=3.050, helpfulness=3.200, cli=0.900 (n=20)

## Per-file metrics
| Script | Dep. P | Dep. R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Judge | Notes |
|---|---|---|---|---|---|---|---|---|---|
| clippy.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and installation instructions but lacks detailed steps for creating a standalone application and a demo. |
| currency_converter.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 4 | ai | openai | The candidate README is clear and provides useful information, but lacks some details on usage examples and error handling compared to the reference. |
| CyberScraper.py | 1.00 | 0.56 | 0.00 | 3 | 3 | 3 | ai | openai | flags: 0/1, The candidate README lacks detailed features, installation instructions, and specific usage examples compared to the reference README. |
| docker-db-auto-backup.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README provides basic information but lacks detailed instructions and examples related to backup configurations and supported databases. |
| encrypt.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a good overview and structure but lacks specific usage examples for encryption and decryption, which are crucial for clarity and completeness. |
| fileorganizer.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | The candidate README is clear and well-structured but lacks some details on supported file types and specific command usage compared to the reference. |
| fmi.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and installation instructions but lacks detailed usage examples and specific features compared to the reference. |
| Local-File-Organizer.py | 1.00 | 0.28 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README lacks detailed explanations of features, installation steps, and usage examples compared to the reference README. |
| lock_files.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed examples and some important sections present in the reference README, making it less complete and helpful. |
| Multilingual_Text_to_Speech.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | flags: 1/1, The candidate README is clear but lacks detailed explanations and examples found in the reference README, making it less complete and helpful. |
| Network_Scanner.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed usage instructions and examples, making it less complete and helpful compared to the reference. |
| password_generator.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a basic overview and usage instructions but lacks detailed configuration options and examples compared to the reference. |
| pdfmerger.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 4 | ai | openai | The candidate README is clear and provides useful information, but it lacks some details on installation and has unnecessary dependencies listed. |
| PyCat.py | — | — | — | — | — | — | error | — | Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 30) |
| QR_Generator.py | 1.00 | 1.00 | 0.00 | 3 | 3 | 3 | ai | openai | flags: 0/1, The candidate README lacks clarity on the purpose of the script and does not provide sufficient details on usage or potential risks. |
| resizeimage.py | 1.00 | 0.67 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README lacks detailed usage examples and specific function descriptions, making it less clear and complete compared to the reference. |
| seam_carver.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | flags: 12/12, The candidate README is clear and well-structured but lacks some details on the algorithm and future improvements compared to the reference. |
| Video_editor_bot.py | 1.00 | 1.00 | 1.00 | 3 | 2 | 3 | ai | openai | The candidate README lacks detailed features, deployment instructions, and a comprehensive project structure, making it less informative than the reference. |
| vpc_subnet_calculator.py | 1.00 | 1.00 | 1.00 | 5 | 4 | 4 | ai | openai | The candidate README is clear and well-structured, providing detailed usage instructions and examples, but lacks a comprehensive TODO section and information on future enhancements. |
| Watermark_bot.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README lacks detailed features, configuration settings, and specific commands, making it less informative compared to the reference. |
| wisdom_tree.py | 1.00 | 0.00 | 1.00 | 3 | 2 | 2 | ai | openai | The candidate README lacks essential details about the application's functionality, installation steps, and usage instructions compared to the reference README. |
