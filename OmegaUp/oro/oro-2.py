data = []

while True:
    try:
        line = input()
        data.append(line)
    except EOFError:
        # Python arroja este error cuando termina de leer el archivo
        break  # aquí ya puedes usar |line|

N,B = (int(x) for x in data[0].split())
val = list(int(x) for x in data[1:])
S = sum(val)
#print(N, B, val, S)

# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W

# We initialize the matrix with -1 at first.
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsack(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

        # choice diagram code
    if wt[n - 1] <= W:
        t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
            knapsack(wt, val, W, n - 1))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = knapsack(wt, val, W, n - 1)
        return t[n][W]

print(S-knapSack(S-B, val, val, len(val))-B)