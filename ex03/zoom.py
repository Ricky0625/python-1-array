from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str, zfactor: int | float, start_pixel: tuple =(0,0)) -> np.ndarray:

    """
    ft_zoom(path: str, zfactor: int | float, start_pixel: tuple) -> np.ndarray
    
    NOTE: start_pixel is an optional argument. It has a default value of (0, 0).

    Return a zoomed img arr based on the zfactor(zoom in factor) and start pixel
    (if specified).
    """

    try:
        if not isinstance(zfactor, (int | float)):
            raise AssertionError("expecting factor to be an int")

        if zfactor < 1:
            raise AssertionError("expecting factor to be greater than 0")

        # load image
        img_arr = ft_load(path)
        if img_arr is None:
            return
        print(img_arr)

        # get the width and height of the img_arr, tuple unpacking operation
        (height, width, _) = img_arr.shape

        # calculate the new height and width based on the zoom factor
        new_dimension = min(height, width)
        new_height = int(new_dimension / zfactor)
        new_width = int(new_dimension / zfactor)

        left, upper = start_pixel
        right = left + new_width
        lower = upper + new_height

        if right > width or lower > height:
            raise AssertionError("zoomed region exceeds image dimension")
        
        zoomed_img_arr = img_arr[upper:lower, left:right]
        print(f"New shape after slicing: {zoomed_img_arr.shape}")
        print(zoomed_img_arr)
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
        img_arr = ft_zoom("animal.jpeg", 2, (450, 100))

        if img_arr is not None:
            plt.imshow(img_arr)
            plt.show()
    except KeyboardInterrupt:
        plt.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
