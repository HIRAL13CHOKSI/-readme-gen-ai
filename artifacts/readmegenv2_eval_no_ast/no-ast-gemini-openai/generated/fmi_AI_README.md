```markdown
# FMI Weather Data Utility

## Overview

This Python script provides a way to access weather data from the Finnish Meteorological Institute (FMI) open data service. It allows you to retrieve both observations and forecasts for specific locations. The script parses the XML responses from the FMI API and returns the data as a list of `Observation` or `Forecast` objects (defined in a separate `observation.py` file).

**Note:** This script relies on a sibling `observation.py` file which defines the `Observation` and `Forecast` classes.  Since the `observation.py` file is unavailable, example usage involving `Observation` and `Forecast` objects is omitted.

## Features

*   Retrieves weather observations for a given place or coordinates.
*   Retrieves weather forecasts for a given place or coordinates, using the "harmonie" model.
*   Parses the XML response from the FMI API.
*   Fetches a list of all Finnish observation stations with metadata.

## Installation

1.  Save the provided code as `fmi.py`.
2.  Ensure you have the required packages installed. Use pip to install them:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

The script is designed to be used as a module within a larger Python project.  You'll need to import the `FMI` class to use its methods.

```python
from fmi import FMI

# Initialize the FMI class. You can specify either 'place' or 'coordinates'.
fmi = FMI(place='Helsinki') # Or fmi = FMI(coordinates='60.17,24.95')

# Get recent observations
observations = fmi.observations()

# Get weather forecast (harmonie model)
forecasts = fmi.forecast()

# Get list of stations
stations = FMI.fetch_stations()

# Print station information
for station in stations:
    print(f"Station Name: {station['name']}, Latitude: {station['latitude']}, Longitude: {station['longitude']}")
```

### Methods

*   `__init__(apikey=None, place=None, coordinates=None)`: Initializes the `FMI` object.
    *   `apikey`: Deprecated API key (no longer required).
    *   `place`: Name of the location (e.g., 'Helsinki').
    *   `coordinates`: Latitude and longitude of the location (e.g., '60.17,24.95').  Can also be set using environment variables `FMI_PLACE` and `FMI_COORDINATES`.
*   `observations(**params)`: Retrieves weather observations.  The `params` argument takes additional query parameters to be passed to the FMI API.
*   `forecast(model='harmonie', **params)`: Retrieves weather forecasts.
    *   `model`: Currently, only 'harmonie' is supported. The `params` argument takes additional query parameters to be passed to the FMI API.
*   `fetch_stations()`: Retrieves a list of Finnish observation stations with metadata (fmisid, wmo, name, latitude, longitude, height, started, groups).  This is a static method and is called directly on the class `FMI`.

## Examples

The following examples demonstrate how to use the `FMI` class to retrieve weather data.

```python
from fmi import FMI

# Example 1: Get observations for Helsinki
fmi_helsinki = FMI(place='Helsinki')
observations_helsinki = fmi_helsinki.observations()

# The following code would print data from the retrieved observations,
# if Observation class were defined.
# for obs in observations_helsinki:
#     print(f"Time: {obs.time}, Temperature: {obs.data.get('temperature')}")


# Example 2: Get forecast for specific coordinates
fmi_coords = FMI(coordinates='60.17,24.95')
forecasts_coords = fmi_coords.forecast()

# The following code would print data from the retrieved forecasts,
# if Forecast class were defined.
# for forecast in forecasts_coords:
#     print(f"Time: {forecast.time}, Temperature: {forecast.data.get('temperature')}")

# Example 3: Get weather stations
stations = FMI.fetch_stations()

# Print basic information for each station.
for station in stations:
    print(f"Station: {station['name']}, ID: {station['fmisid']}, Coordinates: {station['latitude']}, {station['longitude']}")
```

## Limitations or Notes

*   The script depends on the `observation.py` file, which contains the definitions for the `Observation` and `Forecast` classes. Without this file, you cannot fully utilize the retrieved data.
*   The API key parameter is deprecated and no longer functional.
*   The script currently only supports the 'harmonie' model for forecasts.
*   Error handling is limited to raising HTTP errors from the requests library.  More robust error handling could be added.
*   The script performs relative imports, meaning it must be run as part of a package, or the import path must be adjusted.

