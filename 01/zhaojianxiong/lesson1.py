import random
# encoding: utf-8
print('99乘法表')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    if i - 1 > 0:
        print(i, '*', i, '=', i * i, end=' ')
    else:
        print(i, '*', i, '=', i * i)
    m = i
    while m > 1:
        m = m - 1
        if m == 1:
            print(i, '*', m, '=', i * m)
        else:
            print(i, '*', m, '=', i * m, end=' ')


print('Guess Number')
i = 1
random_num = random.randint(0, 100)
while i <= 5:
    number = int(input('Please input a number:'))
    if number < random_num:
        print('Guess small')
    elif number > random_num:
        print('Guess big')
    elif number == random_num:
        print('Guess right')
    i += 1
print('Too stupid')
