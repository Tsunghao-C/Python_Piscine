import matplotlib.pyplot as plt
from load_image import ft_load


try:
    img = ft_load("cat.jpg")
    print(img)
except ValueError as e:
    print(e)

try:
    slice_img = img[10:150, 100:250, :1]
except ValueError as e:
    print(e)
print(f"New shape after slicing: {slice_img.shape}")
print(slice_img)
imgplot = plt.imshow(slice_img)
plt.show()
