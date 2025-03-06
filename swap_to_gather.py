n = input()
s = input()
s = list(s)
n = int(n)
count = 0
ones = []
length = 100_000_000_000
for i in range(n):
    if s[i] == "1":
        count+=1
        ones.append(i)

median = ones[len(ones)//2]
result = 0
for i, one in enumerate(ones):
    result+= abs(median-one) - abs(len(ones)//2-i)

print(result)