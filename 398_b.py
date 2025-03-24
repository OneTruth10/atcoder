a = input().split(' ')

seen = {}
three = False
two = False

for card in a:
    seen[card] = seen.get(card, 0) + 1

for key,  value in seen.items():
    if value>=3:
        if three:
            two = True
        else:
            three = True
    elif value==2:
        two = True

if three and two:
    print("Yes")
else:
    print("No")