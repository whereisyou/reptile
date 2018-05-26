number = float(input("请输入数值："))
if number > 1 and number % 1 ==0:
    j = 1
    print(j,end=" ")
    for j in range(1, int(number+1)):
        i = 2
        while i < j and j % i != 0:
            i += 1
        if i == j:
            print(j, end=" ")
else:
    print("请输入一个正整数！")