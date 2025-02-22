initial = input()
result = ""
swapped = False
w = False
count = 0
for i in range(len(initial)):
    if initial[i]=="W":
        w = True
        count+=1
        if i==len(initial)-1:
            result+="W"*count
    elif w and initial[i]=="A":
        result += "A" + "C"*count
        count = 0
        w = False
    elif w and initial[i]!="A":
        result = result + "W"*count + initial[i]
        count = 0
        w = False
    else:
        result += initial[i]
        w = False

        
print(result)
        