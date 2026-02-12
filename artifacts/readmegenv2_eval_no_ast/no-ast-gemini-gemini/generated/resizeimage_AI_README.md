This README describes `resizeimage.py`, a Python module for various image resizing operations.

# `resizeimage.py`

This Python module provides a collection of utility functions for robust image resizing using the Pillow library. It offers several methods for manipulating image dimensions, including cropping, fitting, covering, and resizing to specific widths or heights, while maintaining aspect ratios where appropriate.

## Overview

`resizeimage.py` acts as a module that exports several functions to handle common image resizing tasks. It is designed to be imported into other Python scripts, providing a flexible API for processing images with different scaling and cropping strategies.

## Features

*   **`resize_crop(image, size)`**: Crops the image to a specified `size` from its center. Requires the original image to be at least as large as the target size.
*   **`resize_cover(image, size, resample=Image.LANCZOS)`**: Resizes and then crops the image to completely cover the specified `size`, maintaining the aspect ratio.
*   **`resize_contain(image, size, resample=Image.LANCZOS, bg_color=(255, 255, 255, 0))`**: Resizes the image to fit entirely within the specified `size`, maintaining the aspect ratio. If the image doesn't fill the entire `size`, it's centered and the remaining space is filled with a `bg_color` (defaulting to transparent).
*   **`resize_width(image, size, resample=Image.LANCZOS)`**: Resizes the image to a specific width (provided as `size`), maintaining the aspect ratio. Requires the original image width to be greater than or equal to the target width.
*   **`resize_height(image, size, resample=Image.LANCZOS)`**: Resizes the image to a specific height (provided as `size`), maintaining the aspect ratio. Requires the original image height to be greater than or equal to the target height.
*   **`resize_thumbnail(image, size, resample=Image.LANCZOS)`**: Creates a thumbnail of the image that fits within the specified `size`, preserving its aspect ratio.
*   **`resize(method, *args, **kwargs)`**: A convenient dispatcher function that allows calling any of the above resize methods by their name (e.g., `'crop'`, `'cover'`).
*   **Input Validation**: Some methods include built-in validation to prevent operations that would enlarge the image beyond its original dimensions, raising an `ImageSizeError` if such conditions are met.

## Installation

This module primarily depends on the Pillow library for image manipulation.

1.  **Install Pillow**:
    ```bash
    pip install Pillow
    ```
2.  **Integrate the Module**:
    Place `resizeimage.py` in your project directory or a location on your Python path.

    **Note on `imageexceptions.py`**:
    The script uses a relative import `from .imageexceptions import ImageSizeError`. This indicates that it is designed as a module within a larger Python package and expects a companion module named `imageexceptions.py` to be present in the same package for custom error handling. If you intend to use this script as a standalone file, you might need to adapt the `ImageSizeError` import or provide a simple `imageexceptions.py` file defining this class if its error handling is critical for your use case.

## Usage

As `resizeimage.py` is a module, you use it by importing its functions into your Python script.

```python
from PIL import Image
# Assuming resizeimage.py is in the same directory or on your Python path
# You might need to adjust the import based on your project structure if the
# relative import for ImageSizeError is resolved (e.g., as part of a package).
from resizeimage import resize_cover, resize_contain, resize_width, resize 

# Open an image (replace "your_image.jpg" with your actual image path)
try:
    img = Image.open("your_image.jpg")
except FileNotFoundError:
    print("your_image.jpg not found. Creating a dummy image for demonstration.")
    img = Image.new('RGB', (800, 600), color='blue')
    img.save("your_image.jpg")
    img = Image.open("your_image.jpg")

print(f"Original image size: {img.size}")

# Example 1: Using the 'resize' dispatcher function
# Resize to cover a 300x200 area
resized_img_cover = resize('cover', img, [300, 200])
resized_img_cover.save("output_cover_dispatcher.jpg")
print(f"Dispatcher cover result size: {resized_img_cover.size}")

# Example 2: Using individual functions
# Resize to contain within a 400x300 area with a white background
resized_img_contain = resize_contain(img, [400, 300], bg_color=(255, 255, 255))
resized_img_contain.save("output_contain_white_bg.png")
print(f"Contain result size (white bg): {resized_img_contain.size}")

# Example 3: Resize to a specific width
# Resize to a width of 200 pixels
resized_img_width = resize_width(img, 200)
resized_img_width.save("output_width_200px.jpg")
print(f"Width resize result size: {resized_img_width.size}")

print("\nCheck the 'output_*.jpg/png' files for results.")
```

## Examples

Below are more detailed examples demonstrating the various resizing methods.

```python
from PIL import Image
# Import all desired resize functions
from resizeimage import resize_crop, resize_cover, resize_contain, resize_width, resize_height, resize_thumbnail

# Load an example image or create a dummy one if it doesn't exist
try:
    original_image = Image.open("example.jpg")
except FileNotFoundError:
    # Create a dummy image for testing if example.jpg doesn't exist
    print("example.jpg not found. Creating a dummy 'example.jpg' for demonstration.")
    original_image = Image.new('RGB', (800, 600), color='green')
    original_image.save("example.jpg")
    original_image = Image.open("example.jpg") # Reload to get a proper Pillow image object

print(f"Original image size: {original_image.size}")

# 1. Resize Crop
# Crops the image to a 200x200 square from the center.
try:
    cropped_image = resize_crop(original_image, [200, 200])
    cropped_image.save("output_crop_200x200.jpg")
    print(f"Crop result size: {cropped_image.size}")
except Exception as e: # Catch ImageSizeError if image is too small
    print(f"Could not perform resize_crop (image too small or ImageSizeError not defined): {e}")

# 2. Resize Cover
# Resizes and crops to completely cover a 300x200 area.
covered_image = resize_cover(original_image, [300, 200])
covered_image.save("output_cover_300x200.jpg")
print(f"Cover result size: {covered_image.size}")

# 3. Resize Contain
# Resizes to fit within a 400x300 area, padding with a transparent background.
contained_image = resize_contain(original_image, [400, 300], bg_color=(0, 0, 0, 0)) # transparent background
contained_image.save("output_contain_400x300.png")
print(f"Contain result size: {contained_image.size}")

# 4. Resize Width
# Resizes the image to have a width of 150 pixels, maintaining aspect ratio.
try:
    width_resized_image = resize_width(original_image, 150)
    width_resized_image.save("output_width_150.jpg")
    print(f"Width resize result size: {width_resized_image.size}")
except Exception as e: # Catch ImageSizeError if original width is smaller than 150
    print(f"Could not perform resize_width (original width too small or ImageSizeError not defined): {e}")


# 5. Resize Height
# Resizes the image to have a height of 100 pixels, maintaining aspect ratio.
try:
    height_resized_image = resize_height(original_image, 100)
    height_resized_image.save("output_height_100.jpg")
    print(f"Height resize result size: {height_resized_image.size}")
except Exception as e: # Catch ImageSizeError if original height is smaller than 100
    print(f"Could not perform resize_height (original height too small or ImageSizeError not defined): {e}")

# 6. Resize Thumbnail
# Creates a thumbnail that fits within 128x128.
thumbnail_image = resize_thumbnail(original_image, [128, 128])
thumbnail_image.save("output_thumbnail_128x128.jpg")
print(f"Thumbnail result size: {thumbnail_image.size}")

print("\nAll example operations completed. Check the 'output_*.jpg/png' files.")
```

## Limitations or Notes

*   **Module Structure**: This script is designed as a Python module intended to be part of a larger package. The relative import `from .imageexceptions import ImageSizeError` implies a specific package structure. It cannot be directly executed as a top-level script (e.g., `python resizeimage.py`) if `imageexceptions.py` is not properly set up as a sibling module within a Python package.
*   **Dependency**: Requires the `Pillow` library for all image processing operations.
*   **Validation**: Some resizing functions (`resize_crop`, `resize_cover`, `resize_width`, `resize_height`) include built-in validation to ensure the target dimensions are not larger than the original image's corresponding dimensions. Attempting such operations will raise an `ImageSizeError`.
*   **Resampling Filter**: Most resizing functions allow specifying a `resample` filter (e.g., `Image.LANCZOS`, `Image.BICUBIC`, `Image.BILINEAR`) to control the quality of the resizing operation. `Image.LANCZOS` is used by default for high-quality downsampling.
