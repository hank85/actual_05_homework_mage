#!/usr/local/bin/python3
# 99cfb 三种方法

for i in range(1,10): 
    for j in range(1,1+i):
        print(str(j) + "*" + str(i) + "=" + str(i*j), end="")
    print() 
 
for i in range(1,10): 
   for j in range(1,i+1):
       print("%d*%d=%2d" % (i,j,i*j), end ="")
   print()
     
print ('\n'.join([''.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
