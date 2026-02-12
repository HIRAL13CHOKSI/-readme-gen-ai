This README provides an overview and instructions for the `CyberScraper.py` utility.

---

# CyberScraper 2077

## Overview

CyberScraper 2077 is a Streamlit-based web application designed for intelligent web scraping and data extraction, powered by a conversational AI interface. It allows users to provide URLs or ask questions, and the application will scrape the specified web content, extract information, and present it in a structured format. It supports various large language models (LLMs) and includes features for data download and integration with Google Sheets.

## Features

*   **Interactive Web Interface:** Built with Streamlit for an intuitive chat-like user experience.
*   **AI-Powered Scraping:** Leverages AI models to understand requests, scrape web pages, and extract relevant data.
*   **Multiple LLM Support:** Integrates with OpenAI (GPT), Google (Gemini), and local Ollama models.
*   **Conversational History:** Maintains a history of chats, grouped by date, allowing users to revisit previous scraping sessions.
*   **Data Presentation & Download:** Displays scraped data in interactive tables (Pandas DataFrames) and offers download options for CSV and Excel formats.
*   **Google Sheets Integration:** Authenticate with Google and upload extracted data directly to Google Sheets.
*   **Flexible Scraping Modes:** Option to use the current browser (useful for bypassing some website blocks) or a headless browser for scraping.
*   **Configurable Scraper:** Basic scraper configuration options like retries, delay, and debug mode.
*   **Persistent Chat Data:** Chat history and extracted data are saved locally.

## Installation

This script is part of a larger project structure and requires specific directories and files to be present for it to function correctly.

1.  **Python Environment:** Ensure you have Python 3.8+ installed.

2.  **Dependencies:** Install the required Python packages:
    ```bash
    pip install streamlit pandas google-auth-oauthlib playwright xlsxwriter
    ```
    After installing `playwright`, you also need to install the browser binaries:
    ```bash
    playwright install
    ```

3.  **Project Structure:** This script expects to find `app/` and `src/` directories in the same parent directory as `CyberScraper.py`, containing its submodules and assets.
    *   The `app/` directory should contain `streamlit_web_scraper_chat.py`, `ui_components.py`, `utils.py`, `styles.css`, and an `icons/` subdirectory with `radiation.png`, `man.png`, `skull.png`.
    *   The `src/` directory should contain `ollama_models.py`, and `utils/google_sheets_utils.py`, and `scrapers/playwright_scraper.py`.
    *   For Google Sheets integration, you will need a `client_secret.json` file in the root directory (alongside `CyberScraper.py`). Refer to Google's documentation on how to obtain OAuth 2.0 client credentials.

4.  **API Keys (Optional but Recommended):**
    For using OpenAI and Google Gemini models, set your respective API keys as environment variables:
    *   `OPENAI_API_KEY` for GPT models.
    *   `GOOGLE_API_KEY` for Gemini models.
    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    export GOOGLE_API_KEY="your_google_api_key"
    ```
    (On Windows, use `set OPENAI_API_KEY="your_openai_api_key"` in Command Prompt or `$env:OPENAI_API_KEY="your_openai_api_key"` in PowerShell).

5.  **Ollama (Optional):** If you plan to use Ollama models, ensure you have an Ollama server running locally and the desired models pulled.

## Usage

To run the application, navigate to the directory containing `CyberScraper.py` and its required `app/` and `src/` subdirectories, then execute the following command:

```bash
streamlit run CyberScraper.py
```

This will open the application in your web browser, typically at `http://localhost:8501`.

### Interaction Flow

1.  **Sidebar:**
    *   **Model Selection:** Choose your preferred AI model (e.g., `gpt-4o-mini`, `gemini-1.5-flash`, `ollama:llama3`).
    *   **"Use Current Browser" Checkbox:** Toggle this if you want Playwright to use your existing browser instance instead of launching a new headless one. This can be helpful for sites that detect or block automated headless browsers.
    *   **"Refresh Ollama Models" Button:** Fetches and lists available Ollama models from your local server.
    *   **New Chat:** Start a new conversation.
    *   **Conversation History:** Browse and resume previous chats. You can also delete old chats here.

2.  **Main Chat Area:**
    *   The main area displays the current chat messages.
    *   Use the chat input box at the bottom to enter URLs or ask questions.

3.  **Google Sheets Authentication:**
    When prompted to upload data to Google Sheets, a button will appear. Clicking it will initiate the Google OAuth flow in your browser. You will need to grant CyberScraper permission to access your Google Sheets.

## Examples

*   **Scrape a website and summarize its content:**
    1.  Type a URL into the chat input, e.g., `https://www.example.com`
    2.  After it scrapes, you can then ask: `Summarize the main points of this page.`

*   **Extract specific data from a page:**
    1.  Type a URL, e.g., `https://www.fakestoreapi.com/products` (a JSON API endpoint, but can be any HTML page).
    2.  Then ask: `Extract the product names and their prices into a table.`

*   **Upload extracted data to Google Sheets:**
    1.  After a successful data extraction (where a DataFrame is displayed), a "Upload to Google Sheets" button will appear below the table.
    2.  Click it and follow the authentication prompts.

## Limitations or Notes

*   **Required Local Modules:** This script relies on `app` and `src` directories containing specific Python modules and assets, which must be present in the expected project structure.
*   **API Keys:** Using advanced LLM features (GPT, Gemini) requires valid API keys set as environment variables. Without them, only local Ollama models (if configured) or basic functionality might be available.
*   **Google OAuth:** Requires a `client_secret.json` file for Google Sheets integration and a one-time authentication process.
*   **Web Scraping Variability:** Website structures can change, and some websites actively block scraping attempts. The "Use Current Browser" option might help but is not guaranteed.
*   **Ollama Server:** If using Ollama models, an Ollama server must be running on your machine.
*   **Accuracy:** "CyberScraper 2077 can make mistakes sometimes. Report any issues to the developers." - As stated in the application itself.
*   **File Persistence:** Chat history is saved to `chat_history.json` in the script's directory.
