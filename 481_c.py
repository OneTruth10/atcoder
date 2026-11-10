Q = int(input())
result = []
account = {}
num = 1
for _ in range(Q):
    s = input()
    temp = account.get(s, 0)
    if temp==0:
        account[s] = num
        result.append(str(num))
        num += 1
    else:
        result.append(str(temp))
        
print("\n".join(result))