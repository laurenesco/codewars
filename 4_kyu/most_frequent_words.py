# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import heapq

WHITELIST = set("abcdefghijklmnopqrstuvwxyz'")

def top_3_words(text: str) -> list[str]:
    """
    Takes a block of text and returns the 3 most common words.
    
    Assumptions per problem spec:
     - A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
     - Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
     - Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
     - Matches should be case-insensitive, and the words in the result should be lowercased.
     - Ties may be broken arbitrarily.
     - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

    """
    word_count = {}
    current_word = ''
    
    for char in text.lower():
        
        # If the character is not whitelisted, pop word
        if char not in WHITELIST and len(current_word) > 0:
            
            word_count[current_word] = word_count.get(current_word, 0) + 1
            current_word = ''
            
        # Else if in whitelist append to current word
        elif char in WHITELIST:
            current_word += char
            
    # Get the last word
    if len(current_word) > 0:
        word_count[current_word] = word_count.get(current_word, 0) + 1
        
    # Eliminate words that are only apostraphes per problem spec
    word_count = {w: c for w, c in word_count.items() if w.strip("'")}
    
    return heapq.nlargest(3, word_count, key=word_count.get)
