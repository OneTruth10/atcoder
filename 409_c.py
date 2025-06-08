#I didn't parcipitate this contest but solved as a revision
n, l = map(int, input().split(" "))
d = map(int, input().split(' '))

points = {i:set() for i in range(l)}
next_point = 0
between = 0
previous = 0

for i, distance in enumerate(d):
    next_point += previous
    if next_point >= l:
        next_point -= l
    temp = points[next_point]
    temp.add(i)
    points[next_point] = temp
    previous = distance
    
next_point += previous
if next_point >= l:
        next_point -= l
temp = points[next_point]
temp.add(n-1)
points[next_point] = temp
#print(points)
if l%3!=0:
    print("0")
else:
    result = 0
    between = l//3
    for i in range(between):
        result += len(points[i]) * len(points[i+between]) * len(points[i+between*2])
    print(result)