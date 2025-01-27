length = input()
sequence = input()
sequence = sequence.split()
geo = True
for i, elt in enumerate(sequence):
    sequence[i] = float(elt)

ratio = sequence[1]/sequence[0]
for i in range(int(length)):
    if i>0 and sequence[i]!=sequence[i-1]*ratio:
        geo = False
        break

if geo:
    print("Yes")
else:
    print("No")