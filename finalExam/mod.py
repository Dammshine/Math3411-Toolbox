# Number Mod is easy but polynomial is bit harder
# try to do it here

def modPolynomialHelper(inputPoly: list[int], modPoly: list[int], currPolynomial: list[int]) -> list[int]:
    #print(inputPoly)
    # We would want to apply euclidean algorithm recursively
    highestIdx = 0
    for i in range(len(inputPoly)):
        if inputPoly[i] != 0:
            highestIdx = i
    
    # Base case   
    if (highestIdx + 1) < len(modPoly):
        return inputPoly
    
    # Otherwise, we use highestIdx to match
    digit = inputPoly[highestIdx] / modPoly[len(modPoly) - 1]
    currPolynomial.append([digit, highestIdx + 1 - len(modPoly)])

    # Deduct from inputPoly
    for i in range(len(modPoly)):
        inputPoly[highestIdx - i] -= digit
    
    return modPolynomialHelper(inputPoly, modPoly, currPolynomial)

def convertArr(arr: list[int]):
    # Truncate from back
    while len(arr) > 0 and arr[-1] == 0:
        arr.pop()
    
    finalS = ""
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            continue
        
        finalS += f"{arr[i]} "
        if i != 0:
            if i == 1:
                finalS += f"* x "
            else:
                finalS += f"* x^{i} "
        
        finalS += "+ "
    finalS = finalS[:-3]
    return finalS

def convertToArr(curr: list[int], n : int):
    newArr = []
    for i in range(n):
        newArr.append(0)
    
    for i in curr:
        newArr[i[1]] = i[0]
    
    return newArr

def modPolynomial(inputPoly: list[int], modPoly: list[int], zField = None) -> list[int]:
    copyInput = inputPoly[:]
    curr = []
    remainder = modPolynomialHelper(inputPoly, modPoly, curr)

    if zField == None:
        pass
    else:
        # For remainder
        for i in range(len(remainder)):
            remainder[i] += zField * 10000
            remainder[i] %= zField

    print(f"poly :{convertArr(copyInput)} = ({convertArr(convertToArr(curr, len(inputPoly)))}) * ({convertArr(modPoly)}) + ({convertArr(inputPoly)})")

modPolynomial([1,2,1], [2,1], zField=3)
    