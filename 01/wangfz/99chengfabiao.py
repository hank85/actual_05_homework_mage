#encoding:utf-8
#打印乘法口诀表
i = 1
while (i <=9):
    j = 1
    while j <= i:
        x = j * i
        print(i,'*',j,'=',x,"\t",end=" ")
        i += 1
    print("\n")
    j += 1