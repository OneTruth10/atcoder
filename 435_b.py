N = int(input())
a = list(map(int, input().split()))
cum_a = [0] * (N + 1)

for i in range(N):
    cum_a[i + 1] = cum_a[i] + a[i]

result = 0

for l in range(N):
    for r in range(l, N):
        subarray_sum = cum_a[r + 1] - cum_a[l]
        valid = True
        
        for i in range(l, r + 1):
            if subarray_sum % a[i] == 0:
                valid = False
                break
        
        if valid:
            result += 1

print(result)