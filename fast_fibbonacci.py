import numpy as np
from timeit import default_timer as timer

def fast_fibbonacci(n):
    m = np.array([[1, 1], [1, 0]], dtype='O')
    t = np.identity(2, dtype='O')
    while n > 0:
        if n % 2 == 1:
            t = m.dot(t)
        m = m.dot(m)
        n = n // 2
    return t[1][0]

def naive_fibbonacci(n):
    if n == 1 or n == 2:
        return 1
    return naive_fibbonacci(n-1) + naive_fibbonacci(n-2)

def fib(n):
    return np.linalg.matrix_power(np.array([[1, 1], [1, 0]], dtype='O'), n)[1,0]


def main():
    n = int(input("which fib number you wanna get?\n"))
    start = timer()
    print("Fast:\nF({0})={1}".format(n, fast_fibbonacci(n)))
    end = timer()
    print("calculated in {:.6f}".format(end - start))
    start = timer()
    print("Naive:\nF({0})={1}".format(n, naive_fibbonacci(n)))
    end = timer()
    print("calculated in {:.6f}".format(end - start))
    start = timer()
    print("Library method:\nF({0})={1}".format(n, fib(n)))
    end = timer()
    print("calculated in {:.6f}".format(end - start))


if __name__ == '__main__':
    main()
