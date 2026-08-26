# https://www.codewars.com/kata/6925ba5fcee28ebed6e18e7d

import math

def entropy(message: str) -> float:
    """
    Returns the entropy of a message, where entropy is defined as:
    
       H = - \sum p_I * log_2(p_i)
       
    where p is the probability of a symbol, defined as:
    
       p_i = count(p_i) / len(message)
       
    Note: Spaces are not considered informative symbols
    """
    
    symbols = {}
    H = 0.0
    message = message.replace(" ", "")
    
    # Get count for each unique symbol
    for symbol in message:
        symbols[symbol] = symbols.get(symbol, 0) + 1
                        
    # Calculate entropy using probability formula
    for symbol, value in symbols.items():
        probability = value / len(message)
        H += probability * math.log2(probability)
        
    return -(H)
