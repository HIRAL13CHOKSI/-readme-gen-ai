# Seam Carver

Content-aware image resizing using seam carving.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/your_org/your_repo/actions)

## Overview

This project implements a seam carving algorithm to intelligently resize images by iteratively removing "unimportant" seams of pixels. Unlike traditional cropping or scaling, seam carving preserves prominent features by prioritizing the removal of areas with low visual energy.

Key features include:

*   **Axis-specific resizing**: Shrink images along either the horizontal (x) or vertical (y) axis.
*   **Customizable pixel reduction**: Specify the exact number of pixels to remove.
*   **Intermediate image saving**: Monitor the carving process by saving images at defined intervals.
*   **Seam visualization**: Highlight the removed seam on intermediate images to understand the algorithm's decisions.
*   **Border padding option**: Choose whether to pad the output images to their original size.

## Requirements

*   **Python**: `3.8+`
*   **Operating System**: Linux, macOS, Windows

## Dependencies

This project relies on the following packages:

### Third-Party Packages

*   `PIL` (Pillow)
*   `energy_functions`
*   `google-generativeai`
*   `groq`
*   `numba`
*   `numpy`
*   `openai`
*   `tqdm`
*   `utils`

### Standard Library Modules

*   `__future__`
*   `argparse`
*   `os`
*   `sys`

## Installation

To install the necessary dependencies, use `pip` with the provided `requirements.txt` file.

```bash
pip install -r ..\requirements.txt
```

For development, you can install the project in editable mode:

```bash
pip install -e .
```

## Usage

Run the `seam_carver.py` script from your terminal, providing an input image and specifying the desired resizing parameters.

```bash
python seam_carver.py input_file <value> --axis <value> --pixels <value> --output <value> --interval <value> --border <value> --show_seam <value>
```

## Flags

The script accepts the following command-line arguments:

| Flag        | Alias | Type | Required | Default | Help                                                               | Choices |
| :---------- | :---- | :--- | :------- | :------ | :----------------------------------------------------------------- | :------ |
| `input_file`|       | str  | False    | None    |                                                                    |         |
| `--axis`    | `-a`  | str  | True     | None    | What axis to shrink the image on.                                  | x, y    |
| `--pixels`  | `-p`  | int  | True     | None    | How many pixels to shrink the image by.                            |         |
| `--output`  | `-o`  | str  | False    | None    | What to name the new cropped image.                                |         |
| `--interval`| `-i`  | int  | False    | None    | Save every i intermediate images.                                  |         |
| `--border`  | `-b`  | bool | False    | None    | Whether or not to pad the cropped images to the size of the original |         |
| `--show_seam`| `-s` | bool | False    | None    | Whether to highlight the removed seam on the intermediate images.  |         |

## Environment Variables

None specified.

## Examples

### 1. Basic Image Resizing

Shrink an image `original.jpg` by 100 pixels along the x-axis and save it as `resized.jpg`:

```bash
python seam_carver.py original.jpg --axis x --pixels 100 --output resized.jpg
```

### 2. Resizing with Intermediate Saves and Seam Visualization

Shrink `landscape.png` by 50 pixels along the y-axis, saving an intermediate image every 10 removed pixels, and highlighting the removed seam. The output image will be named `landscape_shrunk.png`.

```bash
python seam_carver.py landscape.png -a y -p 50 -o landscape_shrunk.png -i 10 -s
```

## Input/Output

| Type  | Description                                     |
| :---- | :---------------------------------------------- |
| Input | An image file (e.g., JPG, PNG, BMP)             |
| Output| A resized image file, potentially with intermediates |

## Testing

This project includes a test suite. To run the tests, navigate to the project root directory and execute:

```bash
pytest
```

## Troubleshooting

*   **`ModuleNotFoundError`**: Ensure all dependencies listed in the `Dependencies` section are installed. Run `pip install -r ..\requirements.txt` again.
*   **`KeyError` or unexpected behavior with `--axis`**: Double-check that you are providing either `x` or `y` as the value for the `--axis` flag. No other values are accepted.
*   **Output image not found**: If `--interval` is used, intermediate images are saved in a subdirectory. The final image will be in the specified output path. If no `--output` is provided, the script might not save a final image explicitly, depending on its internal logic (though it's usually recommended to specify one).

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. See `CONTRIBUTING.md` (coming soon) for more details.

## License

This project is licensed under the MIT License. See the `LICENSE` file (coming soon) for full details.
