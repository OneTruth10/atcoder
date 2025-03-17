s = input()
count = 0
for i in range(len(s)-1):
    if s[i]=="i" and s[i+1]=="i":
        count+=1
    elif s[i]=="o" and s[i+1]=="o":
        count+=1

if s[0]=="o":
    count+=1
if s[-1]=="i":
    count+=1
if (len(s)+count)%2!=0:
    count+=1

print(count)