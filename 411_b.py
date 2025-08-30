n = int(input())
d = list(map(int, input().split(" ")))
#print(d)
for i in range(n-1):
    distance = 0
    temp = []
    for j in range(i, n-1):
        distance += d[j]
        temp.append(str(distance))
    print(" ".join(temp))
