from math import sqrt

def level(x):
    y = int(sqrt(x))
    if y**2==x:
        return y-1
    else:
        return(y)

