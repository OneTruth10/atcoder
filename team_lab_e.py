count = 0
temp = 0
car = []
for i in range(500, 0, -1):   
    if temp+i <= 5000:
        temp += i
        car.append(i)
    else:
        count +=1
        temp = i
        print(sum(car))
        car = []
        
print(sum([i for i in range(50)]))
print(count)