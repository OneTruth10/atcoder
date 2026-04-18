def simplest_form(x):
    stack = []
    reduce = ['(','x','x',')']
    for char in x:
        stack.append(char)
        if len(stack)>=4:
            if stack[-4:]==reduce:
                for _ in range(4):
                    stack.pop()
                stack.append('x')
                stack.append('x')
    return "".join(stack)


T = int(input())
result = []

for _ in range(T):
    a = input()
    b = input()
    if simplest_form(a)==simplest_form(b):
        result.append("Yes")
    else:
        result.append("No")

print("\n".join(result))