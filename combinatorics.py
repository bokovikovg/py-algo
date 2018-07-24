import numpy as np
import time

def A(n, k):
    n = int(n)
    k = int(k)
    x = np.ones(k, dtype=np.int32)
    res = []
    res.append([num for num in x])
    last = np.array([n for i in range(0, k)])
    while not np.array_equal(x, last):
        p = k - 1
        while not x[p] < n:
            p -= 1
        x[p] += 1
        x[p+1:k] = 1
        res.append([num for num in x])
    return res

def P(n):
    x = np.array([i for i in range(1, n+1)], dtype=np.int)
    last = np.array([i for i in range(n, 0, -1)], dtype=np.int)
    res = []
    res.append([num for num in x])
    while not np.array_equal(x, last):
        k = n - 2
        while x[k] > x[k+1]:
            k -= 1
        t = k + 1
        while (t < n - 1) and (x[t+1] > x[k]):
            t += 1
        temp = x[k]
        x[k] = x[t]
        x[t] = temp
        x[k+1:n:1] = x[n:k:-1]
        res.append([num for num in x])
    return res

def C(n, k):
    x = np.zeros(n, dtype=np.int)
    last = np.zeros(n, dtype=np.int)
    x[n-k:n] = 1
    last[0:k] = 1
    res = []; res.append([num for num in x])
    while not np.array_equal(x, last):
        s = n - 2
        while not ((x[s] == 0) and (x[s+1] == 1)):
            s -= 1
        num = 0
        for k in range(s, n):
            num += x[k]
        x[s] = 1
        x[s+1:n-num+1] = 0
        x[n-num+1:n] = 1
        res.append([t for t in x])
    return res
#Разбиения
def partition(number):
     answer = set()
     answer.add((number, ))
     for x in range(1, number):
         for y in partition(number - x):
             answer.add(tuple(sorted((x, ) + y)))
     return answer

def main():
    print("A(3, 2)={0}".format(A(3,2)))
    print("P(3)={0}".format(P(3)))
    print("C(4, 2)={0}".format(C(4, 2)))
    print("partition of 4 is ", partition(4))

if __name__ == '__main__':
    main()
