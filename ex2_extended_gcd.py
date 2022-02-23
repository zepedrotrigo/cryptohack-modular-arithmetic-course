def gcd(a,b, calls=0):
    r = a%b

    if r == 0:
        return b, calls

    return gcd(b,r,calls+1)

def get_integers(a,b,calls): # http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
    r = [b,a] # list of division remainders
    for i in range(calls-1): # -1 because the last value is not needed
        r.append(r[-2]%r[-1]) # keep calculation division remainders between last two numbers in list

    u = 0
    v = 1
    for i in range(1,len(r)):
        tmp = u
        u = v - (r[-i-1]//r[-i]) * u # (expr inside) goes through list of remainders in reverse
        v = tmp

    return u,v


a = 26513
b = 32321

val, calls = gcd(a,b)
u,v = get_integers(a,b, calls)
print(f"u*{a} + v*{b} = gcd({a},{b}) if u={u} and v={v}")
