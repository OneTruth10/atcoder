n, k = map(int, input().split(" "))
a = input().split(" ")
a = map(int, a)
product = 1
for num in a:
    product *= num 
    temp = str(product)
    if len(temp)>k:
        product = 1
        
        
print(product)