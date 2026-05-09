N, K = map(int, input().split(" "))
A = [0 for _ in range(N)]
a_len = [0 for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split(" ")))
    a_len[i] = temp[0]
    A[i] = temp[1:]
    
C = list(map(int, input().split(" ")))
#print(a_len)
b_len = 0
curr = 0
i = 0
while b_len<K:
    curr = b_len
    b_len += a_len[i]*C[i]
    i+=1
    #print(b_len)

temp = (K-curr)%a_len[i-1]

print(A[i-1][temp-1])