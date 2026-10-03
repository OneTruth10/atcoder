N, Q = map(int, input().split(" "))
num_range = {}
result = []
for i in range(Q):
    l, r, x = map(int, input().split(" "))
    temp = num_range.get(x, [])
    temp.append((l, r))
    num_range[x] = temp
    
diff = [0] * (N+2)

for x, intervals in num_range.items():
    intervals.sort()
    merged = []
    for l, r in intervals:
        if not merged:
            merged.append([l, r])
        else:
            if l <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], r)
            else:
                merged.append([l, r])
    for l, r in merged:
        diff[l] += 1
        diff[r+1] -= 1
        

cnt = 0
for i in range(1, N+1):
    cnt += diff[i]
    result.append(str(cnt))
    
print(" ".join(result))