# x = a1*N1*x1 + ... + an*Nn*xn

n1, n2, n3 = [5,11,17]
a1, a2, a3 = [2,3,5]

N = n1*n2*n3
N1,N2,N3 = [n2*n3, n1*n3, n1*n2]
x1, x2, x3 = [pow(N1,-1,n1), pow(N2,-1,n2), pow(N3,-1,n3)]

x = a1*N1*x1 + a2*N2*x2 + a3*N3*x3
print(x%N)