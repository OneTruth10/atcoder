X = list(input())
X = list(map(int, X))
nums = {}
for x in X:
    temp = nums.get(x, 0)
    temp+=1
    nums[x] = temp
result = ""
key = set(nums.keys())
for i in range(len(key)):
    temp = min(key)
    if temp==0:
        key.remove(0)
        temp = min(key)
        result = str(temp) + "0"*nums[0]
        nums[temp]-=1
    else:
        temp = min(key)
        result += str(temp)*nums[temp]
        key.remove(temp)
print(result)
