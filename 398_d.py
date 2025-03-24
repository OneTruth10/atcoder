nrc = input().split()
n, r, c = map(int, nrc)
s = list(input())
smoke = set([(0,0)])
for i in range(n):
    if s[i]=="N":
        for pos in smoke:
            smoke.remove(pos)
            temp.add((pos[0]-1,pos[1]))
        smoke.update(temp)
        smoke.add((0,0))
        if (r,c) in smoke:
            print("1",end="")
        else:
            print("0",end="")
    elif s[i]=="S":
        temp = set()
        for pos in smoke:
            smoke.remove(pos)
            temp.add((pos[0]+1,pos[1]))
        smoke.update(temp)
        smoke.add((0,0))
        if (r,c) in smoke:
            print("1",end="")
        else:
            print("0",end="")
    elif s[i]=="E":
        temp = set()
        for pos in smoke:
            smoke.remove(pos)
            temp.add((pos[0],pos[1]+1))
        smoke.update(temp)
        smoke.add((0,0))
        if (r,c) in smoke:
            print("1",end="")
        else:
            print("0",end="")
    elif s[i]=="W":
        for pos in smoke:
            smoke.remove(pos)
            temp.add((pos[0],pos[1]-1))
        smoke.update(temp)
        smoke.add((0,0))
        if (r,c) in smoke:
            print("1",end="")
        else:
            print("0",end="")