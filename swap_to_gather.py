n = input()
s = input()
s = list(s)
n = int(n)
left = 0
longest = 0
curr = 0
con = False
for i in range(n):
    if s[i]=="1" and not con:
        con = True
        curr = i
    elif s[i]=="0" and con:
        con = False
        if longest < i-curr:
            longest = i-curr
            left = curr


print(f"{longest}, starting from: {left}")
