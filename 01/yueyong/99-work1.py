#encoding: utf-8
#打印九九乘法口诀
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i * j,'\t',end='')
    print()


