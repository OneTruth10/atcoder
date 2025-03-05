n, q = input().split(' ')
label = {i:i for i in range(1,int(n)+1)}
pegion = {i:i for i in range(1,int(n)+1)}
nest = {i:i for i in range(1,int(n)+1)}
result = []
for i in range(int(q)):
    op = input().split(" ")
    if op[0]=="1":
        pegion[int(op[1])] = label[int(op[2])]
    elif op[0]=="2":
        nest[label[int(op[1])]], nest[label[int(op[2])]] = nest[label[int(op[2])]], nest[label[int(op[1])]]
        label[int(op[1])], label[int(op[2])] = label[int(op[2])], label[int(op[1])]
        
    elif op[0]=="3":
        result.append(str(nest[pegion[int(op[1])]]))

print("\n".join(result))