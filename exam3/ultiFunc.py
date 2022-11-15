import math
from sympy import Q, ask

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

"""
Calculating invertible units
"""
def get_inver_units(m: int) -> int:
    # Is invertible if gcd(a, m) != 1
    count = []
    for i in range(2, m):
        if math.gcd(i, m) == 1:
            count += [i]
    return count

"""
Calculating invertible units
"""
def calculate_inver_units(m: int) -> int:
    # Is invertible if gcd(a, m) != 1
    return len(get_inver_units(m))

"""
Apply euler's theorem to solve 
5^77 mod 77 
"""
def find_mod(base : int, power : int, mod : int):
    # Altenrtaively I can just do it
    return (base ** power) % mod

"""
Find the order of an element
"""
def find_order(num : int, base: int) -> int:
    if num > base: 
        return None
    
    for i in range(1, base):
        if num ** i % base == 1:
            return i

    return None

"""

"""
def find_factor_fermet(num: int)-> list[int]:
    lowerBound = math.ceil(math.sqrt(num))
    for t in range(lowerBound, num - 1):
        s = t ** 2 - num
        if math.isqrt(s) ** 2 == s:
            return [t - math.isqrt(s), t + math.isqrt(s)]
    return 

print(find_factor_fermet(78793))
