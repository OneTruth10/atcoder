count = 0

for i in range(1, 12000):
    seen = []
    for j in range(1,int(i)):
        k = i/j
        temp = (j**2 + k**2)**0.5
        if temp == int(temp) and k==int(k):
            if not set([j,k,temp]) in seen:
                seen.append(set([j,k,temp]))
                count += 1
                
                    
print(count)