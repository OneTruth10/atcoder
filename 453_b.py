T, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
last = A[0]

print("0", last)
for i in range(1,T+1):
    if abs(last-A[i])>=X:
        last = A[i]
        print(i, last)