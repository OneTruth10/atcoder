N = int(input())
a = list(map(int, input().split(" ")))

result = 0

for i in range(len(a)):
    if i%2==0:
        result += a[i]
        
print(result)