n = int(input())
s = list(map(int, input().split(" ")))
distances = []
past = 0
max_distance = 10**9 + 1
for dis in s:
    distances.append(dis-past)
    past = dis
    
for i in range(1, len(s)-1):
    