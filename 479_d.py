N, Q = map(int, input().split(" "))

L = [0] + list(map(int, input().split(" ")))
R = list(map(int, input().split(" "))) + [0]
new_r = [0]*N
new_l = [0]*N
min_right= 100_000_000_000
min_left = 100_000_000_000
result = []
for i in range(N-1):
    min_right = min(min_right, R[i])
    new_r[i] = min(R[i], min_right+L[i])
    min_left = min(min_left, L[-(i+1)])
    new_l[-(i+1)] = min(L[-(i+1)], min_left + R[-(i+1)])
    
for _ in range(Q):
    s, t = map(int, input().split(" "))
    if s<t:
        result.append(str(new_r[s-1]))
    else:
        result.append(str(new_l[s-1]))
        
print("\n".join(result))