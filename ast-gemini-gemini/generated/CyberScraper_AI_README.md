# CyberScraper

An AI-powered interactive web scraping and data processing tool.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/user/repo?style=social)](https://github.com/user/repo)

## Overview

CyberScraper is a Streamlit-based interactive application designed to facilitate web scraping and data processing tasks through an intuitive chat interface. It leverages powerful AI models (Google Generative AI, OpenAI, Groq) to understand user requests, extract information from web pages, and process the results using Pandas for data manipulation. Key features include:

*   **Interactive Chat Interface**: Engage with an AI assistant to specify scraping targets and data processing instructions.
*   **AI-Powered Scraping**: Utilize various large language models to intelligently extract structured or unstructured data from URLs.
*   **Data Processing with Pandas**: Seamlessly integrate data handling and transformation using the Pandas library.
*   **Google Sheets Integration**: Support for displaying processed data and potentially uploading it to Google Sheets (inferred from `display_message_with_sheets_upload` and `google_auth_oauthlib`).
*   **Chat History Management**: Save and load conversation history for continuity.

## Requirements

*   **Python**: Version 3.8 or higher.
*   **Operating System**: Cross-platform (Linux, macOS, Windows).

## Dependencies

### Standard Library

The following modules from Python's standard library are utilized:

*   `asyncio`
*   `atexit`
*   `base64`
*   `datetime`
*   `io`
*   `json`
*   `os`
*   `re`
*   `time`
*   `urllib`

### Third-Party Packages

CyberScraper relies on the following external libraries:

*   `google-generativeai`
*   `google_auth_oauthlib`
*   `groq`
*   `openai`
*   `pandas`
*   `streamlit`

### External Tools

None specified.

## Installation

To get started with CyberScraper, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-repo/CyberScraper.git
cd CyberScraper
pip install -r ../requirements.txt
```

*(Note: The `requirements.txt` file is expected in the parent directory of `CyberScraper.py`.)*

## Usage

CyberScraper is a Streamlit application. To launch the interactive web interface, navigate to the directory containing `CyberScraper.py` and run:

```bash
streamlit run CyberScraper.py
```

This command will open the application in your default web browser.

## Flags

None specified.

## Environment Variables

CyberScraper uses environment variables for API key configuration:

| Name             | Default | Description                                 |
| :--------------- | :------ | :------------------------------------------ |
| `GOOGLE_API_KEY` | None    | Google API key for Generative AI services.  |
| `OPENAI_API_KEY` | None    | OpenAI API key for OpenAI model integration. |

## Examples

### 1. Launching the Application

Start the interactive Streamlit application from your terminal:

```bash
streamlit run CyberScraper.py
```

This will launch the web interface where you can interact with the AI assistant.

### 2. Performing a Web Scraping Task

Once the Streamlit app is running, you can interact with it through the chat interface:

1.  **Set API Keys**: Ensure `GOOGLE_API_KEY` and/or `OPENAI_API_KEY` are set in your environment or provided within the application's UI if an option exists.
2.  **Provide a URL**: In the chat input, paste a URL you wish to scrape.
3.  **Specify Data Needs**: Instruct the AI on what information to extract (e.g., "Scrape all product names and prices from this page," or "Summarize the main points of this article").
4.  **Process and View Data**: The AI will process your request, perform the scraping, and display the results within the application, possibly in a Pandas DataFrame or formatted output. You might then have options to further process or upload this data.

## Input/Output

| Type   | Description                                                                                     |
| :----- | :---------------------------------------------------------------------------------------------- |
| **Input**  | User prompts (text commands, URLs) via the Streamlit chat interface. API keys (via environment variables or UI). |
| **Output** | Scraped web content, AI-generated responses, structured data (e.g., tables), formatted messages, chat history. |

## Testing

This project includes tests to ensure reliability. To run the test suite, we recommend using `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **Missing API Keys**: If the application fails to initialize or respond to AI queries, ensure that `GOOGLE_API_KEY` and/or `OPENAI_API_KEY` environment variables are correctly set. Without these, AI model interactions will fail.
    ```bash
    export GOOGLE_API_KEY="your_google_api_key"
    export OPENAI_API_KEY="your_openai_api_key"
    streamlit run CyberScraper.py
    ```
2.  **Dependency Installation Issues**: If you encounter `ModuleNotFoundError` or similar issues, verify that all dependencies are correctly installed. Double-check your `pip install -r ../requirements.txt` command and ensure it completed without errors. If necessary, activate a virtual environment before installation.

## Contributing

Coming soon.

## License

Coming soon.
