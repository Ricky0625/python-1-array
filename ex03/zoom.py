from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
import sys


def ft_zoom(img_arr: np.ndarray, factor: int | float,
            start_px: tuple = (0, 0)) -> np.ndarray:

    """
    ft_zoom(path: str, zfactor: int | float, start_pixel: tuple) -> np.ndarray

    NOTE: start_pixel is an optional argument. Default value is (0, 0).

    Return a zoomed img arr based on the zfactor(zoom in factor)
    and start pixel (if specified).
    """

    try:
        if img_arr is None:
            raise AssertionError("img_arr is None")

        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")

        if not isinstance(factor, (int, float)):
            raise AssertionError("expecting factor to be an int")

        if not isinstance(start_px, tuple):
            raise AssertionError("expecting start_px to be a tuple")

        if not all([x >= 0 for x in start_px]):
            raise AssertionError("expecting start_px consists of " +
                                 "positive values only")

        if factor < 1:
            raise AssertionError("expecting factor to be greater than 0")

        # get the width and height of the img_arr, tuple unpacking operation
        (height, width, _) = img_arr.shape

        # calculate the new height and width based on the zoom factor
        new_dimension = min(height, width)
        new_height = int(new_dimension / factor)
        new_width = int(new_dimension / factor)

        left, upper = start_px
        right = left + new_width
        lower = upper + new_height

        if right > width or lower > height:
            raise AssertionError("zoomed region exceeds image dimension")

        zoomed_img_arr = img_arr[upper:lower, left:right]
        print(f"New shape after slicing: {zoomed_img_arr.shape}" +
              f" or ({zoomed_img_arr.shape[0]}, {zoomed_img_arr.shape[1]})")
        return zoomed_img_arr
    except Exception as e:
        print(f"[ERROR]: {e}")


def main():

    """
    main function
    1. load image
    2. zoom image
    3. display image
    """

    try:
        img_arr = ft_load("animal.jpeg")
        print(img_arr)
        zoomed = ft_zoom(img_arr, 2, (450, 100))
        print(zoomed)

        if zoomed is None:
            return
        plt.imshow(zoomed)
        plt.show()
    except KeyboardInterrupt:
        plt.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
