n, r = map(int, input().split(" "))
l = input().split(" ")
first_zero = False
kaihei = 0
for i in range(r):
    if not first_zero and l[i]=="0":
        first_zero=True

    if first_zero and l[i]=="0":
        kaihei+=1
    elif first_zero and l[i]=="1":
        kaihei+=2
first_zero = False
for i in range(1,n-r+1):
    if not first_zero and l[-i]=="0":
        first_zero = True
    if first_zero and l[-i]=="0":
        kaihei+=1
    elif first_zero and l[-i]=="1":
        kaihei+=2

print(kaihei)