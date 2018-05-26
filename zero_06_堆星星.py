i = 1
k = 1
j = int(input("请输入层数："))
while i <= j:
    k = i
    while (j-k) > 0:
        print(" ", end="")
        k += 1
    k = i
    while k > 0:
        print("* ", end="")
        k -= 1
    print("")
    i += 1