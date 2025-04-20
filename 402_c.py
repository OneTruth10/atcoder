n, m = input().split(" ")
n, m = int(n), int(m)
menu = []
for i in range(m):
    temp = input().split(' ')
    menu.append(tuple([temp[0], set(temp[1:])]))
    
b = input().split(" ")

overcome = set()

for ing in b:
    overcome.add(ing)
    count = 0
    for a in menu:
        if int(a[0]) <= len(overcome) and a[1]-overcome==set():
            count += 1
            
    print(count)
            