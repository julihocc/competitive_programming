def check(n):
    from itertools import permutations
    for p in permutations(range(1,n+1)):
        valid = True
        for i in range(len(p)-1):
            if p[i+1]-p[i] in set([1,-1]):
                valid = False
                break
        if valid:
            return p
    return None

if __name__=='__main__':
    n = int(input())
    output = check(n)
    if output is not None:
        #print(output)
        output = (str(x) for x in output)
        print(' '.join(output))
    else:
        print('NO SOLUTION')

