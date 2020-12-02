import numpy as np
from pprint import pprint

from aux101 import *

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