import matplotlib.pyplot as plt
import numpy as np

def up(x):
    m = 11
    n = 20
    y = np.array([0.5 for k in range(len(x))])
    for i in range(m):
        p = 1
        for j in range(n):
            p *= np.sin(np.pi*(2*i - 1)/2**j)/(2*i - 1)
        y += p * np.cos(np.pi*(2*i - 1)*x)
    return y

def main():
    x = np.arange(-1, 1, 0.0001)
    y = up(x)
    fig = plt.subplots()
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()
