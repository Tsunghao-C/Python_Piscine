import matplotlib.image as mpimg
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    '''load an image and return the image in np.ndarray'''
    try:
        # Check input
        if not isinstance(path, str):
            raise AssertionError("wrong path format")
        if not path:
            raise AssertionError("Empty path")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} not found")

        # Check file format
        valid_extensions = ['.jpg', '.jpeg']
        if not any(path.lower().endswith(ext) for ext in valid_extensions):
            raise AssertionError("Unsupported file format.")

        # read the image
        # The return of imread() is alrady a numpy array
        img = mpimg.imread(path)
        if img is None:
            raise ValueError("Error: Image loading returned None")
        if not isinstance(img, np.ndarray):
            raise ValueError(f"Error: Expected numpy array, got {type(img)}")
        # print(f"The shape of image is: {img.shape}")
        return img
    except AssertionError as e:
        print("AssertionError:", e)
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except ValueError as e:
        print("ValueError", e)
    except Exception as e:
        print("Unexpected Error:", e)
    return None
