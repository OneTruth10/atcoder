T = int(input())
result = []
for _ in range(T):
    N = int(input())
    base = 0
    minA = 100_000_000_000
    diff = []
    for _ in range(N):
        a, b = map(int, input().split(" "))
        base += a
        minA = min(a, minA)
        diff.append(b-a)
    diff.sort()
    ans = base
    curr = base
    for k in range(1, N+1):
        curr += diff[k-1]
        ans = min(ans, curr + max(0, 2*k - N)*minA)
    result.append(str(ans))
    
print("\n".join(result))