n = input()
s = input()
s = list(s)
n = int(n)
count = 0
ones = []
for i in n:
    if s[i] == "1":
        count+=1
        ones.append(i)



