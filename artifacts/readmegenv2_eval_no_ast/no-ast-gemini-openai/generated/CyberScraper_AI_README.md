```markdown
# CyberScraper 2077

## Overview

CyberScraper 2077 is a Streamlit application designed for web scraping and data extraction using natural language interaction. It allows users to specify a URL and ask questions about the data on the page, providing responses in text, CSV, or Excel formats. The application supports multiple language models, including OpenAI's GPT series, Google's Gemini series, and local Ollama models. It also allows users to download extracted data and upload it to Google Sheets.

## Features

-   **Web Scraping**: Extracts data from specified URLs using Playwright.
-   **Natural Language Interaction**: Allows users to ask questions about the scraped data.
-   **Multiple Model Support**: Supports various language models including `gpt-4o-mini`, `gpt-3.5-turbo`, `gemini-1.5-flash`, `gemini-pro`, and local Ollama models.
-   **Data Export**: Downloads data in CSV and Excel formats.
-   **Google Sheets Integration**: Uploads data directly to Google Sheets.
-   **Chat History**: Maintains a history of conversations for each URL.
-   **Browser Options**: Uses a headless browser by default or allows the user to specify to use their current browser.

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  Install the required Python packages. Since the script relies on modules within the `app` and `src` directories, and given the `ModuleNotFoundError`, it's likely that a standard `pip install -r requirements.txt` was intended but omitted from the user's instructions. Therefore, creating a virtual environment and attempting to install dependencies based on the imports is recommended.  If a `requirements.txt` file exists in the repository, use that instead.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    pip install streamlit pandas google-auth-oauthlib playwright xlsxwriter
    playwright install
    ```
3.  (Optional) Set up API keys:
    -   For OpenAI models, set the `OPENAI_API_KEY` environment variable.
    -   For Google Gemini models, set the `GOOGLE_API_KEY` environment variable.
4.  (Optional) For Google Sheets integration, create a `client_secret.json` file for OAuth 2.0 authentication.

## Usage

1.  Run the script:
    ```bash
    streamlit run CyberScraper.py
    ```
2.  Open the application in your browser using the URL provided by Streamlit (usually `http://localhost:8501`).
3.  Enter the URL you want to scrape in the chat input.
4.  Ask questions about the data.
5.  Download the data in CSV or Excel format, or upload it to Google Sheets using the buttons below the displayed data.

### Example Commands

-   To scrape a website:
    ```
    https://www.example.com
    ```
-   To ask a question about the data:
    ```
    What are the prices of the listed items?
    ```

## Examples

1.  **Scrape and analyze product prices from an e-commerce website:**

    -   Enter the URL of the product listing page.
    -   Ask "What is the average price of the products?"

2.  **Extract information from a news article:**

    -   Enter the URL of the news article.
    -   Ask "Who are the main people mentioned in the article?"

## Limitations or Notes

-   The script requires an internet connection to scrape websites and use the language models.
-   Google Sheets integration requires a `client_secret.json` file for OAuth 2.0 authentication.
-   Some websites may block web scraping attempts. Using the "Use Current Browser" option might help in some cases.
-   The performance of the script depends on the complexity of the website and the selected language model.
-   Error handling is included, but unexpected errors may still occur. Report any issues to the developers.
-   The application saves chat history to `chat_history.json` in the same directory as the script.
```
