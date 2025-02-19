import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''Invert the color of the image received.'''
    # Check input
    if not isinstance(array, np.ndarray):
        raise ValueError("Error: wrong input format")
    if array is None:
        raise ValueError("Error: Empty input")
    if array.ndim not in [2, 3]:
        raise ValueError("Error: Wrong array size, must be 2D or 3D array")

    # Process image
    inverted = 255 - array
    print(inverted)

    # Display image
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    '''Filter red color of the image received.'''
    # Check input
    if not isinstance(array, np.ndarray):
        raise ValueError("Error: wrong input format")
    if array is None:
        raise ValueError("Error: Empty input")
    if array.ndim != 3:
        raise ValueError("Error: Wrong array size, must be 3D array")

    # Process image
    red = np.zeros_like(array)
    red[:, :, 0] = array[:, :, 0]
    print(red)

    # Display image
    Image.fromarray(red).show()
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    '''Filter green color of the image received.'''
    # Check input
    if not isinstance(array, np.ndarray):
        raise ValueError("Error: wrong input format")
    if array is None:
        raise ValueError("Error: Empty input")
    if array.ndim != 3:
        raise ValueError("Error: Wrong array size, must be 3D array")

    # Process image
    green = np.zeros_like(array)
    green[:, :, 1] = array[:, :, 1]
    print(green)

    # Display image
    Image.fromarray(green).show()
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''Filter blue color of the image received.'''
    # Check input
    if not isinstance(array, np.ndarray):
        raise ValueError("Error: wrong input format")
    if array is None:
        raise ValueError("Error: Empty input")
    if array.ndim != 3:
        raise ValueError("Error: Wrong array size, must be 3D array")

    # Process image
    # Use zeros_like to create a zero matrix with same shape
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    print(blue)

    # Display image
    Image.fromarray(blue).show()
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''Change to grayscaled image'''
    # Check input
    if not isinstance(array, np.ndarray):
        raise ValueError("Error: wrong input format")
    if array is None:
        raise ValueError("Error: Empty input")
    if array.ndim != 3:
        raise ValueError("Error: Wrong array size, must be 3D array")

    # Process image
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey = np.stack([grey_channel, grey_channel, grey_channel], axis=2)

    # Display image
    Image.fromarray(grey.astype(np.uint8)).show()
    return grey
