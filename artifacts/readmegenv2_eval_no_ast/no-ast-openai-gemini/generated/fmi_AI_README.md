# FMI Python Utility

## Overview
The FMI Python Utility is a standalone script designed to interact with the Finnish Meteorological Institute (FMI) API. It allows users to retrieve weather observations and forecasts based on specified locations or coordinates.

## Features
- Fetch current weather observations.
- Retrieve weather forecasts using the Harmonie model.
- Access metadata for Finnish weather observation stations.
- Supports both location-based and coordinate-based queries.

## Installation
To use this utility, ensure you have Python installed on your machine. You will also need to install the required libraries. You can do this using pip:

```bash
pip install requests beautifulsoup4
```

## Usage
To use the FMI utility, you need to create an instance of the `FMI` class and call its methods to retrieve weather data.

### Example Commands

1. **Get Weather Observations:**
   ```python
   from fmi import FMI

   fmi = FMI(place='Helsinki')
   observations = fmi.observations()
   for obs in observations:
       print(f'Time: {obs.time}, Temperature: {obs.temperature}, Wind Speed: {obs.wind_speed}')
   ```

2. **Get Weather Forecast:**
   ```python
   from fmi import FMI

   fmi = FMI(coordinates='60.1695,24.9354')  # Helsinki coordinates
   forecast = fmi.forecast()
   for f in forecast:
       print(f'Time: {f.time}, Temperature: {f.temperature}, Wind Speed: {f.wind_speed}')
   ```

3. **Fetch Observation Stations:**
   ```python
   from fmi import FMI

   stations = FMI.fetch_stations()
   for station in stations:
       print(f'Station Name: {station["name"]}, Latitude: {station["latitude"]}, Longitude: {station["longitude"]}')
   ```

## Examples
- To get observations for a specific place (e.g., "Helsinki"):
  ```python
  fmi = FMI(place='Helsinki')
  observations = fmi.observations()
  ```

- To get a forecast for a specific location using coordinates:
  ```python
  fmi = FMI(coordinates='60.1695,24.9354')
  forecast = fmi.forecast()
  ```

- To list all available observation stations:
  ```python
  stations = FMI.fetch_stations()
  ```

## Limitations or Notes
- The script currently supports only the Harmonie model for forecasts.
- The use of an API key is deprecated; you can use the utility without one.
- Ensure that the required libraries are installed before running the script.
- The script is designed for use in a Python environment where it can be imported; ensure proper paths are set if running as a standalone script.
