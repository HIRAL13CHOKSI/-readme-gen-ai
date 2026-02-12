# Seam Carver

Shrink images using the seam carving algorithm.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tests](https://github.com/USERNAME/REPOSITORY/actions/workflows/test.yml/badge.svg)](https://github.com/USERNAME/REPOSITORY/actions/workflows/test.yml)

## Overview

This script implements the seam carving algorithm to intelligently resize images by removing low-energy seams.  It allows you to specify the axis to shrink along (x or y) and the number of pixels to remove. Intermediate images can be saved to observe the carving process.

Notable features:

*   Resizes images by removing low-energy seams instead of simply cropping.
*   Supports shrinking along either the x or y axis.
*   Can save intermediate images to visualize the seam carving process.
*   Highlights the removed seam on intermediate images (optional).

## Requirements

*   Python 3.7+
*   Any operating system that supports Python and the required dependencies.

## Dependencies

### Standard Library

*   `__future__`
*   `argparse`
*   `os`
*   `sys`

### Third-Party Packages

*   `PIL`
*   `energy_functions`
*   `numba`
*   `numpy`
*   `tqdm`
*   `utils`
*   `google-generativeai`
*   `groq`
*   `openai`

## Installation

Install the required dependencies using `pip`:

```bash
pip install -r ..\requirements.txt
```

Alternatively, for an editable install:

```bash
pip install -e .
```

## Usage

```
python seam_carver.py input_file <value> --axis <value> --pixels <value> --output <value> --interval <value> --border <value> --show_seam <value>
```

## Flags

| Flag         | Alias | Type   | Required | Default | Help                                                                     |
|--------------|-------|--------|----------|---------|--------------------------------------------------------------------------|
| `input_file` |       | `str`  | No       | `None`  |                                                                          |
| `--axis`     | `-a`  | `str`  | Yes      | `None`  | What axis to shrink the image on. (choices: `x`, `y`)                  |
| `--pixels`   | `-p`  | `int`  | Yes      | `None`  | How many pixels to shrink the image by.                                 |
| `--output`   | `-o`  | `str`  | No       | `None`  | What to name the new cropped image.                                      |
| `--interval` | `-i`  | `int`  | No       | `None`  | Save every i intermediate images.                                        |
| `--border`   | `-b`  | `bool` | No       |         | Whether or not to pad the cropped images to the size of the original     |
| `--show_seam`| `-s`  | `bool` | No       |         | Whether to highlight the removed seam on the intermediate images.       |

## Examples

1.  Shrink an image by 50 pixels along the x-axis and save the result:

    ```bash
    python seam_carver.py input.jpg --axis x --pixels 50 --output output.jpg
    ```

2.  Shrink an image by 30 pixels along the y-axis, save every 10 intermediate images with highlighted seams, and pad the output:

    ```bash
    python seam_carver.py input.png --axis y --pixels 30 --output output.png --interval 10 --show_seam --border
    ```

## Input/Output

| Input         | Output        |
|---------------|---------------|
| Image file    | Resized image |

## Testing

To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **`ImportError: No module named 'PIL'`**:  Make sure you have Pillow installed.  Run `pip install Pillow`.
2.  **Slow performance**: The seam carving algorithm can be computationally intensive. Consider using a smaller image or reducing the number of pixels to remove.

## Contributing

Coming soon

## License

Coming soon
