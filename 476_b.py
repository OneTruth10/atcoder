N = int(input())
S = input()
T = input()
check = True
for i in range(len(T)):
    if T[i] == "*":
        pass
    elif T[i] != S[i]:
        check = False
        break
    
if check:
    print("Yes")
else:
    print("No")