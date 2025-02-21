import matplotlib.image as mpimg
import numpy as np
import os


def ft_load(path: str):
    '''load an image and return array'''
    # Check input
    if not isinstance(path, str):
        raise ValueError("Error: wrong path format")
    if not path:
        raise ValueError("Error: Empty path")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: File {path} not found")

    # Check file format
    valid_extensions = ['.jpg', '.jpeg']
    if not any(path.lower().endswith(ext) for ext in valid_extensions):
        raise ValueError("Error: Unsupported file format.")
    try:
        # read the image
        # The return of imread() is alrady a numpy array
        img = mpimg.imread(path)
        if img is None:
            raise ValueError("Error: Image loading returned None")
        if not isinstance(img, np.ndarray):
            raise TypeError(f"Error: Expected numpy array, got {type(img)}")
        # print(f"The shape of image is: {img.shape}")
        return img
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error: Cannot read {path} - {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Error: Unknown error loading {path} - {str(e)}")
