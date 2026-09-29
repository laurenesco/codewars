# https://www.codewars.com/kata/56b3b27cadd4ad275500000c

LEGAL_CHARS = set("abcdefghijklmnopqrstuvwxyz")
ILLEGAL_WORDS = set("a", "the", "on", "at", "of", "upon", "in", "as")

def word_count(sentence: str) -> int:
    word_count = l_ptr = 0
    sentence = lower(sentence)
    
    while l_ptr < len(sentence) - 1:
        word = ""
        r_ptr = l_ptr + 1
        
        # If current character is valid, grab word
        if sentence[l_ptr] in LEGAL_CHARS:
            while sentence[r_ptr] in LEGAL_CHARS and r_ptr < len(sentence):
                r_ptr += 1
            

            
        # Verify word is legal and add to word count
        if word not in ILLEGAL_WORDS and len(word) > 0:
            word_count ++    
    
    
    return word_count
