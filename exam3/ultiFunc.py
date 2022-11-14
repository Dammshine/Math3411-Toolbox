import math

def calculate_entropy(prob : list[float], radix: int) -> float:
    sum = 0
    for x in prob:
        sum += (x) * math.log(1 / x, radix)
    return sum

def calculate_len_from_fano(prob : float, radix: int) -> int:
    for i in range(1, 100):
        if (1 / radix ** i) < prob:
            return i
    return -1