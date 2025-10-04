x, y = input().split(" ")
os = {"Ocelot":1, "Serval":2, "Lynx":3}


if os[x]>=os[y]:
    print("Yes")
else:
    print("No")