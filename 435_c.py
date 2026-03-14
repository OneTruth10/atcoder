N = int(input())
a = list(map(int, input().split(" ")))
cum_a = [0]*(N+1)
for i in range(1, N+1):
    cum_a[i] = i+a[i-1]
    
i = 1
domino = cum_a[1]
while i<domino:
    domino = max(domino, cum_a[i])
    if domino>N:
        domino = N+1
    i+=1
    
print(domino-1)