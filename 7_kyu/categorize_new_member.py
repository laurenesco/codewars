# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data: list[tuple[int, int]]) -> list[str]:
    """
    Accepts a list of candidate's age and handicap. If the candidate's age is 
    at least 55, and their handicap is greater than 7, they will be in the
    senior category. Otherwise, they will be in the Open category.

    Both are working solutions.
    """
    
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]
    
    # categories = []
    
    # for age, handicap in data:
    #     if age >= 55 and handicap > 7:
    #         categories.append("Senior")
    #     else:
    #         categories.append("Open")
    
    # return categories
