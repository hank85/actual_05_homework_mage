#encoding:utf-8
#打印乘法口诀表
n = 1
while (n <=9 ):
    x = 1
    while x <= n:
        l = n * x
        print(x,'*',n,'=',l,"  ",end=" ")
        x += 1
    print("\n")
    n += 1
