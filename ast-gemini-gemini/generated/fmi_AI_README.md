# `fmi.py`

A Python utility for fetching and processing data from the Finnish Meteorological Institute (FMI).

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fmi?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square)

## Overview

This tool provides a convenient interface for retrieving meteorological and environmental data from the Finnish Meteorological Institute (FMI) using HTTP requests and HTML parsing (via Beautiful Soup). It further integrates with various large language models (LLMs) through `google-generativeai`, `groq`, and `openai` to enable advanced processing, analysis, or summarization of the retrieved data. This allows for dynamic interpretation and generation of insights from raw FMI observations.

## Requirements

*   **Python**: Version 3.8+ (recommended)
*   **Operating System**: Platform-independent (Linux, macOS, Windows)

## Dependencies

### Standard Library Modules

*   `os`
*   `warnings`

### Third-Party Packages

*   `bs4`
*   `google-generativeai`
*   `groq`
*   `observation`
*   `openai`
*   `requests`

### External Tools

None specified.

## Installation

To get started, clone this repository and install the required dependencies.

```bash
# Clone the repository (if not already done)
# git clone <repository_url>
# cd <repository_directory>

# Install dependencies from the requirements file
pip install -r ..\requirements.txt

# For development, you can install in editable mode:
pip install -e .
```

## Usage

Run the script directly from your terminal. Location parameters can be specified via environment variables.

```bash
python fmi.py
```

## Flags

None.

## Environment Variables

| Name            | Default | Description                                 |
| :-------------- | :------ | :------------------------------------------ |
| `FMI_COORDINATES` | None    | Specifies the geographical coordinates (e.g., "60.192059,24.945831") for FMI data retrieval. |
| `FMI_PLACE`       | None    | Specifies a place name (e.g., "Helsinki") for FMI data retrieval. |

## Examples

Below are a few examples demonstrating how to use `fmi.py` to retrieve data using different location specifications.

### Example 1: Fetching data for a specific place

You can specify a location by setting the `FMI_PLACE` environment variable before running the script.

```bash
export FMI_PLACE="Tampere"
python fmi.py
```

### Example 2: Fetching data for specific coordinates

Alternatively, provide exact geographical coordinates using the `FMI_COORDINATES` environment variable.

```bash
export FMI_COORDINATES="60.192059,24.945831" # Example: Helsinki city center
python fmi.py
```

## Input/Output

| Type   | Description                                                                  |
| :----- | :--------------------------------------------------------------------------- |
| Input  | Environment variables (`FMI_PLACE`, `FMI_COORDINATES`) for location specification. |
| Output | Meteorological or environmental observation data, potentially processed or summarized by LLMs. Output format will depend on the script's internal logic (e.g., print to console, JSON, etc.). |

## Testing

The project includes tests to ensure reliability. You can run them using `pytest`.

```bash
pip install pytest
pytest
```

## Troubleshooting

1.  **Missing Dependencies**: If you encounter `ModuleNotFoundError` errors, ensure all dependencies are correctly installed. Re-run `pip install -r ..\requirements.txt`.
2.  **Network Issues**: Data retrieval relies on network access to FMI services. Check your internet connection if the script fails to fetch data. Firewall or proxy settings might also interfere.
3.  **Invalid Location**: Ensure that `FMI_PLACE` or `FMI_COORDINATES` are correctly formatted and represent valid locations recognized by FMI services. Incorrect or ambiguous inputs might lead to no data being returned.

## Contributing

Coming soon.

## License

Coming soon.
