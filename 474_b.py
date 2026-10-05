N = int(input())
P = list(map(int, input().split(" ")))
rule = True
for i in range(len(P)):
    if (P[i]-1)//10!=i//10:
        rule = False
        break
    
print("Yes" if rule else "No")