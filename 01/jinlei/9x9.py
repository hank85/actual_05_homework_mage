#encoding: utf-8
n=1
m=1
for n in range(1,10):
    for m in range(1,n+1):
        print (n,'X',m,'=',n*m,'\t',end='')
    print()
