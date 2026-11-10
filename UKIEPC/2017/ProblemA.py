def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i
N = int(input())
max_day = 0
found = False
planet_days = []
common_multiple = 1
result = "IMPOSSIBLE"
for _ in range(N):
    h, r, t = map(int, input().split(" "))
    max_day = max(h, max_day)
    planet_days.append((h,r,t))
    common_multiple = LCM(common_multiple, h)
common_multiple = min(common_multiple, 1825)
imos_sunset = [0]*(max_day*common_multiple)
for h,r,t in planet_days:
    if r<t:
        imos_sunset[0]+=1
        imos_sunset[r]-=1
        for i in range(t, h, len(imos_sunset)-(h-t+r)):
            imos_sunset[i]+=1
            imos_sunset[i+h-t+r]

pref_sunset = [0]
for i, num in enumerate(imos_sunset):
    temp = pref_sunset[-1] + num
    if temp==N:
        found = True
        result = str(i)
        break
    pref_sunset.append(temp)

print(len(imos_sunset))
print(pref_sunset)
print(result)