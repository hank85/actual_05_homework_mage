#encoding: utf-8

i = 1
k = 1
for i in range(1,10):
    for k in range(1,i+1):
        print(i,'*',k,"=",k*i,"\t",end='')
        k += 1
    print()
while i <= 9:
    while k <= i:
        print(i, '*', k, "=", k * i, "\t", end='')
        k += 1
        print ()
        k = 1
        i += 1
