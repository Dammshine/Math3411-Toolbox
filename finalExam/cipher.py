# Use Caesar cipher
def caesarCipher(s : str, pos : str):
    posShift = ord(pos) - ord('a')
    newS = ""
    for i in s:
        newC = ord(i) + posShift
        if newC > ord('z'):
            newC -= 26
        
        newS += chr(newC)
    return newS

"""
    Decipher  a code uses Caesar
"""
def caesarDecipher(s : str, pos : str):
    posShift = ord(pos) - ord('a')
    newS = ""
    for i in s:
        newC = ord(i) - posShift
        if newC < ord('a'):
            newC += 26
        
        newS += chr(newC)
    return newS

"""
    Periodic polyalphabetic substitution
"""
def caesarPeriodCipher(s : str, key : str):
    newS = ""
    for i in range(len(s)):
        newS += caesarCipher(s[i], key[i % len(key)])
    return newS

"""
    Periodic polyalphabetic substitution
"""
def caesarPeriodDecipher(s : str, key : str):
    newS = ""
    for i in range(len(s)):
        newS += caesarDecipher(s[i], key[i % len(key)])
    return newS

"""
    Non periodic polyalphabetic substitution
"""
def nPplainText(s : str, key : str):
    newS = ""
    for i in range(len(key)):
        newS += caesarCipher(s[i], key[i % len(key)])
    for i in range(len(key), len(s)):
        newS += caesarCipher(s[i], s[i - len(key)])
    return newS

def nPplainTextDecipher(s : str, key : str):
    newS = ""
    for i in range(len(key)):
        newS += caesarDecipher(s[i], key[i % len(key)])

    for i in range(len(key), len(s)):
        newS += caesarDecipher(s[i], newS[i - len(key)])
    return newS

def nPcipherText(s : str, key : str):
    newS = ""
    for i in range(len(key)):
        newS += caesarCipher(s[i], key[i % len(key)])
    for i in range(len(key), len(s)):
        newS += caesarCipher(s[i], newS[i - len(key)])
    return newS

def nPcipherTextDecipher(s : str, key : str):
    newS = ""
    for i in range(len(key)):
        newS += caesarDecipher(s[i], key[i % len(key)])

    for i in range(len(key), len(s)):
        newS += caesarDecipher(s[i], s[i - len(key)])
    return newS

# Try brute force
def bruteDipher(s : str, l : int):
    newS = ""
    keys = "abcdefghijklmnopqrstuvwxyz"
    for i in keys:
        for j in keys:
            newS += (i + " " + j + ": ")

            newS += caesarPeriodDecipher(s, i + j)
            newS += "\n"
    return newS


#print(bruteDipher("kmhz", 2))