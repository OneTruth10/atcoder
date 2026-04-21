l,r,d,u = map(int, input().split(" "))
result = 0


#|x|>|y|
for x in range(l,r+1):
    if x%2==0:
        upper = min(abs(x)-1, u)
        lower = max(-abs(x)+1, d)
        temp = max(0, upper-lower+1)
        result += temp
       
#|x|<=|y|
for y in range(d,u+1):
    if y%2==0:
        right = min(abs(y), r)
        left = max(-abs(y), l)
        temp = max(0, right-left+1)
        result += temp
        
print(result)
    