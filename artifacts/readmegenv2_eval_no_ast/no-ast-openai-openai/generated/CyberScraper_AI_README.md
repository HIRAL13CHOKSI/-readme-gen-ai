# CyberScraper 2077

## Overview
CyberScraper 2077 is a web scraping utility built with Streamlit that allows users to scrape data from websites and interact with it through a chat interface. The application supports multiple AI models for processing user queries and can handle various data formats, including CSV and Excel.

## Features
- **Web Scraping**: Easily scrape data from any URL provided by the user.
- **Chat Interface**: Interact with the scraper through a conversational interface.
- **Data Handling**: Display scraped data in tables and allow users to download it in CSV or Excel formats.
- **Model Selection**: Choose from multiple AI models for processing queries.
- **OAuth Authentication**: Authenticate with Google for additional features.
- **Chat History**: Maintain a history of conversations for easy reference.

## Installation
To run CyberScraper 2077, ensure you have Python installed on your machine. You will also need to install the required dependencies. 

1. Clone the repository or download the script.
2. Install the necessary packages:
   ```bash
   pip install streamlit pandas google-auth google-auth-oauthlib
   ```
3. Ensure you have the required API keys set in your environment for OpenAI and Google services.

## Usage
To run the application, execute the following command in your terminal:

```bash
streamlit run CyberScraper.py
```

Once the application is running, you can access it via your web browser at the provided local URL.

### Example Commands
- To scrape a website, simply enter the URL in the chat input.
- Ask questions about the data retrieved, e.g., "What is the average price of items listed?"

## Examples
1. **Scraping a Website**:
   - User: `https://example.com`
   - Assistant: "Scraping example.com... This may take a moment."

2. **Querying Data**:
   - User: `What are the top 5 products?`
   - Assistant: Displays the top 5 products from the scraped data.

3. **Downloading Data**:
   - After scraping, the user can download the data in CSV or Excel format using the provided buttons.

## Limitations or Notes
- Ensure that the URLs provided are accessible and do not block scraping attempts.
- The application may require specific API keys for certain models; ensure these are set in your environment.
- The performance may vary based on the website's structure and response time.

For any issues or feature requests, please contact the developers.
