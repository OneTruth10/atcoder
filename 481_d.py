from collections import deque

N, M , S, T = map(int, input().split(" "))
routes = {}
min_planets = {}
for _ in range(M):
    A, B = map(int, input().split(" "))
    min_planet = min_planets.get(A, 100_000_000)
    min_planet = min(min_planet, B)
    min_planets[A] = min_planet
    temp = routes.get(A, [])
    temp.append(B)
    routes[A] = temp
    
visited = set()
dp = {S:0}
q = deque([S])
while q:
    node = q.popleft()
    if routes.get(node, -1)==-1:
        continue
    
    min_val = min_planets.get(node, -1)
        
    for neighbor in routes[node]:
        weight = 0 if min_val==neighbor else 1
        next_cost = weight + dp[node]
        if neighbor not in dp or next_cost<dp[neighbor]:
            dp[neighbor] = next_cost
            if weight==0:
                q.appendleft(neighbor)
            else:
                q.append(neighbor)

"""                
stack = [(S, 0)]
while stack:
    node, parent = stack.pop()
    if (node, parent) not in visited:
        print(node, parent)
        visited.add((node, parent))
        temp = dp.get(node, 100_000_000)
        if min_planets[parent]==node:
            dp[node] = min(dp[parent], temp)
        else:
            dp[node] = min((dp[parent]+1), temp)
        if routes.get(node, -1)==-1:
            continue
        for neighbor in routes[node]:
            if (neighbor, node) not in visited:
                stack.append((neighbor, node))
        print(dp)
"""
print(dp.get(T, -1))
