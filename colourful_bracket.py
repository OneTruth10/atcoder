t = input()
i = 1

while i<len(t):
    if t[i-1]=="(" and t[i]==")":
        if i<len(t)-1 and i>1:
            t = t[:i-1] + t[i+1:]
            i-=2
        elif i==1:
            t = t[2:]
            i-=2
        else:
            t = t[:i-1]
        print(t)
    elif t[i-1]=="[" and t[i]=="]":
        if i<len(t)-1 and i>1:
            t = t[:i-1] + t[i+1:]
            i-=2
        elif i==1:
            t = t[2:]
            i-=2
        else:
            t = t[:i-1]
        print(t)
    elif t[i-1]=="<" and t[i]==">":
        if i<len(t)-1 and i>1:
            t = t[:i-1] + t[i+1:]
            i-=2
        elif i==1:
            t = t[2:]
            i-=2
        else:
            t = t[:i-1]
        print(t)
    i+=1
            
if t=="":
    print("Yes")
else:
    print("No")