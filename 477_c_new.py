Q = int(input())
S = input()
T = input()
N = len(S)
M = len(T)
has_T = [0]*N

offset = N-M+1
result = []
for i in range(offset):
    if S[i:M+i]==T:
        has_T[i] = 1
pref = [0]*(N+1)
for i in range(N):
    pref[i+1] = pref[i] + has_T[i]
    
    
for _ in range(Q):
    l, r = map(int, input().split(" "))
    left_i = l-1
    right_i = r-M+1
    if right_i>left_i:
        count = pref[right_i]-pref[left_i]
        if count>=1:
            result.append("Yes")
        else:
            result.append("No")
    else:
        result.append("No")
        
print("\n".join(result))