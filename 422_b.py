h, w = map(int, input().split(" "))
grid = ["" for i in range(h)]
looped = True
for i in range(h):
    grid[i] = input()

for i in range(h):
    for j in range(w):
        count = 0
        black = False
        if grid[i][j]=="#":
            black = True
            if j-1>=0 and grid[i][j-1]=="#":
                count+=1
            if j+1<w and grid[i][j+1]=="#":
                count+=1
            if i-1>=0 and grid[i-1][j]=="#":
                count+=1
            if i+1<h and grid[i+1][j]=="#":
                count+=1
        if black and not (count==2 or count==4):
            looped = False

if looped:
    print("Yes")
else:
    print("No")