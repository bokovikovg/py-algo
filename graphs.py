# TASK 2
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, k):
    eps = 0.01
    if np.fabs(x + eps) < 0:
        return 1
    return np.sin(np.pi*x/(a**k))/(np.pi*x/a**k)

def draw_graph(astart, alpha, step, task):
    alpha = np.arange(astart, alpha, step)
    phi = np.arange(0.0, 2*np.pi, 0.001)
    fig, ax = plt.subplots()
    #plt.xlim(-20, 20), plt.ylim(-20, 20)
    plt.axis('equal')
    for a in alpha:
        if task == 'a' or task == 'b':
            #task A (circles)
            x, y = a*np.cos(phi), a*np.sin(phi)
            plt.plot(x, y)
            if task == 'b':
                #task Б (astroids)
                x, y = a*(np.cos(phi))**3, a*(np.sin(phi))**3
                plt.plot(x, y)
        if task == 'c':
            # task B
            rho = np.ones(len(phi)) - a*np.sin(phi)
            x, y = rho*np.cos(phi), rho*np.sin(phi)
            plt.plot(x, y)
        if task == 'd':
            x = np.arange(-1, 1, 0.001)
            n = len(x)
            y = np.ones(n) - np.fabs(x)**a
            y = np.fabs(y)
            plt.plot(x, y, x, -y)
        if task == 'e':
            x = np.arange(-10, 10, 0.001)
            t = np.ones(len(x))
            for k in range(1, 21):
                t *= np.sinc(x/(a**k))
            t = np.fabs(t)
            y = np.log10(t)
            plt.xlim(-10, 10), plt.ylim(-np.max(y), np.max(y))
            plt.plot(x, y)
    plt.show()


def main():

    draw_graph(0.1, 1, 0.1, 'e')

if __name__ == '__main__':
    main()
