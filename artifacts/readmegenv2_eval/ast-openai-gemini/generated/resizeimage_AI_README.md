```markdown
# Resize Image Tool
A Python utility for resizing images with various methods.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
The Resize Image Tool is a Python script that provides functions for resizing and validating images using the Pillow library. It supports multiple resizing methods, including cropping, covering, containing, and resizing by width or height. This tool is designed for ease of use and flexibility in image manipulation.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform

## Dependencies
### Standard Library Modules
- `__future__`
- `functools`
- `math`
- `sys`

### Third-Party Packages
- `PIL`
- `imageexceptions`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To run the script, use the following command:

```bash
python resizeimage.py
```

## Flags
None

## Environment Variables
| Name | Default | Description |
|------|---------|-------------|
| None specified | | Controls runtime behavior |

## Examples
### Example 1: Basic Usage
Run the script to execute the default functionality:
```bash
python resizeimage.py
```

### Example 2: Resizing an Image
You can call the resizing functions directly in your Python code:
```python
from PIL import Image
from resizeimage import resize

image = Image.open('path/to/image.jpg')
resized_image = resize.resize_cover(image, [800, 600])
resized_image.save('path/to/resized_image.jpg')
```

## Input/Output
| Input | Output |
|-------|--------|
| Image file | Resized image file |

## Testing
To run tests, use `pytest` as the default testing framework. Ensure you have it installed and run:

```bash
pytest
```

## Troubleshooting
- **Issue**: Image not found error.
  - **Solution**: Ensure the image path is correct.
  
- **Issue**: Unsupported image format.
  - **Solution**: Check if the image format is supported by Pillow.

## Contributing
Coming soon.

## License
Coming soon.
```
