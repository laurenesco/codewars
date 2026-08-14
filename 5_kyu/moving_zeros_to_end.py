# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(numbers: list[int]) -> list[int]:
    """
    Takes an array of mixed integers and moves all 0's in place to the back
    
    Params:
      - numbers: an array of integers
      
    Returns:
      - numbers: the same array with 0's shifted back
    """
    
    idx_non_zero = 0
    
    for num in numbers:
        
        if num != 0:
            numbers[idx_non_zero] = num
            idx_non_zero += 1

            
    for idx in range(idx_non_zero, len(numbers)):
        numbers[idx] = 0
    
    return numbers
