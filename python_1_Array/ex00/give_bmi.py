import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''retrun a list of BMIs'''
    if not height or not weight:
        raise ValueError("Error: Bad input")
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
