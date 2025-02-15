first = input().split(" ")
result = set()
count = 0
for i in range(int(first[1])):
    edge = input().split(' ')
    if int(edge[0])>int(edge[1]):
        edge[0], edge[1] = int(edge[1]), int(edge[0])
    else:
        edge[0], edge[1] = int(edge[0]), int(edge[1])
    edge = tuple(edge)
    if edge[0]==edge[1] or edge in result:
        count+=1
    else:
        result.add(edge)


print(count)