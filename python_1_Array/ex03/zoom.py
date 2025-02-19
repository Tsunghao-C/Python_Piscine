import matplotlib.pyplot as plt
from load_image import ft_load

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
        raise ValueError(f"Error: Slicing failed - index out of bounds: {e}")

    if slice_img.size == 0:
        raise ValueError("Error: Slicing resulted in empty array")
    print(f"New shape after slicing: {slice_img.shape}")
    print(slice_img)

    # Display Image
    imgplot = plt.imshow(slice_img, cmap='gray')
    plt.show()

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    plt.close()


# This part to download grayscale image
# from PIL import Image


# image = Image.fromarray(slice_img)
# image.save('output.jpeg')
