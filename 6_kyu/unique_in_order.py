# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(sequence) -> list[str]:
    return_list = []
    current_token = None
    
    for token in sequence:
        if not current_token or current_token != token:
            current_token = token
            return_list.append(token)
    
    return return_list
