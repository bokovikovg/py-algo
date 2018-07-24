#polynoms are arrays a[n]*x**n + ... + a[1]*x + a[0]
# a[0:n]

from math import fabs

def poly_horner(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p


def poly_mul(p, q):
    k = len(p)
    l = len(q)
    m = k + l
    c = [0 for i in range(m)]
    for i in range(k):
        for j in range(l):
            c[i+j] = c[i+j] + p[i]*q[j]
    return c

def poly_add(p, q):
    k = len(p)
    l = len(q)
    n = abs(k-l)
    for i in range(n):
        if k > l:
            q.append(0)
        p.append(0)
    c = [p[i]+q[i] for i in range(max(k, l))]
    return c

def degree(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return len(poly)-1

def poly_div(n, d):
    dividend = n[::-1]
    divisor = d[::-1]
    print(dividend, divisor)
    out = list(dividend)
    normalizer = divisor[0]
    for i in range(len(dividend)-len(divisor)-1):
        out[i] /= normalizer
        coef = out[i]
        if coef != 0:
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef
    separator = -(len(divisor) - 1)
    return out[:separator], out[separator:]
def main():

    print("p(2)=", poly_horner([-3, 2, 1], 2))
    print("p*q=", poly_mul([10, 11, 12, 13], [5, -6, 7]))
    print("p+q=", poly_add([10, 11, 12, 13], [5, -6, 7]))
    print("p/q=", poly_div([-42, -12, 1], [-3, 1]))

if __name__ == '__main__':
    main()
