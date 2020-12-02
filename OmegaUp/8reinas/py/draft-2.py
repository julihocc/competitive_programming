"""
Ryuhei Uehara
Algorithm 33: 8Queen(B) for the eight queens problem
Algorithm 34: Subroutine QueenSub(B, i)
"""

from pprint import pprint
import pandas as pd

def NQueen(N):

    B = {}
    ok = False

    for col in range(N):
        B[col] = {}
        for row in range(N):
            B[col][row] = 0

    for row in range(N):
        B[0][row] = 1
        ok = subQueen(B, N, 1)
        if ok:
            return B
        B[0][row] = 0

    return ok

def subQueen(B, N, col):
    for row in range(N):
        print(col, row)
        print(pd.DataFrame(B))
        print()
        c=0
        for k in range(col):
            if row-(col-k)>=0:
                c += B[k][row-(col-k)]
            c += B[k][row]
            if row+(col-k)<N:
                c += B[k][row+(col-k)]
        if c==0:
            B[col][row] = 1
            if col == N-1:
                pprint(B)
                return True
            else:
                ok = subQueen(B, N, col+1)

    return False




if __name__=="__main__":
    output = NQueen(4)
    pprint(output)