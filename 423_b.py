n = int(input())
l = input().split(" ")
visited = 2
left_closed = False
right_closed = False
for i in range(n):
    if l[i]=="1":
        left_closed = True
    if l[-(i+1)]=="1":
        right_closed = True
    if l[i]=="0" and not left_closed:
        visited+=1
    if l[-(i+1)]=="0" and not right_closed:
        visited+=1
unvisited = max(0, (n+1-visited))
print(unvisited)