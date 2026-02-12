# `clippy.py`

An AI-powered desktop clipboard assistant for intelligent text processing.

## Badges

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-pyperclip%2C%20LLMs-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

## Overview

`clippy.py` is a Python script designed to extend your system's clipboard capabilities with AI-driven text processing. Built with `tkinter` for a native desktop experience and `pyperclip` for seamless clipboard interaction, it integrates with leading Large Language Models (LLMs) such as Google Generative AI, Groq, and OpenAI. The tool enables users to easily capture, process, and manipulate text using powerful AI models directly from their clipboard, offering functionalities that can range from summarization to rephrasing or content generation, depending on the integrated AI logic.

**Notable Features:**

*   **Cross-platform Clipboard Integration:** Utilizes `pyperclip` for robust clipboard access across different operating systems.
*   **Intuitive GUI:** Provides a user-friendly interface powered by `tkinter` for easy interaction.
*   **Pluggable AI Backends:** Supports integration with `google-generativeai`, `groq`, and `openai`, allowing flexibility in choosing your preferred LLM provider.

## Requirements

*   **Python:** 3.8+
*   **Operating System:** Cross-platform (Windows, macOS, Linux)

## Dependencies

### Standard Library Modules

*   `tkinter` (Typically included with Python installations, especially desktop environments)

### Third-Party Packages

The following packages are required and will be installed via your `requirements.txt` file:

*   `google-generativeai`
*   `groq`
*   `openai`
*   `pyperclip`

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-org/your-repo.git
    cd your-repo
    ```

2.  **Install dependencies:**
    The project relies on a `requirements.txt` file for its dependencies.
    ```bash
    pip install -r ..\requirements.txt
    ```

## Usage

To run `clippy.py`, simply execute the script after installing its dependencies:

```bash
python clippy.py
```

This will launch the `tkinter` graphical user interface, allowing you to interact with the clipboard assistant.

## Flags

None specified.

## Environment Variables

None specified.

## Examples

### 1. Launching the Clipboard Assistant

Start the `clippy.py` application to activate its AI-powered clipboard monitoring and processing capabilities.

```bash
python clippy.py
```

Upon execution, a Tkinter window will appear, providing controls for clipboard interaction and AI model selection (based on the script's internal logic).

### 2. Processing Clipboard Content

Once the application is running, copy any text to your system clipboard. The `clippy.py` application will then (depending on its implementation) detect the new clipboard content and process it using the configured AI model. For instance, if configured for summarization:

1.  Copy a long paragraph of text from a document or webpage.
2.  Observe `clippy.py`'s GUI for a processed output (e.g., a summarized version).

(Specific interaction details will depend on the `Clippy` class implementation.)

## Input/Output

| Type   | Description                                          |
| :----- | :--------------------------------------------------- |
| **Input**  | Text content from the system clipboard.              |
| **Output** | Processed text (e.g., summarized, rewritten) displayed in the GUI, potentially copied back to the clipboard. |

## Testing

The project includes tests to ensure reliability. To run the tests, it is recommended to use `pytest`.

```bash
pytest
```

## Troubleshooting

1.  **`tkinter` issues:** If you encounter errors related to `tkinter`, ensure your Python installation includes `tkinter`. On some Linux distributions, `tkinter` might need to be installed separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).
2.  **Missing `pyperclip` or LLM dependencies:** If the script fails to start or interact with the clipboard/AI, verify that all dependencies listed in `requirements.txt` are correctly installed. Re-run `pip install -r ..\requirements.txt` to ensure everything is in place.
3.  **AI API Key Configuration:** While not explicitly mentioned in the facts, AI models like Google Generative AI, Groq, and OpenAI typically require API keys. Ensure these keys are correctly set up, usually via environment variables or configuration files, for the AI features to function.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
