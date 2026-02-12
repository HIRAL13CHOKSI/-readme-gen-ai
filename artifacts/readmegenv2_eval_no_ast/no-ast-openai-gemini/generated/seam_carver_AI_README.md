# Seam Carver

## Overview
Seam Carver is a Python utility designed to intelligently crop images along a specified axis by removing vertical or horizontal seams. It utilizes energy functions to determine which pixels to remove, preserving the most important features of the image.

## Features
- Crop images along the x or y axis.
- Choose the number of pixels to remove.
- Option to highlight removed seams in intermediate images.
- Save intermediate images during the cropping process.
- Option to pad the cropped images to the original size.

## Installation
This script requires Python 3 and the following libraries:
- NumPy
- Pillow (PIL)
- Numba
- tqdm

You can install the required libraries using pip:
```bash
pip install numpy pillow numba tqdm
```

## Usage
Run the script from the command line with the following syntax:
```bash
python seam_carver.py <input_file> -a <axis> -p <pixels> [-o <output>] [-i <interval>] [-b <border>] [-s <show_seam>]
```

### Parameters:
- `<input_file>`: Path to the input image file.
- `-a <axis>`: Axis to shrink the image on. Choose either `x` or `y`.
- `-p <pixels>`: Number of pixels to remove from the image width or height.
- `-o <output>`: (Optional) Name for the output cropped image.
- `-i <interval>`: (Optional) Save every `i` intermediate images.
- `-b <border>`: (Optional) Whether to pad the cropped images to the size of the original (True/False).
- `-s <show_seam>`: (Optional) Whether to highlight the removed seam on intermediate images (True/False).

### Example Command
To crop an image named `example.jpg` by 50 pixels along the x-axis and save it as `example_cropped.jpg`, use:
```bash
python seam_carver.py example.jpg -a x -p 50 -o example_cropped.jpg
```

## Examples
1. **Crop 30 pixels from the height of an image:**
   ```bash
   python seam_carver.py image.png -a y -p 30 -o image_cropped.png
   ```

2. **Crop 20 pixels from the width and save every 5th intermediate image:**
   ```bash
   python seam_carver.py image.jpg -a x -p 20 -o image_cropped.jpg -i 5
   ```

3. **Crop with padding and highlight seams:**
   ```bash
   python seam_carver.py image.jpg -a y -p 10 -o image_cropped.jpg -b True -s True
   ```

## Limitations or Notes
- The script requires the `energy_functions` and `utils` modules, which are not provided in this code. Ensure these modules are available in your environment.
- The script does not handle exceptions for invalid input files or parameters, so ensure the input file exists and parameters are correct.
- The script may not work with all image formats; ensure compatibility with the Pillow library.
