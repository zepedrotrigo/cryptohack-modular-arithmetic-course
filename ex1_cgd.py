a = 66528
b = 52920

def gcd(a,b):
    r = a%b

    if r == 0:
        return b

    return gcd(b,r)

print(gcd(a,b))