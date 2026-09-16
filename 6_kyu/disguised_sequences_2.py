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

"""
  n   p       v(n,p)       u(n,p)
----------------------------------
**********************************
  1   1            3            2
  1   2            6            4
  1   3            9            6
  1   4           12            8
**********************************
  2   1            5            3
  2   2           10            6
  2   3           15            9
  2   4           20           12
**********************************
  3   1            7            4
  3   2           14            8
  3   3           21           12
  3   4           28           16
**********************************
  4   1            9            5
  4   2           18           10
  4   3           27           15
  4   4           36           20
**********************************
  5   1           11            6
  5   2           22           12
  5   3           33           18
  5   4           44           24
**********************************
  6   1           13            7
  6   2           26           14
  6   3           39           21
  6   4           52           28
**********************************
  7   1           15            8
  7   2           30           16
  7   3           45           24
  7   4           60           32
"""
