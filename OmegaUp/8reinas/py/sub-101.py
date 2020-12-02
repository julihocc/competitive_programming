import numpy as np
from pprint import pprint

def nqueens(n, a, coor):
    b = np.zeros((n,n), dtype=int)
    for r in range(n):
        b[r][0]=1
        ok = subqueen(a,b, n, 1, coor)
        if ok:
            return True, coor
        else:
            b[r][0]=0
    return False, coor

def get_a(N):

    a = np.zeros((N,N), dtype=int)

    coordenadas = set()

    n = int(input())

    for idx in range(n):
        dato = tuple(int(x) for x in input().split())
        i,j = dato
        coordenadas.add(dato)
        a[i-1][j-1] = 1

    return a, coordenadas

def free_backslash(a,b,r,c):
    k = 1
    while r-k>-1 and c-k>-1:
        if b[r-k][c-k]==1 or a[r-k][c-k]==1:
            return False
        k+=1
    return True

def free_slash(a,b,r,c,n):
    k = 1
    while r+k<n and c-k>-1:
        if b[r+k][c-k]==1 or a[r+k][c-k]==1:
            return False
        k+=1
    return True

def free_row(a,b,r,c):
    k=1
    while c-k>-1:
        if b[r][c-k]==1 or a[r][c-k]==1:
            return False
        k+=1
    return True

def free_col(a,b,n,c):
    for k in range(c):
        if b[k][c]==1 or a[k][c]==1:
            return False
    return True


def subqueen(a,b, n, c, coor):
    #pprint(b)
    for r in range(n):
        if free_backslash(a,b, r, c):
            if free_row(a,b, r, c):
                if free_slash(a,b, r, c, n):
                    b[r,c] = 1
                    if c==n-1:
                        coor.add((r+1, c+1))
                        return True
                    else:
                        ok = subqueen(a,b, n, c+1, coor)
                        if ok:
                            coor.add((r+1, c+1))
                            return True
                        else:
                            b[r,c]=0

if __name__=='__main__':
    a, coor = get_a(8)
    #pprint(a)
    #pprint(coor)
    #pprint(nqueens(8, a, coor))
    ok, coor = nqueens(8, a, coor)
    if ok:
        for row in coor:
            i,j = row
            print(i,j)
    else:
        print(0)