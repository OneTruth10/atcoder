N = int(input())
A = [0 for i in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split(" ")))
#print(A)
X, Y = map(int, input().split(" "))

print(A[X-1][Y])