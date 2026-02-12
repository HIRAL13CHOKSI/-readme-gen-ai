```markdown
# Seam Carving Image Resizer

## Overview

This Python script implements seam carving, a content-aware image resizing technique. It intelligently removes or adds pixels (seams) from an image to change its dimensions while preserving important visual content. The script focuses on reducing the width or height of an image by removing vertical or horizontal seams.

## Features

*   **Content-aware resizing:**  Resizes images by removing low-energy seams, preserving important features.
*   **Axis selection:** Allows resizing along either the x-axis (width) or y-axis (height).
*   **Energy function:** Utilizes a dual-gradient energy function to identify low-energy seams.
*   **Intermediate image saving:** Saves intermediate images at specified intervals to visualize the seam carving process.
*   **Seam highlighting:**  Highlights the removed seam on intermediate images.
*   **Border padding:**  Pads the final cropped image to the original dimensions.

## Installation

1.  Install the required Python packages:

    ```bash
    pip install numpy Pillow tqdm numba
    ```

## Usage

Run the script from the command line with the following arguments:

```bash
python seam_carver.py input_file -a axis -p pixels [-o output] [-i interval] [-b border] [-s show_seam]
```

### Arguments:

*   `input_file`: The path to the input image file.
*   `-a`, `--axis`:  The axis to shrink the image on (`x` or `y`).  Required.
*   `-p`, `--pixels`: The number of pixels to shrink the image by. Required.
*   `-o`, `--output`: The name of the output image file.  If not specified, a default name is generated.
*   `-i`, `--interval`: Save every `interval` intermediate images.
*   `-b`, `--border`: Pad the cropped images to the size of the original (True/False).
*   `-s`, `--show_seam`: Highlight the removed seam on the intermediate images (True/False).

## Examples

1.  Shrink an image named `castle.jpg` by 100 pixels along the x-axis, saving the output as `castle_cropped.jpg`:

    ```bash
    python seam_carver.py castle.jpg -a x -p 100 -o castle_cropped.jpg
    ```

2.  Shrink an image named `castle.jpg` by 50 pixels along the y-axis, saving intermediate images every 10 iterations, and highlight the seams:

    ```bash
    python seam_carver.py castle.jpg -a y -p 50 -i 10 -s True
    ```

3.  Shrink an image named `castle.jpg` by 25 pixels along the x-axis, pad the final image to the original size, and name it `castle_padded.jpg`:

    ```bash
    python seam_carver.py castle.jpg -a x -p 25 -b True -o castle_padded.jpg
    ```

## Limitations or Notes

*   The script requires the `energy_functions` and `utils` modules. Since the script was provided without these dependencies, the script will not run. To run the code, these files must be created.
*   The script uses the dual-gradient energy function. Other energy functions could be implemented by modifying the `energy_map` function.
*   The script currently only supports shrinking images.  Expanding images using seam insertion is not implemented.
*   The `-b` and `-s` arguments require True/False arguments.
