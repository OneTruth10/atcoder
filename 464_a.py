S = input()
w, e = 0, 0
for char in S:
    if char=="W":
        w+=1
    else:
        e+=1
if w>e:
    print("West")
else:
    print("East")