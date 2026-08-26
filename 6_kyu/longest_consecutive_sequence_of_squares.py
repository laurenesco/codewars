# https://www.codewars.com/kata/5aa69e68ba1bb5ecdf000557

def longest_sequence(target: int) -> list[int]:
    """
    Returns a list of consecutive numbers whose squares
    sum to the target.
    """
    solution = []
    total = 0
    candidate = 1    
    
    # Start with 1, progressively add squares until it equals or passes number    
    while total != target:
        total += candidate ** 2
        solution.append(candidate)
        candidate += 1
        
        # If it passes the number, start removing squares from the left and see if we can hit the number
        while total > target:
            removed = solution.pop(0)
            total -= removed ** 2
                        
        if len(solution) == 0:
            return solution

    return solution
