x, y = map(int, input().split(' '))

x += y
if x%12==0:
    print("12")
else:
    print(x%12)