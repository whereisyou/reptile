def postcard():
    name = input()
    age = int(input())
    print('我叫%s，我%d岁。' % (name, age))


def primeNumber(number):
    # 输出0到任意数之间质数
    k = ()
    if number > 1 and number % 1 == 0:
        j = 1
        k += (j,)
        '''
        print(j,end=" ")
        '''
        while j <= number:
            i = 2
            while i < j and j % i != 0:
                i += 1
            if i ==j:
                k += (j,)
                '''
                print(j,end=" ")
                '''
            j += 1
    else:
        print("请输入一个正整数！")
    return k


number = float(input("请输入数字："))
print(primeNumber(number))