######################99乘法表
m=1
n=1
while(m<10):
    while(n<10):
        if m==1 & n==1:
            print("%2d * %2d = %2d\t" % (m, n, m * n))
            break
        elif n < m:
            print("%2d * %2d = %2d\t" %(n,m,m*n),end="")
            n += 1
            continue
        else:
            print("%2d * %2d = %2d" % (n, m, m * n))
            n += 1
            break
    m += 1
    n=1




###################################################c猜数字游戏
import random
x = random.randint(0,100)
#the number you set to gess
i=1
n=5
while(i<=5):
    print("@_@:")
    print(n,end="")
    print(" times left")
    y = input("please input the number you guess:")
    y = int(y)
    if(y == x):
        print("@_@:")
        print("you win")
        break
    elif(y > x):
        print("@_@:")
        print("the number you guess is a little bigger")
    elif(y < x):
        print("@_@:")
        print("the number you guess is a little less")
    i = i + 1
    n = n - 1
else:
    print("@_@:")
    print("times use up,you lose")
