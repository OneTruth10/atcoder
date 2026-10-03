N, V = map(int, input().split(" "))
W = [0] + [int(x) for x in input().split(" ")]

ans = 0
for i in range(1, N - 1):
    for j in range(i + 1, N):
        for k in range(j + 1, N + 1):
            if i + j + k <= V:
                tot = W[i] + W[j] + W[k]
                if tot > ans:
                    ans = tot
                    
print(ans)