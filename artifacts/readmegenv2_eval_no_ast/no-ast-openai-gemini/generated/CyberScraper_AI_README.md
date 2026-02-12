# CyberScraper 2077

## Overview
CyberScraper 2077 is a web scraping utility built using Streamlit, designed to facilitate the extraction of data from websites through a conversational interface. Users can input URLs or questions, and the application will scrape the relevant data, presenting it in an interactive format.

## Features
- **Web Scraping**: Extract data from specified URLs.
- **Data Presentation**: Display scraped data in tables and allow downloads in CSV or Excel formats.
- **Chat Interface**: Engage with the scraper through a chat-like interface.
- **OAuth Integration**: Authenticate with Google for enhanced functionality.
- **Conversation History**: Maintain a history of interactions for easy reference.

## Installation
To run CyberScraper 2077, ensure you have Python installed on your machine. Clone the repository and install the required packages using pip. The following commands can be used:

```bash
git clone <repository-url>
cd CyberScraper
pip install -r requirements.txt
```

*Note: Replace `<repository-url>` with the actual URL of the repository.*

## Usage
To start the application, run the following command in your terminal:

```bash
streamlit run CyberScraper.py
```

Once the application is running, you can interact with it through your web browser.

### Example Commands
- **Scrape a Website**: Enter a URL in the chat input to scrape data from that website.
- **Ask a Question**: Type a question related to the data you are interested in.

## Examples
1. **Scraping a URL**: 
   - Input: `https://example.com`
   - Output: The application will scrape the content of the page and display it in a structured format.

2. **Asking a Question**:
   - Input: `What data can you find on this page?`
   - Output: The application will respond with relevant information extracted from the specified URL.

## Limitations or Notes
- Ensure that the required API keys for OpenAI and Google are set in your environment variables for full functionality.
- The application may not work with all websites due to restrictions or anti-scraping measures.
- The performance may vary based on the complexity of the website being scraped.

## Conclusion
CyberScraper 2077 is a powerful tool for extracting and interacting with web data. With its user-friendly interface and robust features, it simplifies the process of web scraping for users of all skill levels.
