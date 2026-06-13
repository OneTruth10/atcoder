h, w = map(int, input().split(" "))
result = [[] for i in range(h)]

for i in range(h):
    for j in range(w):
        count = 0
        if i-1>=0:
            count+=1
        if i+1<h:
            count+=1
        if j-1>=0:
            count+=1
        if j+1<w:
            count+=1
        result[i].append(count)
    result[i] = " ".join(list(map(str, result[i])))
                
        
print("\n".join(result))