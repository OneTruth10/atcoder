s = input()
result = ""
nums = set(["1","2","3","4","5","6","7","8","9","0"])
for i in range(len(s)):
    char = s[i]
    if char in nums:
        result+=char


print(result)