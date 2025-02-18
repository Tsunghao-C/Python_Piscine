import matplotlib.image as mpimg


def ft_load(path: str):
    '''load an image and return array'''
    if not isinstance(path, str):
        raise ValueError("Error: wrong path format")
    if not path:
        raise ValueError("Error: Empty path")
    try:
        # read the image
        # The return of imread() is alrady a numpy array
        img = mpimg.imread(path)
        print(f"The shape of image is: {img.shape}")
        return img
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error: Cannot read {path} - {str(e)}")
