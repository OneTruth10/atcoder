N, K = map(int, input().split(" "))
A = [int(x) for x in input().split(" ")]
S = sorted(A)

diff = [i for i in range(N) if A[i] != S[i]]

if not diff:
    print("Yes")
else:
    left = diff[0]
    right = diff[-1]

    if right - left + 1 > K:
        print("No")
    else:
        print("Yes")