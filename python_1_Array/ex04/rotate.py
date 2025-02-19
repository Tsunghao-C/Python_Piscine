import matplotlib.pyplot as plt
from load_image import ft_load

try:
    # Load Original Image
    try:
        img = ft_load("cat_grayscale.jpeg")
        print(img)
    except ValueError as e:
        print(e)

    # # Convert to grey scale image
    # gray_img = img.mean(axis=2, keepdims=True)
    # print(f"Gray scale image: {gray_img.shape}")
    # print(gray_img)

    # Do transpose
    try:
        # Use transpose and explicitly assign y(1) to x(0) and x to y
        trans_img = img.transpose(1, 0)
        # Or use swapaxes to assgin which axes to swap
        # trans_img = slice_img.swapaxes(0, 1)
    except Exception as e:
        raise ValueError(f"Error: Transpose failed - {str(e)}")
    print(f"New shape after Transpose: {trans_img.shape}")
    print(trans_img)

    # Display Image
    imgplot = plt.imshow(trans_img, cmap='gray')
    plt.show()

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    plt.close()
