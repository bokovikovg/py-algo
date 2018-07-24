import numpy as np

def mean(x):
    return np.sum(x)/len(x)

def std(x):
    return (np.sum([(x[i]-mean(x))**2 for i in range(len(x))])*1/len(x))**0.5
