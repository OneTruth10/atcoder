H, W = map(int, input().split(" "))
S = []
seen = set()
queue = []
result = 0
flag = False
for i in range(H):
    S.append(input().split(" "))


for i in range(1, H-1):
    for j in range(1, W-1):
        flag = False
        if S[i][j]=="." and (i,j) not in seen:
            up = (i-1,j)
            down = (i+1,j)
            left = (i, j-1)
            right = (i, j+1)
            queue.extend(up, down, left, right)
            seen.add((i,j))
            while queue:
                if queue.pop(0) not in seen :
                    a, b = queue.pop(0)
                    