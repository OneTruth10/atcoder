import math
from bisect import bisect_right
N, M, K = map(int, input().split(" "))
X, Y = map(int, input().split(" "))

A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A.sort()
B.sort()
result = 0

pref_a = [0]*(N+1)
for i in range(N):
    pref_a[i+1] = A[i] + pref_a[i]
    
drink_cost = [0]
drink_k = [0]
for b in B:
    drink_cost.append(drink_cost[-1]+b)
    need_k = math.ceil(b/K)
    drink_k.append(drink_k[-1]+need_k)
    

total_money = X + Y * K
max_items = 0
for d_cnt in range(M+1):
    if drink_k[d_cnt]>Y:
        break
    rem_money = total_money - drink_cost[d_cnt]
    dessrt_cnt = bisect_right(pref_a, rem_money) - 1
    max_items = max(max_items, dessrt_cnt+d_cnt)
        
print(max_items)