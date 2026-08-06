# https://www.codewars.com/kata/528d36d7cc451cd7e4000339

def most_money(students: list[Student]) -> str:
    
    results = []
    max = 0
    
    for pupil in students:
        current_total = get_total(pupil)
                    
        # Compare to current max
        if current_total > max or not results:
            results.clear()
            results.append(pupil.name)
            max = current_total
        elif current_total == max:
            results.append(pupil.name)
    
    # Tie case
    if len(results) == len(students) and len(results) > 1:
        return "all"
    
    return ", ".join(results)
    
def get_total(pupil: Student) -> int:
    return (pupil.fives * 5) + (pupil.tens * 10) + (pupil.twenties * 20)
