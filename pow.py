# Implement pow(x, n).

# This is a great example to illustrate how to solve a problem during a technical 
# interview. The first and second solution exceeds time limit; the third and fourth
# are accepted

# O(n)
def pow(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x*pow(x, n-1)
    else:
        return (1.0/x)*pow(x, n+1)
    
assert pow(2, 0) == 1
assert pow(2, 3) == 8
assert pow(2, -1) == 1/2.0

# O(logn)
def pow2(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            t = pow(x, n/2)
            return t*t
        else:
            n = n - 1
            t = pow(x, n/2)
            return t*t*x

assert pow2(2, 0) == 1
assert pow2(2, 3) == 8
assert pow2(2, 8) == 2**8
assert pow2(2, -1) == 2**-1
assert pow2(2, -8) == 2**-8
