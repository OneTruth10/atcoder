n, d = map(int, input().split(" "))
sus = []
result = 0
for _ in range(n):
    s, t = map(int, input().split(" "))
    sus.append((s,t))

sus.sort(key= lambda t: t[0])

for i in range(len(sus)-1):
    early = sus[i]
    max_start = early[1]-d

    left = i+1
    right = len(sus)-1
    limit_left = i+1

    while left<=right:
        mid = (left+right)//2
        if sus[mid][0]<=max_start:
            left = mid + 1
            limit_left = mid + 1
        else:
            right = mid - 1

    for j in range(i+1, limit_left):
        late = sus[j]
        if early[1]-late[0]<d:
            break
        else:
            duration = min(early[1], late[1]) - late[0]
            if duration>=d: result+= duration - d + 1
            #print(f"i: {i}. duration = {duration}. result = {result}")

print(result)