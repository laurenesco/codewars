# https://www.codewars.com/kata/5263c6999e0f40dee200059d

# unfinished

POSSIBLE_NUMS = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '5', '3'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9'],
    '0': ['0', '8'],
}
def get_pins(observed: str):

    possible_codes = []
    permute(observed, 0, possible_codes)
    
    return possible_codes

def permute(observed: str, idx: int, possible_codes: list[str]) -> list[str]:

    # Base case: No more digits to permute
    if idx == len(observed):
        return set(possible_codes)

    # Recursive case: Permute the current digit
    permute(observed, idx + 1, possible_codes)
    
    # Recursive logic
    for adjacent in POSSIBLE_NUMS[observed[idx]]:
        permuted_code = observed.copy()
        permuted_code[idx] = adjacent
        
        # Recurse for each sub digit
        permute(permuted, idx+1, possible_codes)
        
