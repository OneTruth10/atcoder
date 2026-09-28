n, m = map(int, input().split(" "))
col_freq = {}
colours = set()
timing = {}
for i in range(n):
    a, d, b = map(int, input().split(" "))
    colours.add(a)
    col_freq[a] = col_freq.get(a, 0) + 1
    temp = timing.get(d, [])
    temp.append((a,b))
    timing[d] = temp
    
for j in range(1, m+1):
    change = timing.get(j, -1)
    if change!=-1:
        for a,b in timing[j]:
            colours.add(b)
            col_freq[a]-=1
            col_freq[b] = col_freq.get(b, 0) + 1 
            if col_freq[a]==0:
                colours.remove(a)
    print(len(colours))