# https://code.activestate.com/recipes/576647/

from itertools import permutations
from functools import reduce
from pprint import pprint

def board(vec, n):
    print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n")

def get_res():

    n = int(input())
    res = {}
    for idx in range(n):
        i,j = [int(x) for x in input().split()]
        res[i-1] = j-1
    #pprint(res)
    return res

def nqueens(n, res):
    cols = range(n)
    for vec in permutations(cols):
        if res:
            myiter = (vec[k]==v for k,v in res.items())
            ok = reduce(lambda x,y: x and y, myiter)
        else:
            ok = True
        if ok:
            S0 = set(vec[i] + i for i in cols)
            S1 = set(vec[i] - i for i in cols)
            if n == len(S0) == len(S1):
                #pprint(vec)
                #board(vec, n)
                return vec

if __name__=='__main__':
    res = get_res()
    output = nqueens(8, res)
    if output is not None:
        for i,j in enumerate(output):
            print(i+1, j+1)
    else:
        print(0)


