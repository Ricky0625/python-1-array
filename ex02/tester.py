from load_image import ft_load
import matplotlib.pyplot as plt

img_arr = ft_load("mofyduck.jpeg")
try:
    if (img_arr is not None):
        plt.imshow(img_arr)
        plt.show()
except KeyboardInterrupt:
    plt.close()
except Exception as e:
    print(e)
