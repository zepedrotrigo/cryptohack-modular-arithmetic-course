from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag]) # converts string to bytes
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1': # If byte is 1
            ciphertext.append(n) # appends pow(a,e,p)
        else: # If byte is 0
            n = -n % p # appends -pow(a,e,p) % p
            ciphertext.append(n)
    return ciphertext # so we can get the binary information of the string by doing pow(i,(p-1)//2,p) == 1


print(encrypt_flag(FLAG))