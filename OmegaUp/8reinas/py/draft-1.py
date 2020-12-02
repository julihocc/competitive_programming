"""
Ryuhei Uehara
Algorithm 33: 8Queen(B) for the eight queens problem
Algorithm 34: Subroutine QueenSub(B, i)
"""

import pandas as pd

def NQueen(B, N):

    for col in range(N):
        B[col] = {}
        for row in range(N):
            B[col][row] = 0

    for row in range(N):
        B[0][row] = 1
        subQueen(B, N, 1)
        B[0][row] = 0

def subQueen(B, N, col):
    for row in range(N):
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
                cool_print(B)
            else:
                subQueen(B, N, col+1)
            B[col][row] = 0


def cool_print(B):
    df = pd.DataFrame(B)
    print(df)
    print("\n")


if __name__=="__main__":
    B = {}
    NQueen(B, 4)