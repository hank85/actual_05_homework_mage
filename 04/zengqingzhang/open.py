#encoding:utf-8
path='kk.txt'
#打开文件
fhandler =open(path)
#读取文件
while  True:
	cxt= fhandler.read()
	#cxt=fhandler.readline(2)
	if cxt=='':
		break
print(cxt)
#关闭文件
#fhandler.close(path)