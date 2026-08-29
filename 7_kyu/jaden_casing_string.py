# https://www.codewars.com/kata/5390bac347d09b7da40006f6

# Key insight: Strings are not mutable in python

import string

def to_jaden_case(input: str) -> str:
    words = [_ for _ in input.split(" ")]
    jaden_cased = []

    for word in words:
        jaden_cased.append(word[0].upper() + word[1:len(word)].lower())
    
    return " ".join(jaden_cased)
    
#     return string.capwords(input, " ") # This also works :)
