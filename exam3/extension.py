from codeScheme import ShannonFano

class ExtensionShannonFano(ShannonFano): 
    ownDict = {}
    newProb = []
    shannon = None
    
    def processExtenion(self, probs, extension, currStr, currProb):
        if extension == 0:
            self.newProb.append(currProb)
            self.ownDict[f's{len(self.newProb)}'] = currStr
            return currStr

        for i in range(len(probs)):
            self.processExtenion(probs, extension - 1, currStr + f's{i + 1}', currProb * probs[i])

    def __init__(self, probs, radix, extension):
        # Process prob by extension
        self.processExtenion(probs, extension, "", 1)
        print(self.newProb)
        super().__init__(self.newProb, radix)
    
    """
    ShannonFano
    """
    def generateCodeScheme(self):
        scheme = super().generateCodeScheme()
        for i in range(len(scheme)):
            scheme[i]['var'] = self.ownDict[scheme[i]['var']]
        return scheme