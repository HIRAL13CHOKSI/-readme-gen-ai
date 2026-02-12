# readmegenv2 evaluation

Samples evaluated: 20
Skipped due to errors: 1

## Aggregate metrics
- Dependencies precision: 1.000
- Dependencies recall: 0.875
- CLI completeness: 0.900
- Description clarity: 3.850
- Description completeness: 3.200
- Description helpfulness: 3.250

## Run configuration
- Generation: openai (gpt-4o-mini)
- Judge: openai (gpt-4o-mini)
- Run label: ast-openai-openai

## Signal insights
- Docstrings Present: clarity=3.900, completeness=3.000, helpfulness=3.100, cli=1.000 (n=10)
- Structured Cli: clarity=4.000, completeness=3.400, helpfulness=3.600, cli=1.000 (n=5)
- Sys Argv Only: clarity=4.000, completeness=3.000, helpfulness=3.000, cli=1.000 (n=1)
- Requirements Detected: clarity=3.850, completeness=3.200, helpfulness=3.250, cli=0.900 (n=20)

## Per-file metrics
| Script | Dep. P | Dep. R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Judge | Notes |
|---|---|---|---|---|---|---|---|---|---|
| clippy.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks a demo and detailed step-by-step instructions, which reduces its completeness and helpfulness compared to the reference. |
| currency_converter.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | The candidate README is clear and well-structured but lacks some detailed usage examples and specific error handling information compared to the reference. |
| CyberScraper.py | 1.00 | 0.56 | 0.00 | 3 | 3 | 3 | ai | openai | flags: 0/1, The candidate README lacks detailed features, installation instructions, and usage examples compared to the reference README, making it less informative. |
| docker-db-auto-backup.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and installation instructions but lacks detailed information on supported databases and advanced configuration options. |
| encrypt.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | The candidate README is clear and provides a good overview, but lacks specific usage examples for encryption and decryption that are present in the reference README. |
| fileorganizer.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed information on supported file types and has incomplete sections on contributing and licensing. |
| fmi.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed usage examples and specific functionality descriptions compared to the reference. |
| Local-File-Organizer.py | 1.00 | 0.28 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README lacks detailed explanations of features and usage, making it less clear and complete compared to the reference. |
| lock_files.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and examples, but lacks detailed explanations of certain features and does not cover all aspects found in the reference README. |
| Multilingual_Text_to_Speech.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | flags: 1/1, The candidate README provides a clear overview and usage instructions but lacks detailed explanations about the model's architecture and training process compared to the reference. |
| Network_Scanner.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed usage instructions and examples compared to the reference README. |
| password_generator.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README is clear but lacks detailed usage examples and configuration options compared to the reference README. |
| pdfmerger.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | The candidate README is clear and provides a good overview, but it includes unnecessary dependencies and lacks details on the GUI aspect. |
| PyCat.py | — | — | — | — | — | — | error | — | Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 30) |
| QR_Generator.py | 1.00 | 1.00 | 0.00 | 4 | 3 | 3 | ai | openai | flags: 0/1, The candidate README is clear but lacks specific details about the QR code's purpose and usage context, making it less complete and helpful compared to the reference. |
| resizeimage.py | 1.00 | 0.67 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a general overview and installation instructions but lacks detailed usage examples and specific function descriptions compared to the reference. |
| seam_carver.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 4 | ai | openai | flags: 12/12, The candidate README is clear and provides a good overview, but lacks some details on the algorithm and future improvements that the reference README includes. |
| Video_editor_bot.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and installation instructions but lacks detailed feature descriptions and deployment options compared to the reference. |
| vpc_subnet_calculator.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 4 | ai | openai | The candidate README is clear and well-structured, but it lacks some details on future enhancements and has incomplete sections on contributing and licensing. |
| Watermark_bot.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | openai | The candidate README lacks detailed features, configuration instructions, and specific commands, making it less informative compared to the reference. |
| wisdom_tree.py | 1.00 | 0.00 | 1.00 | 4 | 3 | 3 | ai | openai | The candidate README provides a clear overview and installation instructions, but lacks detailed usage information and feature descriptions compared to the reference. |
