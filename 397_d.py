n = int(input())
result = [-1,-1]
for a in range(int(n**(1/3))):
    print(a)
    for b in range(int(n**(1/3))):
        if (a-b)*(a**2+a*b+b**2)==n:
            result[0] = a
            result[1] = b
            break

if result[0]==-1:
    print("-1")
else:
    print(f"{result[0]} {result[1]}")