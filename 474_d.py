N = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
final_pos = 0
change = []
temp = 0
for i in range(len(a)):
    if a[i]<b[i]:
        temp = a[i]-b[i]
        final_pos += temp
        change.append("1")
    elif a[i]>b[i]:
        temp = (a[i]-b[i])*(10**18)
        final_pos += temp
        change.append(str((10**18)))
    else:
        change.append("1")
    #print(final_pos)
        
if final_pos<=0:
    print("No")
else:
    print("Yes")
    print(" ".join(change))
            
    