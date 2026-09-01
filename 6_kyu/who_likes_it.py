# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names: list[str]) -> str:
    """
    Returns a social media style string representation of 
    who 'likes' something.
    """
  
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"            
        case _:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this" 
