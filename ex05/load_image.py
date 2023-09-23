from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:

    """
    ft_load(path: str) -> numpy array

    Return a numpy array. The array is generated by converting
    an Image object to a numpy array.
    """

    try:
        if not isinstance(path, str):
            raise AssertionError("path must be a string")

        if path == "":
            raise AssertionError("empty path")

        img_obj = Image.open(path)
        img_arr = np.array(img_obj)
        print(f"The shape of image is: {img_arr.shape}")
        return img_arr
    except PermissionError:
        print(f"[ERROR]: permission denied: '{path}'")
    except FileNotFoundError:
        print(f"[ERROR]: no such file or directory: '{path}'")
    except Exception as e:
        print(f"[ERROR]: {e}")