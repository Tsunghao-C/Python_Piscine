import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def transpose_image(array: np.ndarray) -> np.ndarray:
    """
    mimic transpose function
    """
    height, width, channels = array.shape
    transposed_image = np.zeros((width, height, channels), dtype=array.dtype)
    for y in range(height):
        for x in range(width):
            transposed_image[x, y] = array[y, x]

    return transposed_image


def main():
    """
    Load image, slice a square part, grayscaled, rotate, and then display.
    """
    try:
        # Load Original Image
        try:
            img = ft_load("cat.jpeg")
            print(img)
        except ValueError as e:
            print(e)

        # Do slicing and grey scale
        try:
            slice_img = img[10:150, 105:245, :1]
        except IndexError as e:
            raise ValueError(f"Error: Slicing failed - out of bounds: {e}")

        if slice_img.size == 0:
            raise ValueError("Error: Slicing resulted in empty array")
        # print(f"New shape after slicing: {slice_img.shape}")
        # print(slice_img)

        # Do transpose
        try:
            trans_img = transpose_image(slice_img)
            # Use transpose and explicitly assign y(1) to x(0) and x to y
            # trans_img = slice_img.transpose(1, 0)
            # Or use swapaxes to assgin which axes to swap
            # trans_img = slice_img.swapaxes(0, 1)
        except Exception as e:
            raise ValueError(f"Error: Transpose failed - {str(e)}")
        print(f"New shape after Transpose: {trans_img.shape}")
        print(trans_img)

        # Display Image
        plt.imshow(trans_img, cmap='gray')
        plt.show()

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        plt.close()


if __name__ == "__main__":
    main()
