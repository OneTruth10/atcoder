n = int(input())
s = input()
b_pos = []
a_pos = []
total_diff1 = 0
total_diff2 = 0

for i in range(n*2):
    if s[i]=="B":
        b_pos.append(i)
    else:
        a_pos.append(i)
#print(b_pos)
x = 1
for b in b_pos:
    total_diff1+= abs(b-x)
    x+=2
x = 0
for b in b_pos:
    total_diff2+= abs(b-x)
    x+=2


print(min(total_diff2,total_diff1))