first = input()
first = first.split()
num, x = int(first[0]), int(first[1])
foods = []
for i in range(num):
    temp = input()
    temp = temp.split()
    for i,elt in enumerate(temp):
        temp[i] = int(elt)
    foods.append(temp)

under = []

for i in range(num):
    vitamins = {1:0, 2:0, 3:0}
    temp = [foods[i]]
    current_cal = foods[i][2]
    for j in range(i+1, num):
        if current_cal+foods[j][2]<x:
            current_cal += foods[j][2]
            temp.append(foods[j])
    #print(temp)
    for elt in temp:
        vitamins[elt[0]] = vitamins[elt[0]] +elt[1]
    print(vitamins)
    under.append(min(vitamins.values()))


print(under)