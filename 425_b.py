n = int(input())
a = input().split(" ")
a = map(int, a)
p_hold = True
nums = {i:0 for i in range(1,n+1)}
result = [-1 for i in range(n)]
unseen = set([i for i in range(1,n+1)])
#print(unseen)
for i,elt in enumerate(a):
    if elt!=-1:
        nums[elt] = nums[elt]+1
        result[i] = elt
        if nums[elt]>=2:
            p_hold = False
            break
        unseen.remove(elt)

if p_hold:
    print("Yes")
    for i in unseen:
        for j in range(len(result)):
            if result[j]==-1:
                result[j]=i
                break
    print(" ".join(map(str, result)))
else:
    print("No")