# https://code.activestate.com/recipes/576647/

from itertools import permutations
from functools import reduce

def get_a():

    n = int(input())
    res = {}
    for idx in range(n):
        i,j = [int(x) for input().split()]
        res[i-1] = j-1
    return a

def nqueens(n, a):
    cols = range(n)
    for vec in permutations(cols):
        myiter = (vec[k]==v for k,v in a.items())
        if reduce(lambda x,y: x and y, myiter):
            S0 = set(vec[i] + i for i in cols)
            S1 = set(vec[i] - i for i in cols)
            if n == len(S0) == len(S1):
                print(vec)
                board(vec, n)
                break

if __
nqueens(4)
