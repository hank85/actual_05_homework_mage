#encoding:utf-8
#打印乘法口诀表
n = 1
while (n <=9 ):
    s = 1
    while s <= n:
        l = s * n
        print(s,'*',n,'=',l,"  ",end=" ")
        s += 1
    print("\n")
    n += 1
