# https://www.codewars.com/kata/58b3c2bd917a5caec0000017

def sum_groups(arr: list[int]) -> int:
    new_array = []
    idx = 0
    
    print(*arr) 

    while True:
        
        # Walk the array
        while idx < len(arr) - 1:
            sum = arr[idx]
            
            print("\n\n")
            
            print(f"current value: {arr[idx]}")

            # If i and i+1 are both even/odd
            while (arr[idx] + arr[idx + 1]) % 2 == 0 and idx < len(arr)-2:

                # add i+1 to sum and increment index
                sum += arr[idx + 1]
                idx += 1

            # Add sum to new array
            new_array.append(sum)
            print(f"Appending {sum} to new array")
            idx += 1
            
        if len(arr) == len(new_array):
            return len(new_array)
        
        arr = new_array
        idx = 0
