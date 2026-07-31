# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str) -> None:
        self.alphabet = set(alphabet)   
        self.key = key
        self.createDisplacementDict(key)
    
    def encode(self, text: str) -> str:
        """Takes a plaintext string and returns encoded version"""
                
        key_ptr = 0
        result = ""
            
        # Iterate over the string characters and create result
        for c in text:
                    
            # Only convert letters in alphabet, per spec
            if c in self.alphabet:
                shift = self.displacements[self.key[key_ptr]]
                
                # Wrap the shift, if necessary
                if ord(c) + shift > ord('a') + 25:
                    shift -= 26
                                    
                # c = ASCII value of c + how far key_ptr char is from a
                result += chr(ord(c) + shift)

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
                shift = self.displacements[self.key[key_ptr]]
                
                # Wrap the shift, if necessary
                if ord(c) - shift < ord('a'):
                    shift -= 26
                                                        
                # c = ASCII value of c + how far key_ptr char is from a
                result += chr(ord(c) - shift)
                
            else:
                result += c
                
            # Increment the key pointer
            if key_ptr == len(self.key) - 1:
                key_ptr = 0
            else: 
                key_ptr += 1
            
        return result
    
    def createDisplacementDict(self, key: str) -> None:
        """Create dict to store shift values for O(1) lookup later"""
        self.displacements = {}
        
        for c in self.key:
            
            shift = (ord(c.lower()) - ord('a'))
            self.displacements[c] = shift
