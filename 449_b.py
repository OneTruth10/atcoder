H, W, Q = map(int, input().split(" "))
result = []
for _ in range(Q):
    q, num = map(int, input().split(" "))
    if q==1:
        result.append(num*W)
        H-=num
    else:
        result.append(num*H)
        W-=num

for r in result:
    print(r)