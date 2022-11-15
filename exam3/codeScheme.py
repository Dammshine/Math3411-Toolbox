from ultiFunc import calculate_len_from_fano
import pprint
pp = pprint.PrettyPrinter(indent=4)

class CodeScheme():
    _probs = None
    _radix = None

    def __init__(self, probs, radix):
        self._probs = probs
        self._radix = radix
        pass
    
    """
    The base component interface defines operation can be altered by decorator
    """
    def generateCodeScheme():
        pass

class HuffmanCodeScheme(CodeScheme):
    __scheme = None

    def __init__(self, probs, radix):
        super().__init__(probs, radix)
    
    def __doHuffman(self, huffman):
        # Create a new joint entry
        newEntry = {"prob": 0.0, "idx": list()}
        for i, entry in enumerate(huffman[-self._radix:]):
            newEntry["prob"] += entry["prob"]
            newEntry["idx"] += entry["idx"]
            # Add to the codeword
            for index in entry["idx"]:
                self.__scheme[index]["codeword"] = str(i) + self.__scheme[index]["codeword"]
        
        # Remove the entris combined and insert new entry
        huffman = huffman[:(-self._radix)]
        huffman.insert(0, newEntry)
        huffman.sort(key=lambda d: d["prob"], reverse=True)

        return huffman


    def __processCode__(self):
        if self.__scheme != None:
            return self.__scheme
        
        # Applie huffman algorithm
        # Load __scheme with probability, and it's code
        self.__scheme = []
        for idx in range(len(self._probs)):
            self.__scheme.append({"prob": self._probs[idx], "codeword": str(), "var": f"s{idx + 1}", "idx": idx})
        
        # Load Huffman
        huffman = []
        for idx in range(len(self._probs)):
            huffman.append({"prob": self._probs[idx], "idx": [idx]})
        
        # Add Dummy Variable to the __scheme
        while len(huffman) % (self._radix - 1) != 1:
            if (self._radix == 2):
                break
            huffman.append({"prob": self._probs[idx], "idx": list()})
        huffman.sort(key=lambda d: d["prob"], reverse=True)

        # Apply huffman algorithm
        while len(huffman) != 1:
            
            huffman = self.__doHuffman(huffman)
        
        return self.__scheme

    """
    Huffman coding scheme
    """
    def generateCodeScheme(self):
        return self.__processCode__(self)

class ShannonFano(CodeScheme):
    __scheme = None

    def __init__(self, probs, radix):
        super().__init__(probs, radix)
    
    def __insertCode(self, length, code, currStr):
        # If this reaches dead end
        if currStr in code:
            return None
        if length == 0 and currStr not in code:
            code[currStr] = True
            return currStr
        
        
        # Try every radix
        for i in range(self._radix):
            checkRe = self.__insertCode(length - 1, code, currStr + str(i))
            if checkRe != None:
                return checkRe
        
        return None

    def __processCode__(self):
        if self.__scheme != None:
            return self.__scheme

        self.__scheme = []
        fanoLen = []
        for idx in range(len(self._probs)):
            self.__scheme.append({"prob": self._probs[idx], "codeword": str(), "var": f"s{idx + 1}", "idx": idx})
            fanoLen.append({"len": calculate_len_from_fano(self._probs[idx], self._radix)})
        
        # Then sort scheme by prob
        self.__scheme.sort(key=lambda d: d["prob"], reverse=True)
        
        # Then find the length for individual code and insert it
        decisionTree = {}
        for idx in range(len(self.__scheme)):
            codeword = self.__insertCode(fanoLen[idx]["len"], decisionTree, "")
            self.__scheme[idx]["codeword"] = codeword
        return self.__scheme


    """
    ShannonFano
    """
    def generateCodeScheme(self):
        return self.__processCode__()



