N = int(input())
A = list(map(int, input().split(" ")))
pos = 0
neg = 0
max_neg = 0
max_pos = 0
pos_distance = 0
neg_distance = 0
for a in A:
    if a<0:
        neg += abs(a)
        max_neg = max(max_neg, abs(a))
    else:
        pos += a
        max_pos = max(max_pos, a)
        
    
temp = abs(pos-neg)
max_distance = max(temp, abs((pos-max_pos)-(neg+max_pos)), abs((pos+max_neg)-(neg-max_neg)))
if temp==max_distance:
    for a in A:
        




result =  + 1

print(result)