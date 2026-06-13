s = input()
last = len(s)-1
s_pos = []
count = 0

for i in range(len(s)):
    if s[i]=="C":
        s_pos.append(i)
        
for index_s in s_pos:
    count+=1
    entend = min(last-index_s, index_s)
    count+=entend

print(count)