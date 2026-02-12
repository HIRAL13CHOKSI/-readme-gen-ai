# Resize Image Utility

## Overview
The Resize Image Utility is a Python script that provides various functions to resize and crop images using the Pillow library. It allows users to manipulate image dimensions while maintaining quality and aspect ratios.

## Features
- Resize images using different methods: crop, cover, contain, width, height, and thumbnail.
- Validate image dimensions before resizing to prevent errors.
- Support for various resampling techniques.
- Easy-to-use interface for resizing images.

## Installation
To use this utility, ensure you have Python and the Pillow library installed. You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage
To use the resizing functions, import the script and call the `resize` function with the desired method and parameters.

### Example Commands

```python
from PIL import Image
from resizeimage import resize  # Adjust the import based on your file structure

# Load an image
image = Image.open('path/to/your/image.jpg')

# Resize using different methods
cropped_image = resize('crop', image, [200, 200])
covered_image = resize('cover', image, [200, 200])
contained_image = resize('contain', image, [200, 200])
width_resized_image = resize('width', image, [200])
height_resized_image = resize('height', image, [200])
thumbnail_image = resize('thumbnail', image, [200, 200])
```

## Examples
Here are some examples of how to use the resizing functions:

1. **Crop an Image**:
   ```python
   cropped_image = resize('crop', image, [200, 200])
   ```

2. **Cover an Image**:
   ```python
   covered_image = resize('cover', image, [200, 200])
   ```

3. **Contain an Image**:
   ```python
   contained_image = resize('contain', image, [200, 200])
   ```

4. **Resize by Width**:
   ```python
   width_resized_image = resize('width', image, [200])
   ```

5. **Resize by Height**:
   ```python
   height_resized_image = resize('height', image, [200])
   ```

6. **Create a Thumbnail**:
   ```python
   thumbnail_image = resize('thumbnail', image, [200, 200])
   ```

## Limitations or Notes
- The script requires the Pillow library for image manipulation.
- Ensure that the image dimensions specified for cropping or resizing are valid; otherwise, an `ImageSizeError` will be raised.
- The script uses relative imports, which may cause issues if run as a standalone script. Adjust the import statements accordingly based on your project structure.
