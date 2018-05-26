import random
secret = random.randint(1, 50)
guess = input("请输入数字：")
j = '0123456789'
z = 1
for k in guess:
    if k not in j:
        print("对不起，你输入的不是一个正整数。")
        break
    elif z == len(guess) and (k in j):
        guess = int(guess)
        while guess != secret:
            if guess > secret:
                guess = int(input("""嘿嘿，猜大了，大了，哥们。
猜猜我心里想的数字是多少："""))
            else:
                guess = int(input("嘿嘿，你猜小了，小了。\n猜猜我心里想的数字是多少："))
        print("""真厉害，你是我心里的蛔虫么？
可惜才对也没有奖！
游戏结束了，不玩了～～～""")
    z += 1