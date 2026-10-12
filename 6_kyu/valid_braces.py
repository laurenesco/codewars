# https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def valid_braces(string: str) -> bool:
    """
    Returns True or False depending on if the supplied
    string of paretheses, square brackets, and curly braces
    are in a valid open/close pattern.
    """
    
    if not string:
        raise ValueError('Provided string is empty!')
    
    opening_braces = []
    
    for brace in string:
        if brace in ['(', '[', '{']:
            opening_braces.append(brace)
        else:
            if not opening_braces:
                return False
            
            o_brace = opening_braces.pop()
            
            match brace:
                case ')':
                    if o_brace != '(': return False
                case '}':
                    if o_brace != '{': return False
                case ']':
                    if o_brace != '[': return False
                case _:
                    raise ValueError('Unknown value in braces: ' + brace)
    
    return not opening_braces
