# https://www.codewars.com/kata/58409435258e102ae900030f

def parity_bit(binary: str) -> str:
    """
    Performs error detection on an input string of bytes.
    
    Outputs a string of the supplied bytes, with "error" replacing 
    bytes where an error was detected.
    """
    bytes_list = binary.split()
    error_bytes = []
    
    # Check each byte
    for idx, byte in enumerate(bytes_list):
        one_bits = 0
        p_bit = byte[-1]
        
        # Count one bits
        for bit in range(len(byte) - 1):
            if byte[bit] == '1':
                one_bits += 1
            
        # Error detected
        if (one_bits + (p_bit == '1')) % 2 != 0:
            error_bytes.append(idx)

    for error in error_bytes:
        bytes_list[error] = "error"        
        
    return ' '.join(byte[0:7] for byte in bytes_list)
    
