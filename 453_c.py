N = int(input())
L = list(map(int, input().split()))

max_cross = 0

for i in range(2**N):
    current_pos = 0.5
    cross_count = 0
    
    for j in range(N):
        if (i >> j) & 1:
            next_pos = current_pos + L[j]
        else:
            next_pos = current_pos - L[j]
        
        if current_pos * next_pos < 0:
            cross_count += 1
            
        current_pos = next_pos
    
    max_cross = max(cross_count, max_cross)

print(max_cross)