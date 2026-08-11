# https://www.codewars.com/kata/52eb114b2d55f0e69800078d

class Cipher:
    def __init__(self, map1: str, map2: str) -> None:
        """
        Initializes Cipher object used to encode and decode text.
        
        Instance variables:
          - encryption_key: Map used to encrypt text
          - decryption_key: Map used to decrypt text
        
        Params:
          - map1: English alphabet
          - map2: Cipher key
        
        Assumptions:
          - map1 and map2 are the same length
        """
        
        if len(map1) != len(map2):
            raise ValueError("map1 and map2 must be the same length")
        
        self.encryption_key = dict(zip(map1, map2))
        self.decryption_key = dict(zip(map2, map1))

    def encode(self, phrase: str) -> str:
                    
        return ''.join(self.encryption_key.get(char, char) for char in phrase)

    def decode(self, phrase: str) -> str:
                
        return ''.join(self.decryption_key.get(char, char) for char in phrase)
