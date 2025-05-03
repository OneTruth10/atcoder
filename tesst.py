def exformat(t, s=0):
    print(f"{t}, type:{type(t)}")
    if type(t)!=type(()):
        return str(t)
    op, vals = t[0], t[1:]
    op = (" "*s) + op + (" "*s)
    joined = op.join([exformat(v, s) for v in vals])
    print(joined)
    return "({joined})".format(joined=joined)

print(exformat(('+', ('*', 1, 2), ('-', 2, 4, 6), 4), 1))