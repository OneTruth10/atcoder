i, j = map(int, input().split("-"))

if j<8:
    j += 1
elif i<8 and j==8:
    j = 1
    i += 1
else:
    i = 8
    j = 8

print(f"{i}-{j}")