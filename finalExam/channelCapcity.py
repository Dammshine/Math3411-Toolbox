from channel import Channel


# Brute force
# Only can be used for binary channel
def channelCapacity(probsForIndi, precision=6):
    localMax = -1
    localProb = None
    for i in range(10 ** precision):
        prob = [i * (0.1 ** precision), (10 ** precision - i) * (0.1 ** precision)]

        tempChan = Channel(prob, probsForIndi)
        if tempChan.calculate_mutual_entropy() > localMax:
            localMax = tempChan.calculate_mutual_entropy()
            localProb = prob[:]
    
    return [localProb, localMax]

#print(channelCapacity([[2/3, 1/3], [1/10, 9/10]]))