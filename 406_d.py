h, w, n = map(int, input().split(' '))
x = {i:set() for i in range(1,h+1)}
y = {i:set() for i in range(1,w+1)}
result = []

for i in range(n):
    Xi, Yi = map(int, input().split(' '))
    temp = x.get(Xi, set())
    temp.add(Yi)
    x[Xi] = temp
    temp = y.get(Yi, set())
    temp.add(Xi)
    y[Yi] = temp
#print(x)
#print(y)
q = int(input())
removed_x = {}
removed_y = {}
for i in range(q):
    t, pos = map(int, input().split(' '))
    if t == 1:
        result.append(len(x[pos]-removed_y.get(pos, set())))
        for elt in x[pos]:
            temp = removed_x.get(elt, set())
            temp.add(pos)
            removed_x[elt] = temp
        x[pos] = set()
    elif t == 2:
        #print(removed_x)
        result.append(len(y[pos]-removed_x.get(pos, set())))
        for elt in y[pos]:
            temp = removed_y.get(elt, set())
            temp.add(pos)
            removed_y[elt] = temp
        y[pos] = set()
        
        
for r in result:
    print(r)