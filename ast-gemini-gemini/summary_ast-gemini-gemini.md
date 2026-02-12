# readmegenv2 evaluation

Samples evaluated: 20
Skipped due to errors: 1

## Aggregate metrics
- Dependencies precision: 1.000
- Dependencies recall: 0.875
- CLI completeness: 0.900
- Description clarity: 2.700
- Description completeness: 2.250
- Description helpfulness: 2.300

## Run configuration
- Generation: google (gemini-2.5-flash)
- Judge: google (gemini-2.5-flash)
- Run label: ast-gemini-gemini

## Signal insights
- Docstrings Present: clarity=2.800, completeness=2.300, helpfulness=2.300, cli=1.000 (n=10)
- Structured Cli: clarity=3.000, completeness=2.400, helpfulness=2.600, cli=1.000 (n=5)
- Sys Argv Only: clarity=5.000, completeness=5.000, helpfulness=5.000, cli=1.000 (n=1)
- Requirements Detected: clarity=2.700, completeness=2.250, helpfulness=2.300, cli=0.900 (n=20)

## Per-file metrics
| Script | Dep. P | Dep. R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Judge | Notes |
|---|---|---|---|---|---|---|---|---|---|
| clippy.py | 1.00 | 1.00 | 1.00 | 5 | 4 | 4 | ai | google | The candidate README is exceptionally clear in detailing its AI-powered features and provides highly useful troubleshooting, but has a minor issue with the installation path example and lacks platform-specific deployment instructions found in the reference. |
| currency_converter.py | 1.00 | 1.00 | 1.00 | 2 | 1 | 1 | ai | google | The candidate README omits crucial information regarding interactive usage, module integration, and Docker deployment, and introduces misleading dependencies, significantly hindering its completeness, clarity, and helpfulness. |
| CyberScraper.py | 1.00 | 0.56 | 0.00 | 4 | 2 | 3 | ai | google | flags: 0/1, The candidate README is clear in its presentation of basic information, but it is significantly incomplete compared to the reference README, missing major features, the dual-branch architecture, detailed usage guides, and comprehensive troubleshooting, thereby reducing its overall helpfulness. |
| docker-db-auto-backup.py | 1.00 | 1.00 | 1.00 | 2 | 1 | 1 | ai | google | The candidate README fundamentally misrepresents the project as a standalone Python script rather than a Docker container, missing crucial configuration details for Docker interaction, backup location, scheduling, and compression, which severely impacts its completeness and helpfulness. |
| encrypt.py | 1.00 | 1.00 | 1.00 | 1 | 2 | 1 | ai | google | The candidate README completely fails to capture the interactive nature of the script as shown in the reference, replacing clear usage instructions with vague statements about 'internal logic' and introducing irrelevant dependencies, making it unhelpful and misleading for actual use. |
| fileorganizer.py | 1.00 | 1.00 | 1.00 | 5 | 5 | 5 | ai | google | The candidate README is exceptionally clear, complete, and helpful, providing detailed sections on installation, requirements, dependencies, examples, and troubleshooting, which are largely missing or less developed in the reference. |
| fmi.py | 1.00 | 1.00 | 1.00 | 1 | 1 | 1 | ai | google | The candidate README describes a completely different software project with different functionality, dependencies, and usage patterns than the reference README, making it entirely misleading for the intended comparison. |
| Local-File-Organizer.py | 1.00 | 0.28 | 1.00 | 2 | 2 | 2 | ai | google | The candidate README fundamentally misrepresents the product's core 'local-only, privacy-assured, no API' premise by listing multiple external AI providers and API key requirements, and it lacks crucial visual explanations and detailed installation steps present in the reference. |
| lock_files.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | google | The candidate README has good structural elements like a flags table and troubleshooting, but it loses clarity with placeholder text and confusing dependency notes, and lacks the detailed technical depth and comprehensive examples found in the reference, especially regarding internal implementation and nuanced usage warnings. |
| Multilingual_Text_to_Speech.py | 1.00 | 1.00 | 1.00 | 2 | 1 | 1 | ai | google | flags: 1/1, The candidate README has a clear structure but completely lacks project-specific details, presenting generic information and potentially misleading dependencies for the described multilingual speech synthesis project, making it unhelpful for understanding or utilizing its specific features. |
| Network_Scanner.py | 1.00 | 1.00 | 1.00 | 3 | 2 | 2 | ai | google | The candidate README is well-structured but lacks crucial details for setting up the core 'known devices' feature and omits external dependencies like nmap, making it less clear and complete than the reference, and thus less helpful for a new user. |
| password_generator.py | 1.00 | 1.00 | 1.00 | 2 | 2 | 2 | ai | google | The candidate README significantly diverges from the reference by describing a basic script rather than a configurable library, listing unrelated third-party dependencies, and missing instructions for the detailed customization features present in the reference. |
| pdfmerger.py | 1.00 | 1.00 | 1.00 | 3 | 3 | 3 | ai | google | The candidate README is structurally comprehensive with excellent usage examples and troubleshooting, but its clarity, completeness, and helpfulness are significantly diminished by the inclusion of multiple unexplained and seemingly irrelevant AI/LLM-related dependencies. |
| PyCat.py | — | — | — | — | — | — | error | — | Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 30) |
| QR_Generator.py | 1.00 | 1.00 | 0.00 | 1 | 1 | 1 | ai | google | flags: 0/1, The candidate README completely misinterprets the project's purpose, describing a generic QR generator instead of the Discord QR scam and token grabber functionality central to the reference README. |
| resizeimage.py | 1.00 | 0.67 | 1.00 | 4 | 3 | 3 | ai | google | The candidate README offers good examples and a helpful troubleshooting section but lacks a comprehensive API reference for all functions, omits the validation features, and has slightly confusing dependency and installation instructions. |
| seam_carver.py | 1.00 | 1.00 | 1.00 | 4 | 3 | 3 | ai | google | flags: 12/12, The candidate README improves formatting and adds general best practices like badges and a testing section, but significantly detracts from completeness and helpfulness by omitting the detailed algorithm explanation, academic context, and future work present in the reference. |
| Video_editor_bot.py | 1.00 | 1.00 | 1.00 | 2 | 2 | 2 | ai | google | The candidate README is significantly less clear, complete, and helpful than the reference due to prominent placeholder text, a vague feature list, and the absence of direct demo or support links. |
| vpc_subnet_calculator.py | 1.00 | 1.00 | 1.00 | 4 | 4 | 5 | ai | google | The candidate README is significantly more detailed and user-friendly, providing comprehensive instructions, examples, and troubleshooting, though it contains some template placeholders and unexplained dependencies. |
| Watermark_bot.py | 1.00 | 1.00 | 1.00 | 3 | 2 | 2 | ai | google | The candidate README is well-structured and explains the project's technical aspects, but critically fails to list any environment variables or configuration details necessary to make the Telegram bot functional, a major omission compared to the reference. |
| wisdom_tree.py | 1.00 | 0.00 | 1.00 | 1 | 1 | 1 | ai | google | The candidate README describes a completely different project focused on 'AI-generated insights' instead of the 'tui concentration app' outlined in the reference, making it entirely unhelpful and misleading for its intended comparison. |
