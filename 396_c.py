n = map(int, input().split(' '))
b = map(int,input().split(' '))
w = map(int, input().split(' '))

b_sum = []
b_max = -100_000_000_000

w_sum = []

for num in b:
    b_max = max(b_max, num)
    if num>=0:
        b_sum.append(num)

if len(b_sum)==0:
    b_sum.append(b_max)

w_min = 10000000000
for num in w:
    if num>=0:
        if len(w_sum)<=len(b_sum):
            w_min = min(w_min,num)
            w_sum.append(num)
        else:
            w_sum.append(num)
            w_min = min(w_min, num)
            w_sum.remove(w_min)

print(sum(b_sum)+sum(w_sum))