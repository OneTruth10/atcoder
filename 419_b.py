n = int(input())
bag = []
result = []
for i in range(n):
    q = input().split(' ')
    if q[0]=="1":
        bag.append(int(q[1]))
    elif q[0]=="2":
        result.append(min(bag))
        bag.remove(min(bag))


print("\n".join(map(str, result)))