# _*_ coding: utf-8 _*_
import random

input_count = 5
print("这是一个猜数字的游戏,系统随机生成一个数字,根据系统猜出这个数字你有{}次机会".format(input_count))
min_num = 0
max_num = 100
random_num = random.randint(0, 100)
while True:
    if input_count == 0:
        print("太笨了,下次再来,我们的数字是:{}".format(random_num))
        break
    input_num = input("请输入一个{}到{}的数字:".format(min_num, max_num))
    if input_num.isdigit():
        input_num = int(input_num)
        if input_num > max_num or input_num < min_num:
            print("您输入的数字超过了输入范围,请重新输入")
            continue
        input_count -= 1
        if input_num > random_num:
            max_num = input_num
            print("您猜大了,剩余{}次机会".format(input_count))
        if input_num < random_num:
            min_num = input_num
            print("您猜小了,剩余{}次机会".format(input_count))
        if input_num == random_num:
            print("恭喜你猜对了")
            break
    else:
        print("您输入的不是一个数字")

