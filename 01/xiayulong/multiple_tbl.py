# encoding: utf-8
right = 1


while right < 10:
    left = 1
    while left <= right:
        print(left,"*",right,"=",'%-2d' % (left*right),sep="",end=" ")
        left += 1
    print()
    right += 1