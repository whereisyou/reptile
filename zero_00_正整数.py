def number_int(i):
    j = '0123456789'
    z = 1
    for k in i:
        if k not in j:
            k = False
            break
        elif z == len(i) and (k in j):
            k = True
        z += 1
    return k