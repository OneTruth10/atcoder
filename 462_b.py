n = int(input())
result = {i:[] for i in range(1,n+1)}

for i in range(1, n+1):
    a = list(map(int, input().split(" ")))
    for j in range(1, len(a)):
        result[a[j]].append(str(i))


for i in range(1, n+1):
    print(len(result[i]), " ".join(result[i]))