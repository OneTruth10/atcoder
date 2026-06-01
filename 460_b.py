t = int(input())
result = []
for _ in range(t):
    xa, ya, ra, xb, yb, rb = map(int, input().split(" "))
    dis_between = ((xa-xb)**2+(ya-yb)**2)
    max_dis = (ra + rb)**2
    min_dis = (ra - rb)**2
    #print(max_dis, dis_between)
    if max_dis >= dis_between >= min_dis:    result.append("Yes")
    else:   result.append("No")

print("\n".join(result))