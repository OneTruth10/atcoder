N, W = map(int, input().split())
dishes = [list(map(int, input().split())) for _ in range(N)]

max_del = 0

for i in range(2**N):
  total_weight = 0
  total_del = 0
  for j in range(N):
    if (i >> j) & 1:
      total_del += dishes[j][0]
      total_weight += dishes[j][1]

  if total_weight <= W:
    max_del = max(max_del, total_del)

print(max_del)