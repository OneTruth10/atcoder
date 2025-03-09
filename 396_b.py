n = int(input())
stack = ["0"]*100
result = []
for i in range(n):
    q = input().split(' ')
    if q[0]=="1":
        stack.append(q[1])
    else:
        result.append(stack.pop())


print("\n".join(result))