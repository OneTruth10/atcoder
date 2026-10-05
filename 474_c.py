N, Q = map(int, input().split(" "))
P = list(map(int, input().split(" ")))
num_pos = {P[i]:i for i in range(len(P))}
last = len(P)
for _ in range(Q):
    a = int(input())
    num_pos[a] = last
    last += 1
    

asc = {str(k): v for k, v in sorted(num_pos.items(), key=lambda item: item[1])}
print(" ".join(asc.keys()))