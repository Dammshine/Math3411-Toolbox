import math

a = int(input("What's the first number? "))
b = int(input("What's the second number? ")) 

resultStr = ""
lenPad = len(str(a) + str(b))
while 1:
    r = a % b
    if not r:
        break
    resultStr += f"{a} = {b} * {math.floor(a / b)} + {r}\n".ljust(lenPad)
    a = b
    b = r
print(resultStr)
print(f"GCD is : {b}")