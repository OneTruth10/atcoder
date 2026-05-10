import math

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

def isOk(x):
    result = 0
    for i in range(1, N+1):
        if A[i-1]<x:
            need = (x - A[i-1])
            if need%i!=0:
                result += need//i + 1
            else:
                result += need//i
            if result>K:
                return False
    return True

bottom = 1
top = A[0] + K + 1
while top-bottom > 1:
    m = (top + bottom)//2
    if isOk(m):
        bottom = m
    else:
        top = m
print(bottom)