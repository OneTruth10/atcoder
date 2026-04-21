n = int(input())
s = input()
result = ""
head = True

for i in range(n):
    if head:
        if s[i]!="o":
            result+=s[i]
            head = False
    else:
        result += s[i]

print(result)            
        