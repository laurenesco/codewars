# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

# In progress

def strip_comments(message: str, markers: list[str]) -> str:
    uncommented = []
    last_marker = 0
    comment_markers = set(markers)

    for idx in range(len(message)):
        if message[idx] in comment_markers:
            uncommented.append(message[last_marker:idx - 1])
            print(f"appending: {message[last_marker:idx - 1]}")
            last_marker = idx
            
            while message[idx] != "\n" and idx < len(message) - 1:
                idx += 1
                last_marker = idx
        
    
    return ''.join(uncommented)
    
