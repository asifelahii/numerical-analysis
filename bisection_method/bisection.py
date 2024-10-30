import math

def f(x):
    return 3 * x - math.cos(x) - 1 # f(x) = 3x - cos x - 1

def bisection(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("Error: Root is not bracketed")
        return None
    
    c = a;
    while abs(b-a) / 2.0 >tol:
        c = (a+b)/2.0
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c;
        else: a = c
    
    return c

# main
a = 0
b = 1
tol = 1e-5

# calling bisection function
root = bisection(f, a, b, tol)
if root is not None:
    print(f"Root found: {root}")
else: print("No root found")