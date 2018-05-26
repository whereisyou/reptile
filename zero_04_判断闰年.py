def check_week():
    week = int(input("今天周几："))
    if 1 < week < 8:
        if week < 6:
            print("今天是%d，今天是上班日，还要加班" % week)
        else:
            print("今天是周末，可以休息哟")
    else:
        print("你输入错误。")
# 判断任意年份是否为闰年
def leap_year():
    year = int(input("请输入年份："))
    if year > 0:
        if (year % 4 == 0 and year % 100 != 0) or year%400==0:
            print("这是闰年")
        else:
            print("这不是闰年")
    else:
        print("这不是一个有效的年份")