n = int(input())
if n==1:
    print('1')
elif n==2 or n==3:
    print('NO SOLUTION')
else:
    evens = tuple(str(x) for x in range(1,n+1) if x%2==0)
    #print(evens)
    odds = tuple(str(x) for x in range(1,n+1) if x%2==1)
    #print(odds)
    print(" ".join(evens)+" "+" ".join(odds))

