# https://www.codewars.com/kata/586a933fc66d187b6e00031a

import numpy as np

CANDIDATES = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def generateName():
    """
    Creates a unique random string for image file name
    """
    
    # Create file name using numpy random function
    file_name = ''.join(np.random.choice(CANDIDATES, size = 6))
    
    # Ensure file name is unique
    while photoManager.nameExists(file_name):
        file_name = ''.join(np.random.choice(CANDIDATES, size = 6))
        
    return file_name
    
