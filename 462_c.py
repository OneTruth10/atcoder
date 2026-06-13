n = int(input())

curr_min_y = 100_000_000
result = 0

coor = []
for _ in range(n):
    x, y = map(int, input().split(" "))
    coor.append((x,y))

coor.sort(key=lambda p: p[0])
for x,y in coor:
    if y<curr_min_y:
        result+=1
        curr_min_y = y

print(result)