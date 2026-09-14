# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n: list[int]) -> str:
    # Both working solutions that pass all test cases
    
    # return "(" + ''.join(map(str, n[:3])) + ") " + ''.join(map(str, n[3:6])) + "-" + ''.join(map(str, n[6:]))
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
