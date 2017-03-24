#encoding=utf-8

import random
count=0

#生成随机数
random_num=random.randint(0,100)

#提示用户输入数字
input_num=float(input('请输入一个0～100的数字：'))
#进行数字比较
while count<=5:
    count+=1
    # 对数字范围进行判断：
    while True:
        if input_num < 0:
            print('您输入的数字太小了！')
            input_num = float(input('请输入一个0～100的数字：'))
        elif input_num > 100:
            print('您输入的数字太大了！')
            input_num = float(input('请输入一个0～100的数字：'))
        else:
            break
    if count==5:
        print('还没猜出来？不玩了！')
        break
    if input_num==random_num and count==1:
        print('第一次就猜对了，真厉害！')
        break
    elif input_num>random_num:
        print('猜大了，继续猜吧～')
        input_num = float(input('请输入一个0～100的数字：'))

    elif input_num<random_num:
        print('猜小了，继续猜吧～')
        input_num = float(input('请输入一个0～100的数字：'))

    else:
        print('终于猜对了，恭喜！')
        break
