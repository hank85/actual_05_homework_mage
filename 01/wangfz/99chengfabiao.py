#encoding:utf-8
#打印乘法口诀表
i = 1
while (i <=9 ):
    j = 1
    while j <= i:
        x = i * j
        print(j,'*',i,'=',x,"  ",end=" ")
        j += 1
    print("\n")
    i += 1
