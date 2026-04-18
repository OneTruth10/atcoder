N = int(input())
costs = {i:[] for i in range(N-1)}
found = False

for i in range(N-1):
    costs[i] = list(map(int, input().split(" ")))

for a in range(N-2):
    if found:
        break
    for c in range(a+2, N):
        if found:
            break
        #print(a,c)
        #a=N-1, c=
        direct_c = costs[a][c-(a+1)]
        for b in range(a+1,c):
            #print(b, c)
            cost = costs[a][b-(a+1)] + costs[b][c-(b+1)]
            if cost<direct_c:
                found = True
                break


if found:
    print("Yes")
else:
    print("No")