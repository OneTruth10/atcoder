N = int(input())
colour = list(map(int, input().split(" ")))
freq = {i:0 for i in range(1,N+1)}
for c in colour:
    freq[c] += 1

print(N-max(freq.values()))