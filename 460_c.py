import heapq

n, m = map(int, input().split(" "))
count = 0

a = [-x for x in map(int, input().split(" "))]
b = [-x for x in map(int, input().split(" "))]

heapq.heapify(a)
heapq.heapify(b)

while a and b:
    shari = -a[0]
    neta = -b[0]
    
    if neta <= shari * 2:
        heapq.heappop(a)
        heapq.heappop(b)
        count += 1
    else:
        heapq.heappop(b)

print(count)