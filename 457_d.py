import heapq
import sys

input = sys.stdin.read

data = input().split()
N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:   ]))
pq = []

for i in range(N):
    heapq.heappush(pq, (A[i], i+1))
    
    
for i in range(K):
    current_min, index_to_add = heapq.heappop(pq)
    new_val = current_min + index_to_add
    heapq.heappush(pq, (new_val, index_to_add))
        
print(pq[0][0])