```markdown
# seam_carver.py

## Overview
`seam_carver.py` is a Python utility that implements the seam carving algorithm for content-aware image resizing. This technique intelligently reduces an image's dimensions by iteratively removing the "least important" pixel seams, which allows for resizing without distorting important visual content, unlike traditional scaling or cropping methods. The script supports shrinking images along either the horizontal (X) or vertical (Y) axis.

## Features
*   **Content-Aware Resizing**: Reduces image width or height by removing low-energy seams, preserving salient features.
*   **Axis Selection**: Choose to remove seams along the X-axis (reducing width) or Y-axis (reducing height).
*   **Progressive Saving**: Option to save intermediate images at specified intervals during the resizing process, showing the carving progression.
*   **Seam Visualization**: Ability to highlight the exact seam being removed in red on any generated intermediate images.
*   **Output Padding**: Option to pad the final (or intermediate) cropped images with a black border to maintain the original image's dimensions.

## Installation
This script has several external Python dependencies and relies on companion utility files that must be present in the same directory.

1.  **Python Dependencies**: Install the required libraries using pip:
    ```bash
    pip install numpy Pillow numba tqdm
    ```
2.  **Companion Files**: This script imports functions from `energy_functions.py` and `utils.py`. For the script to run successfully, these two files must be located in the same directory as `seam_carver.py`. Without them, you will encounter a `ModuleNotFoundError`.

## Usage
Execute the script from your command line, providing an input image and specifying the desired reduction parameters.

```bash
python seam_carver.py <input_file> --axis <x|y> --pixels <number_of_pixels> [OPTIONS]
```

### Arguments

*   `<input_file>`: Path to the image file you wish to resize.
*   `-a`, `--axis` (required): Specifies the dimension along which to shrink the image.
    *   Choices: `x` (for width) or `y` (for height).
*   `-p`, `--pixels` (required): The exact number of pixels to remove from the specified axis.

### Options

*   `-o`, `--output` `<filename>`: The name for the resulting cropped image. If omitted, the script generates a filename by appending `_crop` before the extension of the input file (e.g., `image.jpg` becomes `image_crop.jpg`).
*   `-i`, `--interval` `<int>`: If provided, the script will save a copy of the image every `i` pixels removed. These intermediate images are stored in a new subdirectory named after the base of your output file.
*   `-b`, `--border`: If this flag is present, any saved images (final or intermediate) will be padded with a black border to maintain the original input image's dimensions.
*   `-s`, `--show_seam`: If this flag is present, the specific seam being removed will be highlighted in red on any intermediate images saved using the `--interval` option.

## Examples

1.  **Shrink `my_photo.png` by 100 pixels along its width (x-axis), saving the output as `my_photo_crop.png`:**
    ```bash
    python seam_carver.py my_photo.png --axis x --pixels 100
    ```

2.  **Reduce `wide_image.jpg` by 50 pixels along its height (y-axis), saving the result to `tall_image.jpg`:**
    ```bash
    python seam_carver.py wide_image.jpg --axis y --pixels 50 --output tall_image.jpg
    ```

3.  **Perform an aggressive reduction, saving progress, highlighting seams, and padding:**
    Shrink `landscape.jpeg` by 200 pixels along the X-axis. Save an intermediate image every 25 pixels, highlight the seam being removed on those intermediate images, and pad all output images to the original dimensions.
    ```bash
    python seam_carver.py landscape.jpeg --axis x --pixels 200 --output resized_landscape.jpeg --interval 25 --show_seam --border
    ```
    This command will create a directory named `resized_landscape` containing images like `resized_landscape_025.jpeg`, `resized_landscape_050.jpeg`, etc., and the final `resized_landscape.jpeg` in the main directory.

## Limitations or Notes
*   **Required Companion Files**: As noted in the Installation section, `seam_carver.py` is designed to work alongside `energy_functions.py` and `utils.py`. These files are essential for the script's operation and must be placed in the same directory.
*   **Default Energy Function**: The script is configured to use the `dual_gradient_energy` function (imported from `energy_functions.py`) as its default method for calculating pixel energy and importance.
*   **Boolean Flags**: For options like `--border` and `--show_seam`, simply including the flag in your command enables the feature. Omitting the flag will disable it.
*   **Performance Optimization**: The `numba` library is leveraged to significantly accelerate the `cumulative_energy` calculation, which is a core part of the seam carving process.
```
