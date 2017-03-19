#enconding: utf-8
for i in range(10):
    b=1
    while b <= i:
        print('{}X{}{}{:<4}'.format(b,i,'=',b*i),end='')
        b+=1
    print()
