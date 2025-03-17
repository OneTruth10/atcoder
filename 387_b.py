x = int(input())

curr = 1
i = 2

while i<x:
    curr = curr * i
    #print(fac)
    if curr == x:
        print(i)
        break
    i+=1