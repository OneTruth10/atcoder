n = input()
arr = input().split(' ')

seen = {}
length = 100000000000
for i in range(int(n)):
    if arr[i] in seen:
        temp = i-seen[arr[i]]
        length = min(temp, length)
        seen[arr[i]] = i
    else:
        seen[arr[i]] = i


if length==100000000000:
    print("-1")
else:
    print(length+1)