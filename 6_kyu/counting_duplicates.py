# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text: str):
    unique_symbols = set()
    duplicates = set()
    
    for symbol in text:
        if symbol.upper() not in unique_symbols:
            unique_symbols.add(symbol.upper())
        else:
            duplicates.add(symbol.upper())
            
    return len(duplicates)
