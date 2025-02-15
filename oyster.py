oysters = input()
takahashi, aoki = oysters.split(' ')


if takahashi=="sick"and aoki=="sick":
    print("1")
elif not(takahashi=="sick" or aoki=="sick"):
    print("4")
elif takahashi=="sick" and aoki=="fine":
    print("2")
else:
    print("3")
