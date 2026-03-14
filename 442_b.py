volume = 0
playing = False
result = []
Q = int(input())

for _ in range(Q):
    a = int(input())
    if a==1:
        volume+=1
    elif a==2:
        volume = max(volume-1, 0)
    else:
        playing = not playing
    
    if volume>=3 and playing:
        result.append("Yes")
    else:
        result.append("No")

print("\n".join(result))