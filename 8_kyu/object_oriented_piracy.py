# https://www.codewars.com/kata/54fe05c4762e2e3047000add

class Ship:
    CREW_WEIGHT = 1.5
    
    def __init__(self, draft: int, crew: int):
        """
        Initialize Ship object
        
        Params:
          - draft: weight of the ship
          - crew:  number of crew on the ship
        """
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self) -> bool:
        """
        Detemines if the ship is worth looting!
        
        Each crew member weights 1.5 units, stored as named constant
        
        Returns True if the draft minus the weight of the crew is > 20, False otherwise
        """
        
        return self.draft - self.CREW_WEIGHT * self.crew > 20
