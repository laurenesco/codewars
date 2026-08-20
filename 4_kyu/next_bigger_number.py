# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n: int) -> int :
    
    n = list(str(n))
    solution = -1
    
    if len(n) < 2:
        return solution
    
    r_ptr = len(n) - 1
    l_ptr = r_ptr - 1
    
    while l_ptr >= 0:
        if n[l_ptr] < n[r_ptr]:
            tmp = n[r_ptr]
            n[r_ptr] = n[l_ptr]
            n[l_ptr] = tmp
            
        break
        
    print(f'l_ptr: {l_ptr}, n: {n}')
        
    prefix = [n[_] for _ in range(l_ptr)]
    sorted = [n[_] for _ in range(l_ptr, len(n))].sort()
    
    solution = str(prefix) + str(sorted)

    
    return solution
