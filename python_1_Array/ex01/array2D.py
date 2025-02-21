import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''slice a 2D array with given start and end'''
    try:
        if not isinstance(family, list):
            raise AssertionError("Input must be a list")
        if not family:
            raise AssertionError("empty list")
        if not all(isinstance(row, list) for row in family):
            raise AssertionError("All elements must be lists")
        if not all(len(row) == len(family[0]) for row in family):
            raise AssertionError("All rows must have same length")
        arr = np.array(family)
        if arr.ndim != 2:
            raise ValueError("Input must be 2D array")
        print(f"My shape is : {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError as e:
        print(f"Error: Cannot convert to 2D array - {str(e)}")
    except Exception as e:
        print("Unexpected Error:", e)
    return None
