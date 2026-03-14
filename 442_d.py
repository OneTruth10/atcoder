def updatebit(arr, n, i, v):
    i+=1
    while i<=n:
        arr[i]+=v
        i += i & (-i)


def construcBIT(arr, n):
    BITtree = [0]*(n+1)
    for i in range(n):
        updatebit(BITtree, n, i, arr[i])

    return BITtree

def getSum(arr, i):
    s = 0
    i = i + 1
    while i>0:
        s+=arr[i]
        i -= i & (-i)
    return s



result = []
N, Q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
fenTree = construcBIT(a, N)
for _ in range(Q):
    q = tuple(map(int, input().split(" ")))
    if q[0]==1:
        x = q[1]
        updatebit(fenTree, N+1, x-1, a[x]-a[x-1])
        updatebit(fenTree, N+1, x, a[x-1]-a[x])
        a[x], a[x-1] = a[x-1], a[x]
    else:
        l = q[1]
        r = q[2]
        if q[1]==1:
            print(getSum(fenTree, q[2]-1))
            #result.append(getSum(fenTree, q[2]-1))
        else:    
            print(getSum(fenTree, q[2]-1)-getSum(fenTree, q[1]-2))
            #result.append(getSum(fenTree, q[2]-1)-getSum(fenTree, q[1]-2))

#for i in result:
 #   print(i)