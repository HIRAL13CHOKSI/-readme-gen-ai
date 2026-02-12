# Seam Carver

## Overview
Seam Carver is a Python utility that intelligently crops images along a specified axis by removing low-energy seams. This technique is useful for resizing images while preserving important content.

## Features
- Crop images by removing vertical or horizontal seams.
- Supports different energy functions for seam calculation.
- Option to save intermediate images during the cropping process.
- Ability to highlight removed seams and pad images with borders.

## Installation
To use the Seam Carver script, ensure you have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install numpy Pillow tqdm numba
```

## Usage
Run the script from the command line with the following syntax:

```bash
python seam_carver.py <input_file> -a <axis> -p <pixels> [-o <output>] [-i <interval>] [-b <border>] [-s <show_seam>]
```

### Arguments
- `<input_file>`: Path to the input image file.
- `-a <axis>`: Axis to shrink the image on (`x` for vertical, `y` for horizontal).
- `-p <pixels>`: Number of pixels to remove from the image width or height.
- `-o <output>`: (Optional) Name for the output cropped image.
- `-i <interval>`: (Optional) Save every `i` intermediate images.
- `-b <border>`: (Optional) Whether to pad the cropped images to the size of the original (default: False).
- `-s <show_seam>`: (Optional) Whether to highlight the removed seam on the intermediate images (default: False).

### Example Commands
1. To crop an image named `input.jpg` by 50 pixels vertically and save it as `output.jpg`:
   ```bash
   python seam_carver.py input.jpg -a y -p 50 -o output.jpg
   ```

2. To crop an image and save every 10th intermediate image:
   ```bash
   python seam_carver.py input.jpg -a x -p 30 -i 10 -o output.jpg
   ```

3. To crop an image and highlight the removed seams:
   ```bash
   python seam_carver.py input.jpg -a y -p 20 -s True -o output.jpg
   ```

## Examples
- Given an image `landscape.jpg`, cropping it by 40 pixels horizontally:
  ```bash
  python seam_carver.py landscape.jpg -a x -p 40 -o landscape_cropped.jpg
  ```

- Cropping `portrait.jpg` by 30 pixels vertically and saving intermediate images:
  ```bash
  python seam_carver.py portrait.jpg -a y -p 30 -i 5 -o portrait_cropped.jpg
  ```

## Limitations or Notes
- The script requires the `energy_functions` module, which is not included in the provided code. Ensure this module is available in your environment for the script to run successfully.
- The script also relies on the `utils` module for various utility functions, which should be provided separately.
- The image processing may take time depending on the size of the image and the number of pixels to be removed.
