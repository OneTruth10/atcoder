N,M,K = map(int, input().split(" "))
H = [*map(int, input().split(" "))]
B = [*map(int, input().split(" "))]
made = 0

H.sort()
B.sort()
last_elt = 0

for i in range(len(H)):
    if not last_elt>len(B)-1:
        for j in range(last_elt, len(B)):
            if B[j]>=H[i]:
                #print(B[j], H[i])
                last_elt = j + 1
                made+=1
                break
if made<K:
    print("No")
else:
    print("Yes")