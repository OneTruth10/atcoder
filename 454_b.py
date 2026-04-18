N, M = map(int, input().split(" "))
F = set(input().split(" "))
result = ""

if len(F)==N:
    result += "Yes"
else:
    result += "No"
result += "\n"

if len(F)==M:
    result += "Yes"
else:
    result += "No"

print(result)