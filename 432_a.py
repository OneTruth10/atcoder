nums = list(map(int, input().split(" ")))

first = max(nums)
nums.remove(first)
second = max(nums)
nums.remove(second)
third = max(nums)

print(f"{first}{second}{third}")