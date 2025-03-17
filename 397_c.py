n = int(input())
a = input().split(' ')

left_distinct = [0]*n
right_distinct = [0]*n

left_set = set()
right_set = set()

max_distinct = 0

for i in range(n):
    left_set.add(a[i])
    left_distinct[i] = len(left_set)

for i in range(n-1, 0, -1):
    right_set.add(a[i])
    right_distinct[i] = len(right_set)

for i in range(n):
    max_distinct = max(left_distinct[i-1]+right_distinct[i], max_distinct)

print(max_distinct)