# https://www.codewars.com/kata/56fe17fcc25bf3e19a000292

import math

def v1(n: int, p: int):
    # Keeping a longer illustrative solution for v1 to look back on
    
    result = 0;
    for k in range(n + 1):
        term1 = (-1) ** k
        term2 = p
        term3 = 4 ** (n - k)
        term4 = math.factorial(2*n - k) // (math.factorial(k) * math.factorial((2*n - k) - k))
        # term4 = math.comb(2*n - k, k) # Both of these solutions work for term4
        
        result += term1 * term2 * term3 * term4
        
    return result
    
def u1(n: int, p: int):
    return sum((-1)**k * p * 4**(n-k) * math.comb(2*n-k+1, k) for k in range(n + 1))
    
def v_eff(n: int, p: int):
    return (n + (n + 1)) * p
    
def u_eff(n: int, p: int):
    return (n + 1) * p
