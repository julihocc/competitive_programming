"""
Ryuhei Uehara
Algorithm 33: 8Queen(B) for the eight queens problem
Algorithm 34: Subroutine QueenSub(B, i)
"""

import pandas as pd
from copy import deepcopy

def NQueen(N):

    global soluciones

    B = {}

    for col in range(N):
        B[col] = {}
        for row in range(N):
            B[col][row] = 0

    for row in range(N):
        B[0][row] = 1
        subQueen(B, N, 1)
        if soluciones:
            return True
        #print(soluciones)
        B[0][row] = 0
    return False

def subQueen(B, N, col):

    global soluciones

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
                #soluciones.append(B.copy())
                soluciones.append(deepcopy(B))
                #cool_print()
            else:
                subQueen(B, N, col+1)
            B[col][row] = 0



def cool_print():

    global soluciones

    for B in soluciones:
        df = pd.DataFrame(B)
        print(df,'\n *')
    print('**')


if __name__=="__main__":
    soluciones = []
    ok = NQueen(8)
    if ok:
        print(len(soluciones))
        cool_print()
    else:
        print(None)