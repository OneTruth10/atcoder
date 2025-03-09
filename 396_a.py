n = int(input())
a = input().split(' ')

for i in range(n-2):
    if a[i]==a[i+1] and a[i+1]==a[i+2]:
        print("Yes")
        break
    elif i == n-3:
        print("No")