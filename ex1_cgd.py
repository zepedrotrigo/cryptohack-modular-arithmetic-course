a = 66528
b = 52920

def gcd(a,b):
    r = a%b

    if r == 0:
        return b

    return gcd(b,r)

print(gcd(a,b))




'''
First time writing the code step by step (incomplete):
(incomplete because I quickly realized b and r could be the arguments of a recursive function like in the solution above)

def gcd(a,b,r=None):
    r = a%b

    while True:
        r = b % r
        tmp = b
        b = r
        r = tmp
'''