```markdown
# Image Resizing Utility

## Overview

This Python script provides a collection of image resizing functions built on top of the Pillow (PIL) library. It offers various resizing methods, including cropping, covering, containing, adjusting by width or height, and creating thumbnails. The script focuses on providing flexible image manipulation options while handling potential errors related to image size.

**Note:** This script depends on the `PIL` library, but due to an import error during analysis, handling of `ImageSizeError` is not fully understood.

## Features

*   **Multiple Resizing Methods:** Offers 'crop', 'cover', 'contain', 'width', 'height', and 'thumbnail' resizing options.
*   **Validation:** Includes validation to ensure the target size is not larger than the original image (except for contain).
*   **Pillow Integration:** Built using the Pillow (PIL) library for image processing.

## Installation

1.  Make sure you have Python installed.
2.  Install the Pillow library using pip:

    ```bash
    pip install Pillow
    ```

## Usage

The script defines several functions for resizing images. The main entry point is the `resize` function, which acts as a dispatcher for the other resizing functions.

### `resize(method, image, size, **kwargs)`

This function selects the appropriate resizing method based on the `method` argument and calls the corresponding function.

*   `method`: A string specifying the resizing method to use. Valid options are 'crop', 'cover', 'contain', 'width', 'height', and 'thumbnail'.
*   `image`: A Pillow image object.
*   `size`: A list or tuple of two integers representing the desired width and height (except for `width` and `height` methods where it can be a single integer).
*   `**kwargs`: Additional keyword arguments that are passed to the underlying resizing function (e.g., `resample` for resampling filter, `bg_color` for `contain` method).

## Examples

Here are a few examples demonstrating how to use the `resize` function:

1.  **Resizing and Cropping an Image:**

    ```python
    from PIL import Image
    from resizeimage import resize

    image = Image.open('input.jpg')
    size = [200, 200]
    cropped_image = resize.resize('crop', image, size)
    cropped_image.save('output_cropped.jpg', image.format)
    ```

2.  **Resizing to Cover:**

    ```python
    from PIL import Image
    from resizeimage import resize

    image = Image.open('input.jpg')
    size = [200, 200]
    covered_image = resize.resize('cover', image, size)
    covered_image.save('output_covered.jpg', image.format)
    ```

3.  **Resizing to Contain with a White Background:**

    ```python
    from PIL import Image
    from resizeimage import resize

    image = Image.open('input.png') #transparent image
    size = [200, 200]
    contained_image = resize.resize('contain', image, size, bg_color=(255, 255, 255, 0))
    contained_image.save('output_contained.png', image.format)
    ```

4.  **Resizing by Width:**

    ```python
    from PIL import Image
    from resizeimage import resize

    image = Image.open('input.jpg')
    width = 200
    resized_image = resize.resize('width', image, width)
    resized_image.save('output_width.jpg', image.format)
    ```

5.  **Creating a Thumbnail:**

    ```python
    from PIL import Image
    from resizeimage import resize

    image = Image.open('input.jpg')
    size = [100, 100]
    thumbnail_image = resize.resize('thumbnail', image, image, size)
    thumbnail_image.save('output_thumbnail.jpg', image.format)
    ```

## Limitations or Notes

*   The script relies heavily on the Pillow (PIL) library. Ensure it is correctly installed.
*   Error handling for invalid image sizes is present, potentially raising an `ImageSizeError` which seems to be defined in a separate module, but this couldn't be confirmed. The script validates that the target `size` dimensions for `crop`, `cover`, `width`, and `height` are not larger than the original image dimensions.
*   The `resize_contain` function defaults to a transparent background color (255, 255, 255, 0). To use a different background, provide the `bg_color` argument.
*   Resampling uses `Image.LANCZOS` by default, but this can be changed via the `resample` argument in the `resize_cover`, `resize_contain`, `resize_width`, `resize_height` and `resize_thumbnail` functions.
