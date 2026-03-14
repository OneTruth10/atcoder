N, X, Y = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
result = ""
possible = True
temp_max = A[0]*Y
temp_min = A[0]*X
pre_min = A[0]*X
pre_max = A[0]*Y
diff = Y-X
for i in A:
    curr_min = i*X
    curr_max = i*Y
    if not (temp_min>curr_max or temp_max<curr_min):
        if (curr_max-temp_max)%diff!=0 or (curr_min-temp_min)%diff!=0:
            result = "-1"
            #print(curr_max-temp_max%diff)
            possible = False
    else:
        result = "-1"
        possible = False
    if not possible:
        break
    temp_max = min(temp_max, (i*Y))
    temp_min = max(temp_min, (i*X))

if result=="-1":
    print(result)
else:
    result = 0
    for i in A:
        a = (i*Y-temp_max)//diff
        b = i-a
        result+=b
    print(result)