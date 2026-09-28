from functools import reduce
from operator import xor

N, Q = map(int, input().split(" "))
a = [0 for i in range(N+1)]
result = []
#print(a)
for _ in range(Q):
    query = list(map(int, input().split(" ")))
    if len(query)==2:
        a[query[1]]+=1
    else:
        for i in range(len(a)):
            if a[i]>=1:
                a[i]-=1
    temp = reduce(xor, a)
    result.append(str(temp))

print("\n".join(result))