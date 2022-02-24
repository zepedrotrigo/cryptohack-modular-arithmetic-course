'''
Theorem: a**(p-1) = 1 mod(p)

3**(13-1) = 1 mod 13
3**12 = 1 mod 13
3 * 3**11 = 1 mod 13

But 3**11 not in range [0,13-1] so:
3**11 % 13 = multiplicative inverse
'''

print(3**11 % 13)