# 8 kyu
# https://www.codewars.com/kata/55d277882e139d0b6000005d

import numpy as np

def find_average(nums: list[int]) -> int:
    # Method 1
#     return np.mean(nums)

    # Method 2
    # return np.sum(nums) / len(nums)

    # Method 3
    total = 0
    for number in nums:
        total += number
        
    return total / len(nums)
