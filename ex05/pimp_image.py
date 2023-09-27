from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_show_img(img_arr: np.ndarray):

    """
    Helper function to show image
    """

    try:
        plt.imshow(img_arr)
        plt.show()
    except KeyboardInterrupt:
        plt.close()


def ft_invert(img_arr: np.ndarray) -> np.ndarray:

    """
    Inverts the color of the image received
    Minus 255 to each of the RGB value
    """

    try:
        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")
        
        inverted = 255 - img_arr
        ft_show_img(inverted)
    except Exception as e:
        print(f"[ERROR]: {e}")


def ft_red(img_arr: np.ndarray) -> np.ndarray:

    """
    Only keep the Red color channel of the image received
    """

    try:
        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")
        
        # create a new array which has the same shape as the ori img_arr
        red_image = np.zeros_like(img_arr)
        # [:, :, 0] refers to the Red channel of the image. 1 is Green, 2 is Blue
        red_image[:, :, 0] = img_arr[:, :, 0]
        ft_show_img(red_image)
    except Exception as e:
        print(f"[ERROR]: {e}")


def ft_green(img_arr: np.ndarray) -> np.ndarray:

    """
    Only keep the Green color channel of the image received
    """

    try:
        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")
        # create a new array which has the same shape as the ori img_arr
        green_image = np.zeros_like(img_arr)
        # 0 is Red. 1 is Green, 2 is Blue
        green_image[:, :, 1] = img_arr[:, :, 1]
        ft_show_img(green_image)
    except Exception as e:
        print(f"[ERROR]: {e}")


def ft_blue(img_arr: np.ndarray) -> np.ndarray:

    """
    Only keep the Blue color channel of the image received
    """

    try:
        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")
        # create a new array which has the same shape as the ori img_arr
        blue_image = np.zeros_like(img_arr)
        # 0 is Red. 1 is Green, 2 is Blue
        blue_image[:, :, 2] = img_arr[:, :, 2]
        ft_show_img(blue_image)
    except Exception as e:
        print(f"[ERROR]: {e}")


def ft_grey(img_arr: np.ndarray) -> np.ndarray:

    """
    Makes the received image into grayscale
    """

    try:
        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")
        
        # calculate the mean value of the rgb value (this will create one value)
        # axis 2 to target the color channels
        grayscale = np.mean(img_arr, axis=2)
        # expand the grayscale value to r,g,b using repeat
        # np.newaxis will create a new axis along the rows
        grayscale = np.repeat(grayscale[:, :, np.newaxis], 3, axis=2).astype(np.uint8)
        ft_show_img(grayscale)
    except Exception as e:
        print(f"[ERROR]: {e}")
