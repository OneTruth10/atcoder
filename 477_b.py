N, D = map(int, input().split(" "))
P = list(map(int, input().split(" ")))
result = []
p = [(i, P[i]) for i in range(len(P))]
p.sort(key=lambda x: x[1])
for i in range(len(P)):
    if i+1==len(P):
        if abs(p[i][1]-p[i-1][1])>=D:
            result.append(p[i][0]+1)
    elif abs(p[i][1]-p[i-1][1])>=D and abs(p[i+1][1]-p[i][1])>=D:
        result.append(p[i][0]+1)

result.sort()        
print(len(result))
print(" ".join(map(str, result)))
