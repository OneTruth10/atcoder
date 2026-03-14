T = int(input())
result = [0]*T
for test in range(T):
    N = int(input())
    w = 0
    temp = [0]*N
    for i in range(N):
        W, P = map(int, input().split(" "))
        w += W
        temp[i] = W + P
    temp.sort(reverse=True)
    for i in range(N):
        w -= temp[i]
        if w<=0:
            result[test] = N-(i+1)
            break

for _ in range(T):
    print(result[_])