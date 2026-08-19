# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n: int) -> int :
    
    num = list(str(n))
    solution = -1
    options = 0
    
    if len(num) < 2:
        return solution
    
    for r_ptr in range( len(num)-1 , -1, -1):
        
        l_ptr = r_ptr - 1
        
        while l_ptr < r_ptr:
            candidate = num
            tmp = candidate[l_ptr]
            candidate[l_ptr] = candidate[r_ptr]
            candidate[r_ptr] = tmp
            candidate = int( ''.join(candidate))
            
            print(f'candidate: {candidate}, n {n}')
            
            if candidate > n and (candidate < solution and options > 0 or options == 0):
                print('setting solution')
                solution = candidate
                options += 1
                
            r_ptr =- 1
            
    return solution
