def gcd(a,b):
    r = a%b

    if r == 0:
        return b

    return gcd(b,r)

print(gcd(66528,52920))