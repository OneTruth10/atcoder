sequence = input()
sequence = sequence.split()
matched = False




        
for i in range(5):
    if matched:
        break
    for j in range(i+1, 5):
        temp = sequence[:]
        temp[i], temp[j] = temp[j], temp[i]
        #print(j)
        #print(temp)
        if temp == ["1","2","3","4","5"]:
            print("Yes")
            matched = True
    
            

if not matched:
    print("No")