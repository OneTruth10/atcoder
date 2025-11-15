s = input()
letters = {}

for letter in s:
    temp = letters.get(letter, 0)
    letters[letter] = temp + 1
    
for k,v in letters.items():
    if v==1:
        print(k)