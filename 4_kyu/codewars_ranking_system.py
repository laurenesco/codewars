# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

class User:    
    
    RANKS = {    
        -8: 1,    
        -7: 2,    
        -6: 3,    
        -5: 4,    
        -4: 5,    
        -3: 6,    
        -2: 7,    
        -1: 8,    
        1: 9,    
        2: 10,    
        3: 11,    
        4: 12,    
        5: 13,    
        6: 14,    
        7: 15,    
        8: 16    
    }    
        
    def __init__(self) -> None:    
        """    
        Initializes an instance of the User class. A User always    
        starts with rank -8 and 0 progress.    
        """    
        self.rank = -8    
        self.progress = 0    
            
    def inc_progress(self, activity_rank: int) -> None:    
        """    
        Applies progress to a User instance    
            
        Business rules:    
        - Any leftover progress after rank up is applied    
          toward next rank, no progress is lost    
        - A user ranks up when they reach 100 progress    
        - Completing an activity...    
          - the same rank as the User yields 3 points    
          - one rank lower than the User yields 1 point    
          - two levels or more lower than the User are ignored    
          - ranked higher than the User yields 10 * d * d where    
            d is the difference in ranking between the activity    
            and the User    
          - rank difference calculations ignore the 0 rank    
        """    
            
        if activity_rank not in self.RANKS:    
            raise ValueError("Valid ranks are -8 through 8, not including 0.")    
            
        # Calculate rank difference between user and activity    
        rank_diff = abs(self.RANKS[self.rank] - self.RANKS[activity_rank])    
        progress_gained = 0    
            
        # Calculate progress gained    
        if self.RANKS[activity_rank] > self.RANKS[self.rank]:    
            progress_gained = 10 * rank_diff * rank_diff    
        elif self.RANKS[activity_rank] == self.RANKS[self.rank]:    
            progress_gained = 3    
        elif self.RANKS[self.rank] - self.RANKS[activity_rank] == 1:    
            progress_gained = 1    
        else:    
            pass    
            
        # Rank up    
        while progress_gained > 0:    
            # Rank up if progress_gained + User progress >= 100    
            if progress_gained + self.progress >= 100:    
                self._rank_up()    
                progress_gained -= (100 - self.progress)    
                self.progress = 0    
            else:    
                self.progress += progress_gained    
                progress_gained = 0    
                    
                
        if self.rank == 8:    
            self.progress = 0    
                            
    def _rank_up(self) -> None:    
        """    
        Increments the rank attribute for a User instances    
            
        Business rules:    
        - Rank !> 8    
        - Rank !< -8    
        - Rank != 0    
        """    
        if self.rank != 8:    
            self.rank += 1    
                
        if self.rank == 0:    
            self.rank += 1
