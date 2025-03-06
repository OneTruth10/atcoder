n = int(input())
grid = [["?"]*n for i in range(n)]

for i in range(1, n+1):
    j = n + 1 - i
    if i<=j:
        if i%2==0:
            for s in range(i-1,j):
                for t in range(i-1,j):
                    grid[s][t] = "."
        elif i%2!=0:
            for s in range(i-1,j):
                for t in range(i-1,j):
                    grid[s][t] = "#"

for i in range(n):
    print("".join(grid[i]))