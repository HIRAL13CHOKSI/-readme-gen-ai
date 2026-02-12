```markdown
# Seam Carver
A Python tool for image resizing using seam carving techniques.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

## Overview
Seam Carver is a Python script that allows users to resize images intelligently by removing seams based on energy functions. It utilizes libraries such as PIL and Numba for efficient image processing. Notable features include:

- Adjustable axis for seam removal (horizontal or vertical)
- Customizable pixel reduction
- Options to save intermediate images and highlight removed seams

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `argparse`
- `os`
- `sys`
- `__future__`

### Third-Party Packages
- `PIL`
- `energy_functions`
- `numba`
- `numpy`
- `tqdm`
- `utils`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To run the script, use the following command:

```bash
python seam_carver.py input_file <value> --axis <value> --pixels <value> --output <value> --interval <value> --border <value> --show_seam <value>
```

## Flags
| Flag         | Alias | Type | Required | Default | Help                                          |
|--------------|-------|------|----------|---------|-----------------------------------------------|
| `--axis`     | `-a`  | str  | Yes      | None    | What axis to shrink the image on.            |
| `--pixels`   | `-p`  | int  | Yes      | None    | How many pixels to shrink the image by.      |
| `--output`   | `-o`  | str  | No       | None    | What to name the new cropped image.          |
| `--interval` | `-i`  | int  | No       | None    | Save every i intermediate images.             |
| `--border`   | `-b`  | bool | No       | None    | Whether or not to pad the cropped images.     |
| `--show_seam`| `-s`  | bool | No       | None    | Whether to highlight the removed seam.        |

## Environment Variables
| Name | Default | Description                          |
|------|---------|--------------------------------------|
| None specified | None | Controls runtime behavior |

## Examples
### Example 1: Basic Usage
```bash
python seam_carver.py input_file my_image.jpg --axis x --pixels 50 --output resized_image.jpg
```

### Example 2: Saving Intermediate Images
```bash
python seam_carver.py input_file my_image.jpg --axis y --pixels 30 --output resized_image.jpg --interval 5 --show_seam True
```

## Input/Output
| Input Type          | Output Type         |
|---------------------|---------------------|
| Image file (JPEG, PNG) | Resized image file (JPEG, PNG) |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: The script fails to find the input image.
  - **Solution**: Ensure the specified input file path is correct.
  
- **Issue**: The output image is not generated.
  - **Solution**: Check if the output filename includes a valid extension (e.g., .jpg or .png).

## Contributing
Coming soon.

## License
Coming soon.
```
