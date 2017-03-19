#encoding: utf-8
i =1
j=1
for i in range(1,10):
    for j in range(1,i+1):
        print (i,'X',j,'=',i*j,'\t',end='')
    print()
[root@localhost pywork]# cat work2.py
#encoding: utf-8
import random
random_num=random.randint(0,100)
num_put=input('请输入一个1到100之间的数字:')
num_count=0
while True:
    if not num_put.strip().isdigit():
        num_put=input('只能输入数字!')
        continue
    else:
        num_count+=1
    num_put=int(num_put)
    if num_put>random_num:
        print('输入大了！')
    elif num_put<random_num:
        print('输入小了！')
    elif num_put==random_num:
        print('输入对了！')
    if num_count==5:
        print('你已经没有机会了！')
        break
    else:
        num_put=input('请输入1个1～100之间的数字！')
