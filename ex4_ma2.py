def mod(n,m):
    return n%m

#r = mod(7**16,17)
r = mod(273246787654**65536,65537)

print(r)

'''
Theorem: a**(p-1) = 1 mod(p)
which means mod(a**(b-1),b) is always 1
'''