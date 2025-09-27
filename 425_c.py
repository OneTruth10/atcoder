n, q = map(int, input().split(" "))
a = list(map(int, input().split(' ')))
sum_list = [0 for i in range(n+1)]
s = 0
offset = 0
moved = 0
result = []
for i in range(len(a)):
    s += a[i]
    sum_list[i+1] = s
#print(sum_list)
for i in range(q):
    query = list(map(int, input().split(" ")))
    if query[0]==1:
        c = query[1]
        if c+moved>=n:
            moved = c + moved - n
        else:
            moved+=c
        offset = sum_list[moved]
    elif query[0]==2:
        l, r = query[1], query[2]
        temp = 0
        if len(sum_list)-moved<=r:
            temp += sum_list[-1]
            temp += sum_list[r+moved-n]
            #temp -= offset
            temp -= sum_list[l+moved-1]
        else:
            temp-=sum_list[moved+l-1]
            temp+=sum_list[moved+r]
        result.append(str(temp))
        
print("\n".join(result))
