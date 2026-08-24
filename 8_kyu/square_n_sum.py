# https://www.codewars.com/kata/515e271a311df0350d00000f

import numpy as np

def square_sum(numbers: list[int]) -> int:
    return np.sum(np.power(numbers, 2))
