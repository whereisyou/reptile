def sum_zero():
    """0到100求和"""

    zero = 0
    sum1 = 0
    while zero < 100:
        zero += 1
        sum1 += zero
    print(sum1)


def factorial_zero():
    """求任意数的阶乘"""

    number = float(input("请输入数字："))
    i = 1
    sum2 = 1
    if number > 0 and number%1==0:
        while i < number+1:
            sum2 *= i
            print(i, end="")
            if i == number:
                i += 1
                continue
            print("*", end="")
            i += 1
        print("=", end="")
        print(sum2)
    else:
        print("对不起，你输入的不是一个正整数")


factorial_zero()
