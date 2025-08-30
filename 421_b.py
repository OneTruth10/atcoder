x, y = map(int, input().split(" "))


for i in range(8):
    a = x + y
    x = y
    y = int(str(a)[::-1])
    
print(y)