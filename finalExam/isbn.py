import math

def isbnCheck(s : str):
    if len(s) != 10:
        return None
    
    # Check
    sum = 0
    for i in range(len(s)):
        sum += (i + 1) * int(s[i] if s[i] != 'X' else "10")
    
    return sum % 11 == 0


# print(isbnCheck("0909117064"))

