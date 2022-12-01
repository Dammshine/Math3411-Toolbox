import numpy as np
import sympy


def checkLinearDepend(matrix):
    # https://stackoverflow.com/questions/64237996/how-to-determine-two-vectors-are-linearly-dependent-or-independent-in-python
    _, indexes = sympy.Matrix(matrix).T.rref()  # T is for transpose
    # print(indexes)

    if len(indexes) == 2:
        return True
    else:
        return False

def pickNfromMatrixHelper(matrix, i, curr, takes):
    if i == 0:
        # print(curr)
        checkDup = curr[:]
        checkDup.sort()
        if tuple(checkDup) in takes:
            return
        
        takes[tuple(checkDup)] = True
        return
    
    for idx in range(len(matrix)):
        if curr.count(idx) != 0:
            continue
        
        curr.append(idx)
        pickNfromMatrixHelper(matrix, i - 1, curr, takes)
        curr.pop()

    return

def pickNfromMatrix(matrix, i):
    takes = {}
    curr = []
    pickNfromMatrixHelper(matrix, i, curr, takes)
    
    retList = []
    for choice in takes:
        localMatrix = []
        for i in choice:
            localMatrix.append(matrix[i])
        retList.append(localMatrix)

    

    return retList

"""
Check the minimum distance for linear code in matrix
"""
def minDistance(matrix):
    # Return the minimum distance
    # Start from 2 and test
    n = np.matrix(matrix)

    # Check from 2
    for i in range(2, len(matrix) + 1):
        query = pickNfromMatrix(matrix, i)
        for q in query:
            if checkLinearDepend(q) == False:
                return i
    
    return -1


#print(minDistance([[1, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1], [0, 1, 1]]))