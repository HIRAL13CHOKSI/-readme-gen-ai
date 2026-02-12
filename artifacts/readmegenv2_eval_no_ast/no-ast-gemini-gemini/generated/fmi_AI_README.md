This README is for `fmi.py`, a Python module designed to interact with the Finnish Meteorological Institute (FMI) open data API.

***

# FMI Weather Data Module

This module provides a Python interface to fetch current weather observations and forecasts from the Finnish Meteorological Institute (FMI) open data API. It allows users to retrieve weather data for a specified place or coordinates, including various meteorological parameters.

**Note:** This file (`fmi.py`) is designed as part of a larger Python package and requires a companion file named `observation.py` to function correctly.

## Features

*   **Fetch Current Observations:** Retrieve the latest weather observations for a given location.
*   **Get Forecast Data:** Access weather forecasts (currently supporting the Harmonie model).
*   **List FMI Stations:** Fetch metadata for all Finnish observation stations.
*   **Flexible Location Specification:** Specify locations by place name or latitude/longitude coordinates.
*   **Comprehensive Data:** Supports a wide range of weather parameters, including temperature, wind speed, precipitation, humidity, pressure, and more.

## Installation

This module is not a standalone executable script. It is designed to be imported as part of a Python package.

1.  **Dependencies:** Ensure you have the necessary external libraries installed:
    ```bash
    pip install requests beautifulsoup4
    ```
2.  **Module Placement:** This `fmi.py` file *must* be placed alongside an `observation.py` file in the same directory or within an accessible Python package structure. The `observation.py` file is expected to define the `Observation` and `Forecast` classes that this module uses for structuring returned data.

    If you are treating this as a minimal "package," place both `fmi.py` and `observation.py` (which defines `Observation` and `Forecast` classes) in the same directory.

## Usage

The `FMI` class provides the main interface for interacting with the FMI API.

### Initialization

Initialize the `FMI` object, optionally providing a place name or coordinates. If not provided, it attempts to read `FMI_PLACE` or `FMI_COORDINATES` from environment variables.

```python
from fmi import FMI

# By place name (reads FMI_PLACE env var if not specified)
fmi_api = FMI(place='Helsinki')

# By coordinates (reads FMI_COORDINATES env var if not specified)
# Format: "latitude,longitude"
fmi_api = FMI(coordinates='60.192059,24.945831') # Helsinki coordinates

# Using environment variables (FMI_PLACE or FMI_COORDINATES)
# os.environ['FMI_PLACE'] = 'Tampere'
# fmi_api = FMI()
```

### Fetching Observations

Use the `observations()` method to get recent weather observations.

```python
# Assuming fmi_api is initialized with a place or coordinates
observations = fmi_api.observations()

for obs in observations:
    print(f"Time: {obs.time}")
    # The attributes available depend on the data returned by FMI
    # and how the Observation class in observation.py processes it.
    # Common attributes might include:
    if hasattr(obs, 'temperature'):
        print(f"  Temperature: {obs.temperature}°C")
    if hasattr(obs, 'wind_speed'):
        print(f"  Wind Speed: {obs.wind_speed} m/s")
    if hasattr(obs, 'precipitation'):
        print(f"  Precipitation: {obs.precipitation} mm")
    print("-" * 20)
```

### Fetching Forecasts

Use the `forecast()` method to retrieve weather forecasts. The `model` parameter currently supports only `'harmonie'`.

```python
# Assuming fmi_api is initialized
forecasts = fmi_api.forecast(model='harmonie', timestep=60) # timestep in minutes

for fc in forecasts:
    print(f"Time: {fc.time}")
    # Forecast objects (from observation.py) similarly expose data
    if hasattr(fc, 'temperature'):
        print(f"  Temperature: {fc.temperature}°C")
    if hasattr(fc, 'wind_speed'):
        print(f"  Wind Speed: {fc.wind_speed} m/s")
    if hasattr(fc, 'weather_symbol'):
        print(f"  Weather Symbol: {fc.weather_symbol}")
    print("-" * 20)
```

### Fetching Station Metadata

The static method `fetch_stations()` retrieves a list of all Finnish observation stations.

```python
stations = FMI.fetch_stations()

for station in stations[:5]: # Print first 5 stations
    print(f"Station Name: {station['name']}")
    print(f"  FMISID: {station['fmisid']}")
    print(f"  Coordinates: ({station['latitude']}, {station['longitude']})")
    print("-" * 20)
```

## Examples

To run these examples, ensure you have an `observation.py` file in the same directory as `fmi.py` that defines `Observation` and `Forecast` classes which accept a timestamp string and a dictionary of weather parameters, and provide attribute-like access to these parameters (e.g., `obs.temperature`). A minimal `observation.py` might look like:

```python
# observation.py
class Observation:
    def __init__(self, time_str, data_dict):
        self.time = time_str
        for k, v in data_dict.items():
            setattr(self, k, v)

class Forecast(Observation):
    pass
```

Then, you can use `fmi.py` as demonstrated:

```python
# main_script.py
from fmi import FMI

# Example 1: Get latest temperature for Rovaniemi
fmi_rovaniemi = FMI(place='Rovaniemi')
observations = fmi_rovaniemi.observations(starttime='2023-10-26T00:00:00Z', endtime='2023-10-27T00:00:00Z', parameters='t2m')

if observations:
    latest_obs = observations[-1]
    print(f"Latest temperature in Rovaniemi ({latest_obs.time}): {latest_obs.temperature}°C")
else:
    print("No observations found for Rovaniemi in the specified timeframe.")

print("\n" + "=" * 30 + "\n")

# Example 2: Get a 3-hour forecast for Helsinki coordinates
fmi_helsinki_coords = FMI(coordinates='60.1695,24.9355') # Helsinki city center
forecasts = fmi_helsinki_coords.forecast(timestep=60, parameters='t2m,ws_10min,weathersymbol3')

print("Helsinki Forecast (next few hours):")
for fc in forecasts[:3]: # Show first 3 forecast points
    temp = f"Temp: {fc.temperature}°C" if hasattr(fc, 'temperature') else "Temp: N/A"
    wind = f"Wind: {fc.wind_speed} m/s" if hasattr(fc, 'wind_speed') else "Wind: N/A"
    symbol = f"Weather: {fc.weather_symbol}" if hasattr(fc, 'weather_symbol') else "Weather: N/A"
    print(f"  {fc.time}: {temp}, {wind}, {symbol}")

print("\n" + "=" * 30 + "\n")

# Example 3: Find all stations in the "road weather" group
road_weather_stations = [
    s['name'] for s in FMI.fetch_stations()
    if 'road weather' in s['groups']
]
print(f"Number of 'road weather' stations: {len(road_weather_stations)}")
print(f"First 5 'road weather' stations: {road_weather_stations[:5]}")
```

## Limitations or Notes

*   **Dependency on `observation.py`:** This module cannot be run independently due to the relative import of `Observation` and `Forecast` classes from `.observation`. You must provide an `observation.py` file with these definitions for `fmi.py` to work.
*   **API Key Deprecation:** The FMI API key is deprecated. The `apikey` parameter in the `FMI` constructor will trigger a `DeprecationWarning` but is no longer necessary for most queries.
*   **Error Handling:** The `requests.raise_for_status()` call ensures HTTP errors are raised. Further error handling (e.g., for missing data in the response) would need to be implemented by the user.
*   **Forecast Model:** Currently, the `forecast()` method only supports `model='harmonie'`.
*   **Single-File Context:** While `fmi.py` is a single file, its design implies it's a component of a larger system rather than a standalone script.
