N, M, K = map(int, input().split(" "))
A = [0] + list(map(int, input().split(" ")))

pref_a = [0] + [A[i]+A[i-1] for i in range(1,N+1)]
result = []
for i in range(1,N+1):
    if pref_a[i]-pref_a[max(i-M, 0)]<=K:
        result.append("Yes")
        #print("Yes")
    else:
        result.append("No")
        #print("No")
        
print("\n".join(result))