N, M = map(int, input().split(" "))

edges = [tuple(map(int, input().split(" "))) for i in range(M)]
#print(edges)
ans = M
for bit in range(2**N):
    deleted = 0
    for u,v in edges:
        if (1&(bit >> u))==(1&(bit >> v)):
            deleted+=1
    ans = min(ans, deleted)

print(ans)