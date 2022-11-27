import math


def pseudoPrime(test, base):
    if math.gcd(test, base) != 1:
        print((test ** (base - 1)) % base)
        return False
    
    if int((test ** (base - 1)) % base) != 1:
        print((test ** (base - 1)) % base)
        return False
    return True



def lucasPrime(test, base):
    def is_prime(n):
        """"pre-condition: n is a nonnegative integer
        post-condition: return True if n is prime and False otherwise."""
        if n < 2: 
            return False;
        if n % 2 == 0:             
            return n == 2  # return False
        k = 3
        while k*k <= n:
            if n % k == 0:
                return False
            k += 2
        return True
    
    if math.gcd(test, base) != 1:
        return False
    
    if int(base ** (test - 1) % test) != 1:
        return False
    
    for i in range(test):
        if is_prime(i) and float((test - 1) // i) == (test - 1) / i:
            if int(base ** ((test - 1) / i) % test) != 1:
                return True
    return False

#lucasPrime(1,2)