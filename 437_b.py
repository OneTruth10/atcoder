H, W, N = map(int, input().split(" "))
square = [0]*H
nums = set()
result = 0
for i in range(H):
    temp = set(map(int, input().split(" ")))
    square[i] = temp
    
for _ in range(N):
    nums.add(int(input()))
    
for i in range(H):
    diff = len(nums) - len(nums-square[i])
    result = max(result, diff)
    
    
print(result)