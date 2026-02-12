```markdown
# Seam Carver
A Python tool for image resizing using seam carving techniques.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
Seam Carver is a Python script that allows users to resize images intelligently by removing seams based on energy functions. This tool is particularly useful for preserving important content in images while reducing their size. Notable features include:

- Seam carving algorithm for image resizing.
- Options for output naming and intermediate image saving.
- Flexibility in specifying the axis of seam removal.

## Requirements
- **Python version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `argparse`
- `os`
- `sys`
- `__future__`

### Third-party Packages
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

For an editable install, you can clone the repository and run:

```bash
pip install -e .
```

## Usage
To run the seam carver, use the following command:

```bash
python seam_carver.py input_file <value> --axis <value> --pixels <value> --output <value> --interval <value> --border <value> --show_seam <value>
```

## Flags
| Flag          | Alias | Type | Required | Default | Help                                           |
|---------------|-------|------|----------|---------|------------------------------------------------|
| `--axis`      | `-a`  | str  | Yes      | None    | What axis to shrink the image on.             |
| `--pixels`    | `-p`  | int  | Yes      | None    | How many pixels to shrink the image by.       |
| `--output`    | `-o`  | str  | No       | None    | What to name the new cropped image.           |
| `--interval`  | `-i`  | int  | No       | None    | Save every i intermediate images.              |
| `--border`    | `-b`  | bool | No       | None    | Whether to pad the cropped images to original size. |
| `--show_seam` | `-s`  | bool | No       | None    | Whether to highlight the removed seam.         |

## Environment Variables
| Name | Default | Description                       |
|------|---------|-----------------------------------|
| None | None    | Controls runtime behavior         |

## Examples
### Example 1: Basic Usage
```bash
python seam_carver.py input_file image.jpg --axis x --pixels 50 --output resized_image.jpg
```

### Example 2: Saving Intermediate Images
```bash
python seam_carver.py input_file image.jpg --axis y --pixels 30 --output resized_image.jpg --interval 5 --show_seam True
```

## Input/Output
| Input Type      | Output Type     |
|-----------------|------------------|
| Image file      | Resized image file |

## Testing
To run the tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: The output image is not appearing.
  - **Solution**: Ensure the output path is correct and you have write permissions.
  
- **Issue**: Invalid axis specified.
  - **Solution**: Use either 'x' or 'y' for the axis flag.

## Contributing
Coming soon.

## License
Coming soon.
```
