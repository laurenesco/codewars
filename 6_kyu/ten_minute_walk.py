# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk: list[str]) -> bool:
    """
    Returns true if the provided walk is exactly 10 blocks
    and returns to the point of origin.
    """
    ns_position = 0
    we_position = 0

    for direction in walk:
        match direction:
            case 'n':
                ns_position += 1 
            case 's':
                ns_position -= 1 
            case 'w':
                we_position -= 1 
            case 'e':
                we_position += 1 
            case _:
                raise Exception("Unknown direction provided")
    
    return len(walk) == 10 and ns_position == 0 and we_position == 0
