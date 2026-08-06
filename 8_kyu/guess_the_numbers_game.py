# https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

class NoMoreLives(Exception):
    """Exception for when the Guesser class is out of lives"""
    pass

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
                
        # If guess is incorrect and out of lives
        if self.lives <= 0:
            
            raise NoMoreLives("Omae wa mo shindeiru")
            
        # If the guess is correct
        elif self.number == n:
        
            return True
            
        # Otherwise
        else:
        
            self.lives -= 1       
            return False
