import math
n = int(input())
max_r = -10000000
min_r = 100000000000
max_c = -1000000000000
min_c = 1000000000000
for i in range(n):
    r, c = map(int, input().split(" "))
    max_r = max(max_r, r)
    min_r = min(min_r, r)
    max_c = max(max_c, c)
    min_c = min(min_c, c)
max_dif = max(math.ceil((max_r-min_r)/2), math.ceil((max_c-min_c)/2))
print(max_dif)