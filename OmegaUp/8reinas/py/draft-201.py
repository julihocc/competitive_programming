import numpy as np
from pprint import pprint

def nqueens(n):
    b = np.zeros((n,n), dtype=int)
    for r in range(n):
        b[r][0]=1
        ok = subqueen(b, n, 1)
        if ok:
            return b
        else:
            b[r][0]=0

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

if __name__=='__main__':
    print(nqueens(8))