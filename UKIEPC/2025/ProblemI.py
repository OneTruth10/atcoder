import math
num = int(input())
b = 1
while 2**b-1 < num:
    b*=2
    
print(f"{b} bits" if b!=1 else f"{b} bit")