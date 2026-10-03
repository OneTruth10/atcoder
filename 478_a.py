N, M = map(int, input().split(" "))

result = [M//N+1]*(M%N) + [M//N]*(N-M%N)
#print(result)
print("\n".join(list(map(str, result))))