count = 0

for i in range(10_000, 100_000):
    if 1487369520%i==0:
        count += 1
        
print(count)