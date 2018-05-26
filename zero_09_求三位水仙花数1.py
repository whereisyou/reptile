i = 2
while i < 1000:
    j = i//100
    k = i//10 - 10*j
    z = i - 100*j - 10*k
    if i == (z**3 + j**3 + k**3):
        print(i)
    i += 1