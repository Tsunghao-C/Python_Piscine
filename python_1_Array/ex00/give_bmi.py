import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''retrun a list of BMIs'''
    if not height or not weight:
        raise ValueError("Error: Empty input")
    if not all(isinstance(elem, int | float) for elem in height):
        raise ValueError("Error: Not all elements in height are int or float")
    if not all(isinstance(elem, int | float) for elem in weight):
        raise ValueError("Error: Not all elements in weight are int or float")
    for x in height:
        if x == 0:
            raise ValueError("Error: zero height")
    np_height = np.array(height, dtype=float)
    np_weight = np.array(weight, dtype=float)
    if np_weight.size != np_height.size:
        raise ValueError("Error: input length not aligned!")
    np_bmi = np_weight / (np_height ** 2)

    return np_bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''return a list of Bool showing if a BMI is over limit'''
    output = [x > limit for x in bmi]
    return output
