import math

def calculate_entropyDup(prob : list[float], radix: int) -> float:
    sum = 0
    for x in prob:
        if x == 0:
            continue
        sum += (x) * math.log(1 / x, radix)
    return sum

class Channel():
    probs = None
    probsForIndi = None
    probOutput = None

    def __init__(self, probs, probsForIndi):
        probOutput = []
        for i in range(len(probsForIndi[0])):
            probOutput.append(0)
        
        for i in range(len(probsForIndi)):
            for j in range(len(probsForIndi[i])):
                probOutput[j] += probs[i] * probsForIndi[i][j]
        
        self.probs = probs
        self.probsForIndi = probsForIndi
        self.probOutput = probOutput
    
    # We want a few different thing
    def sourceEntropy(self):
        return calculate_entropyDup(self.probs, len(self.probs))

    def outputEntropy(self):
        return calculate_entropyDup(self.probOutput, len(self.probs))
    
    def conditionalEntropy(self, inputIdx=None, outPutIdx=None):
        if inputIdx == None and outPutIdx == None:
            return Exception("Have to specify at least one condition")
        
        if inputIdx != None:
            return calculate_entropyDup(self.probsForIndi[inputIdx], len(self.probs))
        else:
            arr = []
            # Need to use baye's rule
            #print(self.probsForIndi)
            for i in range(len(self.probsForIndi)):
                # print(self.probsForIndi[i][outPutIdx], self.probs[i])
                arr.append(self.probsForIndi[i][outPutIdx] * self.probs[i] / self.probOutput[outPutIdx])
            
            #print(arr)
            return calculate_entropyDup(arr, len(self.probs))      

    def calculate_A_to_B_entropy(self):
        sum = 0
        for i in range(len(self.probs)):
            sum += self.probs[i] * self.conditionalEntropy(inputIdx=i)
        return sum

    def calculate_B_to_A_entropy(self):
        sum = 0
        for i in range(len(self.probOutput)):
            sum += self.probOutput[i] * self.conditionalEntropy(outPutIdx=i)
        return sum

    def calculate_mutual_entropy(self):
        return self.outputEntropy() - self.calculate_A_to_B_entropy()

    def calculate_joint_entropy(self):    
        return self.sourceEntropy() + self.calculate_A_to_B_entropy()
          
        