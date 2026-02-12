# Local File Organizer

Intelligently organize your local files with AI-powered categorization and simulation.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/your-project-name.svg)](https://pypi.org/project/your-project-name/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/your-org/your-repo/CI.svg)](https://github.com/your-org/your-repo/actions)
[![Coverage Status](https://coveralls.io/repos/github/your-org/your-repo/badge.svg?branch=main)](https://coveralls.io/github/your-org/your-repo?branch=main)

---

## Overview

The Local File Organizer is an intelligent, interactive tool designed to bring order to your local file system. It leverages advanced AI models (via Google Generative AI, Groq, OpenAI, and Nexa) and natural language processing (NLTK) to understand, categorize, and propose organization strategies for your files.

Key Features:

*   **AI-Powered Categorization**: Utilizes various large language models to intelligently classify files based on their content.
*   **Simulation Mode**: Preview proposed file movements and directory structures before any changes are applied, ensuring safety and control.
*   **Interactive Operation**: Guides users through the organization process with clear prompts for mode selection and confirmation.
*   **Extensible Data Processing**: Supports diverse file types, including text and images, through specialized processing modules.
*   **NLTK Integration**: Enhances text data processing capabilities for richer file analysis.

## Requirements

*   **Python**: Version 3.8+ (recommended)
*   **Operating System**: Cross-platform (Linux, macOS, Windows)

## Dependencies

### Standard Library Modules

*   `os`
*   `time`

### Third-Party Packages

*   `data_processing_common`
*   `file_utils`
*   `google-generativeai`
*   `groq`
*   `image_data_processing`
*   `nexa`
*   `nltk`
*   `openai`
*   `output_filter`
*   `text_data_processing`

## Installation

To get started, clone the repository and install the required dependencies:

```bash
# Clone the repository (if applicable)
# git clone https://github.com/your-org/your-repo.git
# cd your-repo/path/to/script

# Install dependencies
pip install -r ../requirements.txt

# Ensure NLTK data is downloaded (script handles this, but good to know)
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('wordnet', quiet=True)"
```

## Usage

Run the script directly from your terminal. The tool will guide you through the available modes and operations interactively.

```bash
python Local-File-Organizer.py
```

The script will prompt you to select a mode (e.g., "Simulate" or "Execute") and confirm operations.

## Flags

None. The script operates interactively without command-line flags.

## Environment Variables

None specified.

## Examples

The Local File Organizer is designed for interactive use, guiding you through its functionality.

### 1. Simulate File Organization

Run the script to preview how your files would be organized without making any actual changes. This is highly recommended for first-time users.

```bash
python Local-File-Organizer.py
```

When prompted, select the "Simulate" mode. The script will analyze your files and print a proposed directory tree, showing you exactly where files would be moved or organized. You will then be asked for confirmation to proceed (even in simulation, this confirms you've reviewed the plan).

### 2. Execute File Organization

Once you are satisfied with the simulated changes, you can run the script in "Execute" mode to apply the organization to your file system.

```bash
python Local-File-Organizer.py
```

When prompted, select the "Execute" mode. After analysis and presenting the proposed changes, the script will ask for explicit confirmation before moving any files.

## Input/Output

| Type   | Description                                                                                             |
| :----- | :------------------------------------------------------------------------------------------------------ |
| **Input**  | User interactions (mode selection, yes/no confirmations). Files and directories within the specified scope. |
| **Output** | Printed simulation of directory tree, organized files and directories.                                   |

## Testing

The project includes a comprehensive test suite to ensure functionality and reliability.
To run the tests, navigate to the project root and execute `pytest`:

```bash
pytest
```

## Troubleshooting

*   **NLTK Data Errors**: If you encounter errors related to missing NLTK data (e.g., `nltk.downloader.DownloadError`), ensure the necessary NLTK data packages (`punkt`, `wordnet`) are downloaded. The script attempts to do this automatically, but a manual download might be needed:
    ```bash
    python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')"
    ```
*   **API Key Issues**: The AI models (Google Generative AI, Groq, OpenAI, Nexa) typically require API keys set as environment variables (e.g., `OPENAI_API_KEY`, `GROQ_API_KEY`). Ensure these are correctly configured if you experience issues with AI categorization.
*   **Permission Errors**: If the script fails to move or create directories, check the file system permissions for the target directories. Run the script with appropriate user privileges if necessary.

## Contributing

We welcome contributions! Please see our `CONTRIBUTING.md` for guidelines on how to submit pull requests, report bugs, and suggest features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
