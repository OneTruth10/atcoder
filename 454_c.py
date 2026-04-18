N, M = map(int, input().split(" "))
path = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a, b = map(int, input().split(" "))
    path[a].append(b)

def dfs(start, path):
    visited = set()
    visited.add(start)
    stack = [start]
    while stack:
        u = stack.pop()
        for v in path[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return len(visited)

print(dfs(1, path))