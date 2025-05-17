n = input().split(' ')


if int(n[0])>int(n[2]):
    print("Yes")
elif int(n[0])==int(n[2]) and int(n[1])>=int(n[3]):
    print("Yes")
else:
    print("No")