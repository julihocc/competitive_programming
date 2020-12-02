import numpy as np
from pprint import pprint

def get_a(N):

    a = np.zeros((N,N))

    n = int(input())

    for idx in range(n):
        i,j = [int(x) for input().split()]
        a[i-1][j-1] = 1

    return a

def free_backslash(b,r,c):
    k = 1
    while r-k>-1 and c-k>-1:
        if b[r-k][c-k]==1:
            return False
        k+=1
    return True

def free_slash(b,r,c,n):
    k = 1
    while r+k<n and c-k>-1:
        if b[r+k][c-k]==1:
            return False
        k+=1
    return True

def free_row(b,r,c):
    k=1
    while c-k>-1:
        if b[r][c-k]==1:
            return False
        k+=1
    return True

def subqueen(b, n, c):
    #pprint(b)
    for r in range(n):
        if free_backslash(b, r, c):
            if free_row(b, r, c):
                if free_slash(b, r, c, n):
                    b[r,c] = 1
                    if c==n-1:
                        return True
                    else:
                        ok = subqueen(b, n, c+1)
                        if ok:
                            return True
                        else:
                            b[r,c]=0
