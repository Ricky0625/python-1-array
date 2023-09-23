from load_image import ft_load, ft_zoom
import numpy as np
import matplotlib.pyplot as plt
import sys


def ft_transpose(img_arr: np.ndarray) -> np.ndarray:

    """
    ft_transpose(img_arr: np.ndarray) -> np.ndarray

    Return a transposed np array. Takes in a np array and Transpose it.
    Columns become rows; Rows become columns.
    """

    try:
        if img_arr is None:
            raise AssertionError("img_arr is None")

        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be numpy array")

        new_rows = []

        # shape = (height, width, channel)
        num_of_cols = img_arr.shape[1]
        for i in range(num_of_cols):
            col = img_arr[:, i]
            new_rows.append(col)

        transposed = np.array(new_rows)
        (width, height, _) = transposed.shape
        print(f"New shape after Transpose: ({width}, {height})")
        return transposed
    except Exception as e:
        print(f"[ERROR]: {e}")


def main():

    """
    main function
    1. load image
    2. zoom image
    3. transpose image
    4. display image
    """

    try:
        img_arr = ft_load("animal.jpeg")
        zoomed = ft_zoom(img_arr, 2, (450, 100))
        print(zoomed)
        transposed = ft_transpose(zoomed)
        print(transposed)

        if transposed is None:
            sys.exit()
        plt.imshow(transposed)
        plt.show()
    except KeyboardInterrupt:
        plt.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
