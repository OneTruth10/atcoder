n = int(input())
rooms = []
for i in range(n):
    rooms.append(input())

x, y = input().split(" ")

if rooms[int(x)-1]==y:
    print("Yes")
else:
    print("No")