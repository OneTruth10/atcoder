n, m = map(int, input().split(' '))
votes = []
score = {i:0 for i in range(n+1)}
for i in range(n):
    votes.append(input())


for i in range(m):
    one = 0
    zero = 0
    group_zero = set()
    group_one = set()
    for j in range(n):
        if votes[j][i]=="0":
            zero+=1
            group_zero.add(j)
        else:
            one+=1
            group_one.add(j)

    if zero>one:
        for minority in group_one:
            score[minority] = score[minority] + 1
    else:
        for minority in group_zero:
            score[minority] = score[minority] + 1

print(dict(sorted(score.items(), key=lambda item: item[1], reverse=True)))