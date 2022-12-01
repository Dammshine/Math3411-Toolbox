

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True    


class RSA():
    n = None
    p = None
    q = None
    phi = None
    publicKey = None
    decodeKey = None
    k = None

    def __init__(self, p, q, exponent):
        # Check if p and q are prime
        if not isprime(p) or not isprime(q):
            return Exception("Not prime")

        # Find n
        self.n = p * q
        self.p = p
        self.q = q
        self.publicKey = exponent
        self.phi = (p - 1) * (q - 1)

        # Use euclidean to find a primary element
        for i in range(1, exponent):
            if i * exponent % self.phi == 1:
                self.decodeKey = i
        
    def encode(self, num):
        return num ** self.publicKey % self.n
    
    def decode(self, num):
        return num ** self.decodeKey % self.n


