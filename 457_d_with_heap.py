#Heap do not work

import heapq

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
val_index = {}
keys_heap = []

for i in range(N):
    temp = val_index.get(A[i], set())
    if not temp:
        heapq.heappush(keys_heap, A[i])
    temp.add(i)
    val_index[A[i]] = temp
    
for i in range(K):
    while keys_heap and keys_heap[0] not in val_index:
        heapq.heappop(keys_heap)
    min_val = keys_heap[0]
    
    min_index = min(val_index[min_val], default=-1)
    val_index[min_val].remove(min_index)
    
    added = min_val + min_index + 1
    
    get_val_set = val_index.get(added, set())
    if not get_val_set:
        heapq.heappush(keys_heap, added)
    get_val_set.add(min_index)
    val_index[added] = get_val_set
    
    if val_index[min_val] == set():
        del val_index[min_val]
        heapq.heappop(keys_heap)

while keys_heap and keys_heap[0] not in val_index:
    heapq.heappop(keys_heap)
print(keys_heap[0])