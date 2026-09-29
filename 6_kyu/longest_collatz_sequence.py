# https://www.codewars.com/kata/57acc8c3e298a7ae4e0007e3

def longest_collatz(arr: list[int]) -> int:
    """
    Performs Collatz conjecture on each value in array, tracking
    how many operations each takes. 
    
    Returns the value with the longest Collatz sequence. Uses first value in
    the case of a tie.
    """
    if len(arr) == 0:
        raise ValueError("Empty array not permitted.")
    
    max_length = 0
    result = None
    
    for candidate in arr:
        length = collatzify(candidate)
        
        if length > max_length:
            max_length = length
            result = candidate
    
    return result

    """ Alternatively, """
    # return max(arr, key=collatzify)

def collatzify(value: int) -> int:
    """
    Perform Collatz conjecture, and track how many operations it takes. 
    
    Returns the integer value of operations required.
    """
    if value <= 0:
        raise ValueError("Collatz conjecture requires positive, non-zero integers.")
    
    operations = 0
    
    while value != 1:
        if value % 2 == 0:
            value //= 2
        else:
            value = 3 * value + 1
            
        operations += 1
        
    return operations
