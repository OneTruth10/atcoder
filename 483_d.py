N = int(input())
A = list(map(int, input().split(" ")))
pos = 0
neg = 0
max_neg = 0
max_pos = 0
for a in A:
    if a<0:
        neg += abs(a)
        max_neg = max(max_neg, abs(a))
    else:
        pos += a
        max_pos = max(max_pos, a)
        
    
temp = abs(pos-neg)
result = max(temp, abs((pos-max_pos)-(neg+max_pos)), abs((pos+max_neg)-(neg-max_neg))) + 1

print(result)