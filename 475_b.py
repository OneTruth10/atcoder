import math

N = int(input())
A = list(map(int, input().split(" ")))
hundred = 0
ten = 0
one = 0
for i in range(N):
    rem = math.ceil(A[i]/1000)*1000-A[i]
    #print(rem)
    temp = rem//100
    rem -= temp*100
    hundred += temp
    temp = rem//10
    rem -= temp*10
    ten += temp
    one += rem
    
print(one, ten, hundred)