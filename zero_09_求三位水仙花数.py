i = 0
j = 0
k = 0
z = 1
while i < 10:
    j = 0
    k = 0
    while j < 10:
        k = 0
        while k < 10:
            z = i * 100 + j * 10 + k
            if z == i**3 + j**3 + k**3 and z > 1:
                z = i*100 + j*10 + k
                print(z)
            k += 1
        j += 1
    i += 1

