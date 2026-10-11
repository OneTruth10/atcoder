N = int(input())
S = input()

max_rain = 0
curr = 0
for i in range(len(S)):
    if S[i]=="R":
        curr+=1
        max_rain = max(max_rain , curr)
    else:
        curr = 0
        
print(max_rain)