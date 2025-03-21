result = 0

i = 1
while 1359*i<100_000_000:
    temp = str(1359*i)
    result += int(temp[-4])
    i+=1
    
    
print(result)