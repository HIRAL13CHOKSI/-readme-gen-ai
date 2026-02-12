# Resize Image Utility

## Overview
The Resize Image Utility is a Python script that provides various functions to resize and crop images using the Pillow library. It allows users to manipulate images by resizing them to specific dimensions while maintaining their aspect ratios or cropping them as needed.

## Features
- Resize images using different methods: crop, cover, contain, width, height, and thumbnail.
- Validate image dimensions before resizing to prevent errors.
- Support for custom background colors when resizing to fit a specific size.
- Easy-to-use interface for resizing images through a single function call.

## Installation
To use this script, you need to have Python and the Pillow library installed. You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage
To use the resizing functions, you can import the script and call the `resize` function with the desired method and parameters.

### Example Commands
```python
from PIL import Image
from resizeimage import resize  # Adjust import based on your script's location

# Open an image file
image = Image.open('path/to/your/image.jpg')

# Resize using different methods
cropped_image = resize('crop', image, [200, 200])
covered_image = resize('cover', image, [300, 300])
contained_image = resize('contain', image, [300, 300])
width_resized_image = resize('width', image, [250])
height_resized_image = resize('height', image, [250])
thumbnail_image = resize('thumbnail', image, [100, 100])
```

## Examples
1. **Crop an Image**: Resize an image to a centered rectangle of 200x200 pixels.
2. **Cover an Image**: Resize an image to cover a 300x300 pixel area, cropping as necessary.
3. **Contain an Image**: Resize an image to fit within a 300x300 pixel area, maintaining the aspect ratio.
4. **Resize by Width**: Resize an image to a width of 250 pixels, adjusting the height accordingly.
5. **Resize by Height**: Resize an image to a height of 250 pixels, adjusting the width accordingly.
6. **Create a Thumbnail**: Create a thumbnail of an image with maximum dimensions of 100x100 pixels.

## Limitations or Notes
- The script requires the Pillow library to function correctly.
- Ensure that the input image is larger than the desired output size when using methods that validate dimensions (e.g., `crop`, `cover`).
- The script currently does not handle exceptions related to file I/O or unsupported image formats; users should implement their own error handling as needed.
