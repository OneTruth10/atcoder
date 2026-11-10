from collections import deque
n = int(input())
conditions = []
found = True
for _ in range(n):
    u, c, v = input().split(" ")
    conditions.append((u,c,v))
s = input()

nodes = set(list(s))
char_num = {}
for char in s:
    temp = char_num.get(char, 0) + 1
    char_num[char] = temp
adj = {node:[] for node in nodes}
in_degree = {node: 0 for node in nodes}

for u, c, v, in conditions:
    if c=="<":
        adj[u].append(v)
        in_degree[v] += 1
    else:
        adj[v].append(u)
        in_degree[u] += 1
        
q = deque([node for node in nodes if in_degree[node]==0])
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        in_degree[v] -= 1
        if in_degree[v]==0:
            q.append(v)
            
if len(order)!=len(nodes):
    found = False
    
result = ""
if found:
    for char in order:
        result += char*char_num[char]
else:
    result = "IMPOSSIBLE"
print(result)