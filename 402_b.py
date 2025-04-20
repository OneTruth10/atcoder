q = int(input())

queue = []
result = []
for i in range(q):
    query = input().split(" ")
    if query[0] == "1":
        queue.append(query[1])
    else:
        result.append(queue.pop(0))
        
        
print("\n".join(result))
    