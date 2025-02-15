string = input()
count = 0

for i in range(len(string)-2):
    for j in range(1, (len(string)-i+1)//2):
        if string[i]=="A" and string[i+j]=="B" and string[i+2*j]=="C":
            count+=1



print(count)