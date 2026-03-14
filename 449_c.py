import string

N, L, R = map(int, input().split())
S = input()
result = 0
alphabet = {c: [] for c in string.ascii_lowercase}
for i, ch in enumerate(S):
    alphabet[ch].append(i)

for pos in alphabet.values():
    m = len(pos)
    if m < 2:
        continue
    
    left = 0
    right = 0
    
    for i in range(m):

        while left < m and pos[left] < pos[i] + L:
            left += 1
        
        while right < m and pos[right] <= pos[i] + R:
            right += 1

        valid_left = max(left, i + 1)
        if valid_left < right:
            result += (right - valid_left)

print(result)