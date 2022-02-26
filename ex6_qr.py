'''
x is a Quadratic Residue if there exists a such that a**2 = x mod p
otherwise the integer is a Quadratic Non-Residue.
'''

def mod(n,m):
    return n%m

p = 29
ints = [14, 6, 11]

qr = [i for i in range(p) if mod(i**2, 29) in ints]
sol = min(qr)

print(f"{mod(sol**2, 29)} is a quadratic residue and it's root is {sol}.")