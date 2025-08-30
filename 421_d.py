Rt, Ct, Ra, Ca = map(int, input().split(" "))
taka = [Rt,Ct]
aoki = [Ra, Ca]
t_move = []
a_move = []
total = 0

n, m, l = map(int, input().split(" "))
for i in range(m):
    s, a = input().split(" ")
    t_move.append((s,int(a)))
for i in range(l):
    t,b = input().split(" ")
    a_move.append((t,int(b)))

t_dir, t_num = t_move.pop(0)
a_dir, a_num = a_move.pop(0)
for i in range(n):
    if t_num<=0:
        t_dir, t_num = t_move.pop(0)
    if a_num<=0:
        a_dir, a_num = a_move.pop(0)
    if t_dir=="U":
        taka[0] = taka[0]-1
    elif t_dir=="D":
        taka[0] = taka[0]+1
    elif t_dir=="R":
        taka[1] = taka[1]+1
    elif t_dir=="L":
        taka[1] = taka[1]-1
    if a_dir=="U":
        aoki[0] = aoki[0]-1
    elif a_dir=="D":
        aoki[0] = aoki[0]+1
    elif a_dir=="R":
        aoki[1] = aoki[1]+1
    elif a_dir=="L":
        aoki[1] = aoki[1]-1
    if taka==aoki:
        total+=1
    t_num-=1
    a_num-=1


print(total)
