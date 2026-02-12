# Resize Image

A Python utility for flexible image resizing operations.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/your-package.svg)](https://pypi.org/project/your-package/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/rust-lang/rust)

## Overview

`resizeimage.py` provides a comprehensive set of functions for resizing images, leveraging the powerful Pillow library. It offers various resizing methods including `crop`, `cover`, `contain`, `width`, `height`, and `thumbnail`, allowing developers to precisely control how images are scaled and adapted. The module also features a robust `validate` decorator for argument validation, ensuring reliable image processing.

## Requirements

*   **Python Version**: Python 3.x
*   **Operating System**: Platform-independent

## Dependencies

### Python Dependencies

The following Python packages are directly used by `resizeimage.py`:

*   **Pillow** (`PIL`): Essential for image manipulation and processing.
*   **imageexceptions**: A dependency for handling image-related exceptions within the module.

The broader project may also include:

*   `google-generativeai`
*   `groq`
*   `openai`

### External Tools

None specified.

## Installation

To install the necessary dependencies for the project, navigate to the project root directory and run the following command, referencing the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

This will install `Pillow`, `imageexceptions`, and any other project-wide dependencies specified in the `requirements.txt` file.

## Usage

While primarily designed for programmatic integration, the script can be invoked directly (though it offers limited functionality without explicit function calls):

```bash
python resizeimage.py
```

For practical image resizing, import `resizeimage.py` as a module into your Python applications.

## Flags

None. This script does not expose command-line flags.

## Environment Variables

None.

## Examples

The primary use case for `resizeimage.py` is to import its functions into your Python code to perform image resizing operations. Below are examples demonstrating common resizing methods.

First, ensure you have an image file (e.g., `input.jpg`) available for these examples.

```python
# Assuming resizeimage.py is in your Python path or current directory
from PIL import Image
from resizeimage import resizeimage

# Load an image
try:
    with Image.open('input.jpg') as image:
        # Example 1: Resize using resize_cover (fills the entire specified area, cropping if necessary)
        # Target size: 200x200 pixels
        cover_image = resizeimage.resize_cover(image, [200, 200])
        cover_image.save('output_cover.jpg', image.format)
        print("Image resized using 'cover' method and saved as output_cover.jpg")

        # Example 2: Resize using resize_thumbnail (resizes to fit within given dimensions, maintaining aspect ratio)
        # Target thumbnail size: 128x128 pixels
        thumbnail_image = resizeimage.resize_thumbnail(image, [128, 128])
        thumbnail_image.save('output_thumbnail.jpg', image.format)
        print("Image resized using 'thumbnail' method and saved as output_thumbnail.jpg")

        # Example 3: Resize to a specific width, height adjusted automatically
        # Target width: 300 pixels
        width_image = resizeimage.resize_width(image, 300)
        width_image.save('output_width.jpg', image.format)
        print("Image resized by width and saved as output_width.jpg")

        # Example 4: Resize using resize_contain (fits image within specified area, adding padding if necessary)
        # Target size: 250x250 pixels
        contain_image = resizeimage.resize_contain(image, [250, 250])
        contain_image.save('output_contain.jpg', image.format)
        print("Image resized using 'contain' method and saved as output_contain.jpg")

except FileNotFoundError:
    print("Error: input.jpg not found. Please ensure an image file named 'input.jpg' exists.")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Input/Output

| Type   | Description                                 |
| :----- | :------------------------------------------ |
| **Input** | A `Pillow.Image.Image` instance, and a size (integer or list/tuple `[width, height]`). |
| **Output** | A new `Pillow.Image.Image` instance, representing the resized image. |

## Testing

This project includes tests to ensure the reliability of its image resizing functions. To run the tests, navigate to the project root and execute `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **`PIL.Image.open` or image processing errors**:
    *   **Issue**: You might encounter `FileNotFoundError` or issues related to image format.
    *   **Solution**: Ensure the input image file exists at the specified path and has a supported format (e.g., JPEG, PNG). Verify `Pillow` is correctly installed.
2.  **`ModuleNotFoundError: No module named 'resizeimage'`**:
    *   **Issue**: Python cannot find the `resizeimage.py` module when you try to `import resizeimage`.
    *   **Solution**: Make sure `resizeimage.py` is in the same directory as your script, or that its directory is included in your Python path (`sys.path`). For larger projects, consider setting up a proper package structure.
3.  **`ModuleNotFoundError: No module named 'imageexceptions'`**:
    *   **Issue**: The `imageexceptions` module, listed as a dependency, is not found.
    *   **Solution**: Ensure `imageexceptions` is correctly installed. If it's a local project dependency, confirm it's part of your project's `requirements.txt` and installed via `pip install -r ../requirements.txt`. If it's an internal module, verify its path.

## Contributing

Contributions are welcome! Please refer to the project's contribution guidelines (coming soon) for more details on how to get started.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
