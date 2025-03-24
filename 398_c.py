n = int(input())
a = input().split(' ')
seen = {}
result = -1
max_num = 0
for i, person in enumerate(a):
    temp = seen.get(person, [])
    temp.append(i)
    seen[person] = temp

#print(seen)
for key, value in seen.items():
    if len(value)==1:
        if int(key)==max(int(key), max_num):
            result = value[0]+1
            max_num = int(key)


print(result)
