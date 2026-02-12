# FMI Weather Data Fetcher

## Overview
The FMI Weather Data Fetcher is a Python utility that allows users to retrieve weather observations and forecasts from the Finnish Meteorological Institute (FMI) API. The script supports fetching data based on geographical coordinates or predefined locations and provides an easy-to-use interface for accessing various weather parameters.

## Features
- Fetch real-time weather observations.
- Retrieve weather forecasts using the Harmonie model.
- Access metadata for Finnish observation stations.
- Supports both location-based and coordinate-based queries.
- Parses and structures the response data for easy access.

## Installation
To use this script, ensure you have Python installed on your system. You will also need to install the required libraries. You can do this using pip:

```bash
pip install requests beautifulsoup4
```

## Usage
To use the FMI Weather Data Fetcher, you can create an instance of the `FMI` class and call its methods to fetch weather data.

### Example Commands
```python
from fmi import FMI

# Create an instance of the FMI class
fmi = FMI(place='Helsinki')

# Fetch current weather observations
observations = fmi.observations()
for obs in observations:
    print(f"Time: {obs.time}, Temperature: {obs.temperature}°C")

# Fetch weather forecast
forecast = fmi.forecast()
for f in forecast:
    print(f"Time: {f.time}, Forecasted Temperature: {f.temperature}°C")

# Fetch available observation stations
stations = FMI.fetch_stations()
for station in stations:
    print(f"Station Name: {station['name']}, Latitude: {station['latitude']}, Longitude: {station['longitude']}")
```

## Examples
1. **Fetching Observations**: Use the `observations()` method to get current weather data for a specified place or coordinates.
2. **Fetching Forecasts**: Use the `forecast()` method to retrieve future weather predictions based on the Harmonie model.
3. **Station Metadata**: Use `fetch_stations()` to get a list of all Finnish observation stations along with their metadata.

## Limitations or Notes
- The script currently only supports the Harmonie model for forecasts. Future extensions may include additional models.
- The use of an API key is deprecated; however, the script still allows for its inclusion in the constructor.
- Ensure that the environment variables `FMI_PLACE` and `FMI_COORDINATES` are set if you want to use them without explicitly passing them during instantiation.

This README provides a concise guide to using the FMI Weather Data Fetcher. For further information, refer to the FMI API documentation.
