n, q = input().split(' ')
label = {i:i for i in range(1,int(n)+1)}
pegion = {i:i for i in range(1,int(n)+1)}
result = []
for i in range(int(q)):
    op = input().split(" ")
    if op[0]=="1":
        nest[pegion[op[1]]].remove(op[1])
        pegion[op[1]] = op[2]
        nest[op[2]].append(op[1])
    elif op[0]=="2":
        nest[op[1]], nest[op[2]] = nest[op[2]], nest[op[1]]
        for p in nest[op[1]]:
            pegion[p] = op[1]
        for p in nest[op[2]]:
            pegion[p] = op[2]
    elif op[0]=="3":
        result.append(pegion[op[1]])

print("\n".join(result))