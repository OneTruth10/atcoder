N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
result = 0
for y in A:
    if y==K:
        result += 1
for i in range(len(A)-1):
    low = min(A[i], A[i+1])
    high = max(A[i], A[i+1])
    if low < K < high:
        result += 1
        
print(result)