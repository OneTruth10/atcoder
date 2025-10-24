N, Q = map(int, input().split())
version = list(range(N + 2))
count = [0 for _ in range(N + 2)]
for i in range(1, N + 1):
    count[i] = 1
result = []
def find(x):
    while version[x] != x:
            version[x] = version[version[x]]
            x = version[x]
    return x

for _ in range(Q):
    X, Y = map(int, input().split())
    total = 0
    i = find(1)
    while i <= X:
        total += count[i]
        count[i] = 0
        version[i] = find(i+1)
        i = version[i]
    result.append(total)
    count[Y] += total
    
for output in result:
    print(output)