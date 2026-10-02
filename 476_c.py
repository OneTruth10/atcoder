N = int(input())
a = list(map(int, input().split(" ")))
result = []
three = a[:3]
three.sort(reverse=True)
#print(three)
result.append(three[2])
for i in range(3,N):
    #print(i)
    right = a[i]
    if right>three[2]:
        three[2] = right
    three.sort(reverse=True)
    result.append(three[2])
    
    
print("\n".join(map(str, result)))