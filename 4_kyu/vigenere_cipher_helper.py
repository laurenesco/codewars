# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str) -> None:
        self.alphabet = alphabet
        self.key = key
    
    def encode(self, text: str) -> str:
        """Takes a plaintext string and returns encoded version"""
                
        key_ptr = 0
        result = ""
            
        # Iterate over the string characters and create result
        for c in text:
                    
            # Only convert letters in alphabet, per spec
            if c in self.alphabet:
                shift = self.alphabet.index(self.key[key_ptr])
                
                # Wrap the shift, if necessary
                if self.alphabet.index(c) + shift > len(self.alphabet) - 1:
                    shift -= len(self.alphabet)
                                    
                # Shift c by key characters
                result += self.alphabet[self.alphabet.index(c) + shift]

            else:
                result += c
            
            # Increment the key pointer
            if key_ptr == len(self.key) - 1:
                key_ptr = 0
            else: 
                key_ptr += 1
            
        return result
        
    
    def decode(self, text: str) -> str:
        """Takes an encoded string and returns a plaintext version"""
        
        key_ptr = 0
        result = ""
                    
        # Iterate over the string characters and create result
        for c in text:
                    
            # Only convert letters in alphabet, per spec
            if c in self.alphabet:
                shift = self.alphabet.index(self.key[key_ptr])
                
                # Wrap the shift, if necessary
                if self.alphabet.index(c) - shift < 0:
                    shift -= len(self.alphabet)
                                                        
                # Undo the shift on c when decoding
                result += self.alphabet[self.alphabet.index(c) - shift]
                
            else:
                result += c
                
            # Increment the key pointer
            if key_ptr == len(self.key) - 1:
                key_ptr = 0
            else: 
                key_ptr += 1
            
        return result
