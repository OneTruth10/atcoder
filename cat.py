n = input()
n = int(n)
result = [""]*50
for i in range(n):
    temp = input()
    result[len(temp)-1]=temp

print("".join(result))