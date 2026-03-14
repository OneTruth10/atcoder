from math import comb
N, M = map(int, input().split(" "))
conflicts = {i:set() for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split(" "))
    conflicts[a].add(b)
    conflicts[b].add(a)

for i in range(1,N+1):
    temp = len(conflicts[i])+1
    if N-temp<3:
        result = "0"
    else:
        result = str(comb(N-temp, 3))
    if i==N:
        print(result, end="")
    else:
        print(result, end=" ")

