n = int(input())
result = ""
length = 0


if n%2==0:
    half = (n-2)//2
    result += "-"*half + "==" + "-"*half
else:
    half = (n-1)//2
    result += "-"*half + "=" + "-"*half
print(result)
