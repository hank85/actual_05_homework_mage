#enconding: utf-8
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    b=1
    while b <= i:
        print(b,'X',i,'=',b*i,' ',end='')
        b+=1
    print()
