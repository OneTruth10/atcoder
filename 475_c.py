from bisect import bisect_right

N, S, L = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
left_pref = [0]
right_pref = [0]

for i in range(S-1, N-1):
    right_pref.append(right_pref[-1]+A[i])
    
for i in range(S-2, -1, -1):
    left_pref.append(left_pref[-1]+A[i])
    
    
#print(right_pref)
#print(left_pref)

max_town = 0

for i in range(1, len(right_pref)):
    if right_pref[i]>L:
        break
    if right_pref[i]*2>L:
        max_town = max(max_town, i)
        continue
    rem = L - right_pref[i]*2
    additional = bisect_right(left_pref, rem) - 1
    max_town = max(max_town, i+additional)
    
for i in range(1, len(left_pref)):
    if left_pref[i]>L:
            break
    if left_pref[i]*2>L:
        max_town = max(max_town, i)
        continue
    rem = L - left_pref[i]*2
    additional = bisect_right(right_pref, rem) - 1
    max_town = max(max_town, i+additional)
print(max_town+1)
    