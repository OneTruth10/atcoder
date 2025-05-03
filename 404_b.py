def rotate(grid, t):
    temp = list(zip(*grid[::-1]))
    return temp, check_difference(temp,t)
    
def check_difference(s,t):
    count = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                count+=1
    return count
            


n = input()
n = int(n)
s = [None for i in range(n)]
t = [None for i in range(n)]

for i in range(n):
    s[i] = list(input())
    
for i in range(n):
    t[i] = list(input())

no_rot = check_difference(s,t)
once = rotate(s,t)
twice = rotate(once[0],t)
triple = rotate(twice[0],t)

print(min(no_rot, once[1]+1, twice[1]+2, triple[1]+3))