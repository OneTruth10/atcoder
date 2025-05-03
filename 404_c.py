n, m = map(int, input().split(' '))

graph = {}

for i in range(m):
    a,b = map(int, input().split(" "))
    a_set = graph.get(a, set())
    b_set = graph.get(b, set())
    a_set.add(b)
    b_set.add(a)
    graph[a] = a_set
    graph[b] = b_set
found = False
start = a
seen = set([a])
stack = list(graph[a])
while stack:
    node = stack.pop(-1)
    if node not in seen:
        seen.add(node)
        stack.extend(graph[node])
    elif node==start and not seen.difference(set(stack))==seen:
        print("Yes")
        found = True
        break
        
        
if not found:
    print("No")