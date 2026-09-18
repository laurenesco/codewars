# https://www.codewars.com/kata/54c2fc0552791928c9000517

# import numpy as np
import math

def f(n: int, m: int) -> int:
    final_sum = 0
    
    """ Investigation for closed form solution """
    # print (f"{'i':>10} | {'n':>10} | {'m':>10} | {'i % m':>10}")
    # print("-" * 53)
    
    # for i in range (1, n + 1):
    #     final_sum += i % m
    #     print(f"{i:10d} | {n:10d} | {m:10d} | {i % m:10d}")
            
    """ Attempt 1 """
    # for i in range (1, n + 1):
    #     final_sum += i % m
        
    """ Attempt 2 """
    # candidate = 1
                
    # for i in range (1, n + 1):
    #     final_sum += candidate
    #     candidate += 1
        
    #     if candidate == m:
    #         candidate = 0
        
    """ Attempt 3 """
    # reciprocal = 1/m
    
    # for i in range (1, n + 1):
    #     final_sum += i * reciprocal
    
    """ Attempt 4 """
    # vector = np.array([i for i in range(1, n + 1)])
    # return np.sum(vector % m)
    
    """ Attempt 5 """
    sums = n // m
    remainder = n % m
            
    # Calculate sum once
    for i in range (1, m + 1):
        final_sum += i % m
                
    # Multiply by times we will get this sum
    final_sum *= sums
        
    # Add on leftover using triangular number formula
    final_sum += remainder * (remainder + 1) // 2
    
    """ Attempt 6 """
                
    return final_sum
