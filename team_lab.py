result = []

for i in range(1,100000):
    temp = ""
    for chr in str(i):
        if chr == "8":
            temp+="SNOWMAN"
        else:
            temp+=chr
            
    result.append(temp)
    
print("-".join(result)[800887:800917])