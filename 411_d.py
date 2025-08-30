n, q = map(int, input().split(" "))

computer = {}

for i in range(q):
    query = input().split(" ")
    p = int(query[1])
    if query[0]=="1":
        temp = computer.get(0, [])
        computer[p] = temp[:]
    elif query[0]=="2":
        temp = computer.get(p, [])
        temp.append(query[2])
        computer[p] = temp[:]
    else:
        temp = computer.get(p, [])
        computer[0] = temp[:]
t = computer.get(0, [])
print("".join(t))
