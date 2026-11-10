N, M = map(int, input().split(" "))
first_pick = [0]*N
for _ in range(M):
    A, B = map(int, input().split(" "))
    first_pick[A-1]+=1