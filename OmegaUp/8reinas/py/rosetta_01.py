# https://code.activestate.com/recipes/576647/

from itertools import permutations
from pprint import pprint

def nqueens(n):
    cols = range(n)
    for vec in permutations(cols):
        #pprint(vec)
        S0 = set(vec[i] + i for i in cols)
        S1 = set(vec[i] - i for i in cols)
        #pprint(S0)
        #pprint(S1)
        #print()
        if n == len(S0) == len(S1):
            print(vec)
            board(vec, n)
            break

def board(vec, n):
    print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n")

nqueens(4)
