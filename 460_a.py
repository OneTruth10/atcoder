n, m = map(int, input().split(" "))
count = 0
while m!=0:
    m = n%m
    count+=1


print(count)