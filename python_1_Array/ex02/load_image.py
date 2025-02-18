import numpy as np
import matplotlib.image as mpimg
# import matplotlib.pyplot as plt


def ft_load(path: str):
    '''load an image and return array'''
    if not isinstance(path, str):
        raise ValueError("Error: wrong path format")
    if not path:
        raise ValueError("Error: Empty path")
    try:
        # read the image
        img = mpimg.imread(path)
        # # show the image
        # imgplot = plt.imshow(img)
        # plt.show()
        print(f"The shape of image is: {np.array(img).shape}")
        return img
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error: Cannot read {path} - {str(e)}")
