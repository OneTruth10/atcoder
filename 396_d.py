n, m = input().split(' ')
graph = {i:[] for i in range(int(n))}
cost = {}
for i in range(int(m)):
    u, v, w = input().split(' ')
    graph[int(u)].append(int(v))
    cost[(int(u),int(v))] = int(w)

visited = set()  
stack = [1]+graph[1]
path = []
min_xor = 100_000_000_000
temp = 0

while stack: 
    node = stack.pop()
    if node not in visited:
        if node==int(n):
            path.append(node)
            temp = cost[tuple(path[0:2])]
            for i in range(1,len(path)-1):
                temp = temp ^ cost[tuple(path[i:i+2])]
            min_xor  = min(min_xor, temp)
            path = [1]
        elif len(graph[node])==0:
            visited = set()
            path = [1]
        else:
            visited.add(node)
            path.append(node)
        stack.extend(reversed(graph.get(node,[])))
    
print(min_xor)
