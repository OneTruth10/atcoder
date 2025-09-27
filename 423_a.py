x, c = map(int, input().split(" "))


max_w = x/(1+c/1000)
max_w = int((max_w//1000)*1000)
print(max_w)