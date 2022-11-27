import math
from codeScheme import CodeScheme, HuffmanCodeScheme, ShannonFano
import re

"""
Given a code scheme, and encoding string, code it
"""
def getEncoding(code : CodeScheme, encodingString: str) -> str:
    # Parse encoding String s
    scheme = code.generateCodeScheme()
    encodingString = re.findall(r's\d+', encodingString)
    
    ret = ""
    for s in encodingString:
        for coding in scheme:
            if coding['var'] == s:
                ret += coding['codeword']
                break
    
    return ret

"""
Given a code scheme, and decoding string, decode it
"""
def getDecoding(code : CodeScheme, decoding: str) -> str:
    # Parse encoding String s
    if len(decoding) == 0:
        return ""
    
    # Parse encoding String s
    scheme = code.generateCodeScheme()
    for coding in scheme:
        codeword = coding['codeword']
        
        query = decoding.find(fr'{codeword}')
        if query == 0:
            recurSearch = getDecoding(code, decoding[len(codeword):])
            if recurSearch != None:
                return coding['var'] + recurSearch
    
    # Can't be handled
    return None

"""
Given a code scheme, print it scheme more gracefully?
"""
def printCode(code : CodeScheme) -> str:
    # Parse encoding String s
    scheme = code.generateCodeScheme()
    beauti = {}
    for coding in scheme:
        beauti[coding['var']] = coding['codeword']
    
    print(beauti)

"""
Given a code scheme, print it scheme with probability toomore gracefully?
"""
def printCodeWithProb(code : CodeScheme) -> str:
    # Parse encoding String s
    scheme = code.generateCodeScheme()
    beauti = {}
    for coding in scheme:
        beauti[coding['var']] = [coding['codeword'], coding['prob']]
    
    # Can't be handled
    print(beauti)