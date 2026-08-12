# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import heapq

WHITELIST = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'")

def top_3_words(text: str) -> list[str]:
    word_count = {}
    current_word = ''
    
    for char in text.lower():
        # If the character is not whitelisted
        if char not in WHITELIST and current_word not in ['']:
            # Increment count for current word and reset it - ignore if only ' or whitespace
            if current_word != ' ':
                word_count[current_word] = word_count.get(current_word, 0) + 1
            current_word = ''
        elif char in WHITELIST:
            # Ootherwise append to current word
            current_word += char
            
    most_common_words = heapq.nlargest(3, word_count, key=word_count.get)
    print(word_count)
    print(most_common_words)
    
    return most_common_words
