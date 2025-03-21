result = 0
print(str(100)[2])
for i in range(100,345679):
    temp = str(i)
    for j in range(len(temp)-2):
        if temp[j]==temp[j+1] and temp[j]==temp[j+2]:
            result+=i
            break
        
            
print(result)