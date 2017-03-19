#encoding: utf-8

#99乘法口诀表
for x in range(1,10):
	print('\t',x,'\t',end = '')
print('\n')

for i in range(1,10):
	print(i,'\t',end = '')
	for j in range(1,i+1):
		print(j,' * ',i,' =', i*j,'\t',end = '')
	print('\n')
