Q = int(input())
S = input()
T = input()

for j in range(Q):
    l, r = map(int, input().split(" "))
    sub_s = S[l-1:r]
    #print(sub_s)
    if len(sub_s)>=len(T):
        found = False
        offset = len(sub_s)-len(T)+1
        for i in range(offset):
            #print(sub_s[i:len(T)+i])
            if sub_s[i:len(T)+i]==T:
                found = True
                break
        if found:
            print("Yes")
        else:
            print("No")
    else:
        print("No")