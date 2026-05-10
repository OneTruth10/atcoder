from collections import deque

def bfs(H, W , start, goal, grid):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    d_chars = ["U","D","L","R"]

    q = deque()
    visited = {}

    for d in range(4):
        nr, nc = start[0]+dr[d], start[1]+dc[d]
        if 0<=nr<H and 0<=nc<W and grid[nr][nc]!="#":
            state = (nr, nc, d)
            visited[state] = None
            q.append(state)

    while q:
        r, c, d_in = q.popleft()
        if (r, c) == goal:
            return "Yes"
        
        cell = grid[r][c]
        for d_out in range(4):
            if cell=='o' and d_out!=d_in:
                continue
            if cell=='x' and d_out==d_in:
                continue
            nr, nc = r + dr[d_out], c + dc[d_out]
            if 0<=nr<H and 0<=nc<W and grid[nr][nc]!="#":
                new_state = (nr, nc, d_out)
                if new_state not in visited:
                    visited[new_state] = (r, c, d_in)
                    q.append(new_state)
    return "No"



H, W = map(int, input().split(" "))
grid = []

for i in range(H): 
    s = list(input().strip())
    grid.append(s)
    if "S" in s:
        start = (i,s.index("S"))
    if "G" in s:
        goal = (i, s.index("G"))


print(bfs(H,W,start,goal,grid))