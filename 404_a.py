s = input()

s = set(list(s))

alp = set(list("abcdefghijklmnopqrstuvwxyz"))

remaining = alp.difference(s)

for rem in remaining:
    print(rem)
    break