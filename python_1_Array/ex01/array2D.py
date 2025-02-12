import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''slice a 2D array with given start and end'''
    if not isinstance(family, list):
        raise ValueError("Error: Input must be a list")
    if not family:
        raise ValueError("Error: empty list")
    if not all(isinstance(row, list) for row in family):
        raise ValueError("Error: All elements must be lists")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("Error: All rows must have same length")
    try:
        arr = np.array(family)
        if arr.ndim != 2:
            raise ValueError("Error: Input must be 2D array")
        print(f"My shape is : {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error: Cannot convert to 2D array - {str(e)}")
