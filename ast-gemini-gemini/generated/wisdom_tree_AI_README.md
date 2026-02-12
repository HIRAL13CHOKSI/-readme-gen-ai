# Wisdom Tree

An interactive terminal application for exploring AI-generated insights.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://example.com/build-status)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://example.com/coverage)

## Overview

`wisdom_tree.py` is an interactive terminal-based application designed to facilitate exploration of knowledge and insights, powered by modern large language models. Leveraging `curses` for a rich, text-based user interface, the tool integrates with various AI providers (OpenAI, Groq, Google Generative AI) to offer a dynamic and engaging experience directly from your command line.

**Notable Features:**

*   **Interactive TUI:** Built with `curses` for a responsive and engaging terminal user interface.
*   **Multi-AI Provider Support:** Connects to OpenAI, Groq, and Google Generative AI for diverse model access.
*   **Dynamic Insight Generation:** Explore topics and generate content through conversational interaction.

## Requirements

*   **Python:** Version 3.8 or higher.
*   **Operating System:** Cross-platform (Linux, macOS, Windows Subsystem for Linux recommended for full `curses` compatibility on Windows).

## Dependencies

### Python Packages

**Standard Library Modules:**

*   `curses`
*   `os`
*   `pathlib`
*   `threading`
*   `time`
*   `typing`

**Third-Party Packages:**

*   `google-generativeai`
*   `groq`
*   `openai`

## Installation

The recommended way to install `wisdom_tree.py` and its dependencies is using `pip`.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-org/your-repo.git
    cd your-repo
    ```

2.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r ../requirements.txt
    ```
    *Note: The `requirements.txt` file is located in the parent directory relative to `wisdom_tree.py`.*

3.  **For development, install in editable mode:**
    ```bash
    pip install -e .
    ```

## Usage

To launch the Wisdom Tree application, simply run the script from your terminal:

```bash
python wisdom_tree.py
```

Upon execution, an interactive `curses` interface will appear, allowing you to navigate and interact with the AI models.

## Flags

None specified. This script does not currently accept command-line arguments.

## Environment Variables

| Name        | Default | Description           |
| :---------- | :------ | :-------------------- |
| `VLC_VERBOSE` | `null`  | Controls runtime behavior. |

## Examples

### 1. Launching the Wisdom Tree for Interactive Exploration

To begin an interactive session and explore various topics through AI-generated responses:

```bash
python wisdom_tree.py
```

This command will open the `curses`-based UI, where you can interact with the AI to ask questions, generate ideas, or learn about different subjects.

### 2. Exploring a Specific Topic Interactively

While `wisdom_tree.py` doesn't take direct topic arguments, you would launch it and then use the interactive interface to guide the AI towards a specific topic, such as "quantum physics" or "ancient history."

```bash
# Launch the application
python wisdom_tree.py

# ... then, within the interactive terminal interface,
# follow the prompts to specify your area of interest.
```

## Input/Output

| Type   | Description                                                                                                                                                                 |
| :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input  | **User Interactions:** Keyboard inputs for navigation and text entry within the `curses` UI. **API Responses:** Data received from configured AI service providers (OpenAI, Groq, Google Generative AI). |
| Output | **Terminal UI:** Interactive display of information, AI responses, and prompts within the `curses` environment.                                                               |

## Testing

This project includes tests to ensure reliability and correctness. We recommend using `pytest` to run them.

To run the tests:

```bash
pytest
```

## Troubleshooting

1.  **`curses` Initialization Errors:**
    *   **Issue:** On some systems (especially Windows without WSL), `curses` might not initialize correctly, leading to `_curses.error: setupterm: could not find terminal` or similar errors.
    *   **Solution:** Ensure you are running in a compatible terminal environment. For Windows, using Windows Subsystem for Linux (WSL) or a Cygwin/MinGW terminal is recommended. Ensure your `TERM` environment variable is set correctly (e.g., `TERM=xterm-256color`).

2.  **Missing AI API Keys/Credentials:**
    *   **Issue:** If the application fails to connect to the AI services (OpenAI, Groq, Google Generative AI), it's likely due to missing or incorrect API keys.
    *   **Solution:** Ensure you have set the necessary environment variables for your chosen AI provider (e.g., `OPENAI_API_KEY`, `GROQ_API_KEY`, `GOOGLE_API_KEY`). Refer to the documentation of each AI provider for exact variable names and setup instructions.

3.  **Dependency Installation Issues:**
    *   **Issue:** Errors during `pip install -r ../requirements.txt`.
    *   **Solution:** Ensure you are using a compatible Python version (3.8+). If you encounter build errors for specific packages, ensure you have the necessary system-level build tools installed (e.g., `build-essential` on Debian/Ubuntu, Xcode Command Line Tools on macOS).

## Contributing

We welcome contributions! Please see our `CONTRIBUTING.md` for guidelines on how to submit issues, features, or pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
