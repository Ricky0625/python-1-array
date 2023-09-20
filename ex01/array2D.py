import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        if not isinstance(family, list):
            raise AssertionError('not a list')

        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError('start and end should be int')

        arr = np.array(family)

        if arr.ndim != 2:
            raise AssertionError('must be a 2D array')

        new_arr = arr[start:end]

        print(f"My shape is : {arr.shape}")
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()

    except ValueError:
        print("[ERROR]: Lists are not the same size")
    except Exception as e:
        print(f"[ERROR]: {e}")
