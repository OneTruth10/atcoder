n, m = map(int, input().split(' '))
if m==0:
    print("No")
    exit()
graph = {}

for i in range(m):
    a,b = map(int, input().split(" "))
    a_set = graph.get(a, set())
    b_set = graph.get(b, set())
    a_set.add(b)
    b_set.add(a)
    graph[a] = a_set
    graph[b] = b_set
    
for node in graph:
    if len(graph[node]) != 2:
        print("No")
        exit()
for node in graph:
    start = node
    break

seen = set()
stack = [start]

while stack:
    node = stack.pop()
    if node not in seen:
        seen.add(node)
        stack.extend(graph[node] - seen)
        

if len(seen) == n:
    print("Yes")
else:
    print("No")