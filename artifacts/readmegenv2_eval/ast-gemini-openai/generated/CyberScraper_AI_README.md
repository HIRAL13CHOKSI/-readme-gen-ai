# CyberScraper

A tool for scraping and analyzing data from websites.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Overview

CyberScraper is a Python tool designed to scrape and analyze data from websites. It leverages libraries like Streamlit for creating an interactive user interface and Pandas for data manipulation. Key features include:

- Interactive web scraping through a Streamlit interface.
- Data extraction and analysis using web scraping techniques.
- Chat history management (saving and loading).
- Integration with Google Sheets for data upload.

## Requirements

- Python 3.9+
- Operating System: Platform independent

## Dependencies

### Standard Library

- asyncio
- atexit
- base64
- datetime
- io
- json
- os
- re
- time
- urllib

### Third-Party Packages

- app
- google_auth_oauthlib
- pandas
- src
- streamlit
- google-generativeai
- groq
- openai

## Installation

To install CyberScraper and its dependencies, follow these steps:

1.  Clone the repository (if applicable).
2.  Install the required packages using pip:

    ```bash
    pip install -r ..\requirements.txt
    ```

## Usage

To run CyberScraper, use the following command:

```bash
streamlit run CyberScraper.py
```

## Flags

None

## Environment Variables

| Name            | Default | Description                                 |
|-----------------|---------|---------------------------------------------|
| `GOOGLE_API_KEY` | None    | API key for Google services.                |
| `OPENAI_API_KEY` | None    | API key for accessing OpenAI's services.   |

## Examples

1.  Running CyberScraper with Streamlit:

    ```bash
    streamlit run CyberScraper.py
    ```

## Input/Output

| Input        | Output                                     |
|--------------|--------------------------------------------|
| Website URL  | Extracted data, chat history, analyzed insights |
| User prompts | Responses, data visualizations             |

## Testing

To run tests, use pytest:

```bash
pytest
```

## Troubleshooting

1.  **Missing dependencies**: Ensure all required packages are installed using `pip install -r ..\requirements.txt`.
2.  **API Key Issues**: Verify that `GOOGLE_API_KEY` and `OPENAI_API_KEY` environment variables are correctly set with valid API keys.

## Contributing

Coming soon

## License

Coming soon
