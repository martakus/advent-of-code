#!/usr/bin/python
import numpy as np

def findTriangle(arr):
    arr.sort(axis=1)
    return sum(np.sum(arr[:,:2],axis=1)>arr[:,2])

def day3(arr):
    return findTriangle(arr.copy()),findTriangle(arr.copy().T.reshape(-1,3))

if __name__ == '__main__':
    import sys
    f = np.loadtxt(sys.argv[1])
    print day3(f)
