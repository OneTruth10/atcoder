t = int(input())
result = []
for i in range(t):
    a, b, c = map(int, input().split(" "))
    if b>=a or b>=c:
        result.append(min(a,c))
    elif a>=c:
        a -= b
        c -= b
        if a>=2*c:
            result.append(c+b)
        else:
            result.append(b+min((a+c)//3,a,c))

    elif a<c:
        a -= b
        c -= b
        if c>=2*a:
            result.append(a+b)
        else:
            result.append(b+min(((a+c)//3),a ,c))
for r in result:
    print(r)