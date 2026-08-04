# https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
    
    NUMERALS = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }
    
    @staticmethod
    def to_roman(val : int) -> str:
        
        return ''

    @staticmethod
    def from_roman(roman_num : str) -> int:
        
        roman = [c for c in roman_num]
        result = 0
        idx = 0
                
        while idx < len(roman):
            # Handle compound calculation case
            if idx < len(roman) - 1:
                if (
                   roman[idx] == 'C' and roman[idx + 1] in ['M', 'D']
                or roman[idx] == 'X' and roman[idx + 1] in ['C', 'L']
                or roman[idx] == 'I' and roman[idx + 1] in ['X', 'V']
                ):
                    # Compute result
                    result += (RomanNumerals.NUMERALS[roman[idx + 1]] - RomanNumerals.NUMERALS[roman[idx]]) 
                    
                    # Account for next iteration and next step
                    idx += 1
                    result -= RomanNumerals.NUMERALS[roman[idx]]
                                            
            # Handle normal case
            result += RomanNumerals.NUMERALS[roman[idx]]
            idx += 1
                           
        return result
