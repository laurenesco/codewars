hex_chars = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F',
}

def get_hex_char(decimal: int) -> str:
    """
    Converts a decimal input into a hexadecimal string and returns that string
    """
    
    # Round if the value is outside bounds
    if decimal > 255: 
        decimal = 255
    elif decimal <= 0:
        return "00"
        
    converted_chars = []    
    result = ''
    
    while decimal > 0:
        # Divide by 16 and grab remainder
        remainder = decimal % 16
        decimal //= 16
                        
        # Convert remainder to hex
        if remainder > 9:
            hex = hex_chars[remainder]
        elif len(converted_chars) == 0:
            hex = f"{remainder:02d}"
        else: 
            hex = remainder
                    
        # Add hex to result stack (need LIFO)
        converted_chars.append(str(hex))
                                                                       
    return ''.join(reversed(converted_chars))
            

def rgb(r: int, g: int, b: int) -> str:
    """
    Returns hexadecimal code for a given RGB input
    """
    return get_hex_char(r) + get_hex_char(g) + get_hex_char(b)
    
    
