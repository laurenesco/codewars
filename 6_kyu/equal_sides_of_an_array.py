# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

import numpy as np

def find_even_index(arr: list[int]) -> int:
    """
    Return the index for which the sum of all elements left of the index
    and the sum of all elements right of the index is equal.
    
    Return -1 if no such index exists.
    """
    l_sum = 0
    r_sum = np.sum(arr[1:])
    balanced_ptr = -1
    
    candidate_ptr = 0
    
    while candidate_ptr < len(arr) - 1 and l_sum != r_sum:        
        candidate_ptr += 1
        l_sum += arr[candidate_ptr - 1]
        r_sum -= arr[candidate_ptr]
        
        if l_sum == r_sum:
            return candidate_ptr
    
    if l_sum == r_sum:
        balanced_ptr = candidate_ptr
    
    return balanced_ptr
        
