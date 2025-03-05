n = input()
s = input().split(' ')

for i in range(int(n)-1):
    if int(s[i])>=int(s[i+1]):
        print("No")
        break
    elif i==int(n)-2:
        print("Yes")


