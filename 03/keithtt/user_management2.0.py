#encoding: utf-8

users = []
user_info_dict = '|{0:^20}|{1:^10}|{2:^20}|'
user_info_header = user_info_dict.format('name','age','tel')

while True:
	action = input('Please input(add/delete/find/update/list/exit): ')
	if action == 'add':
		useradd = input('请按格式输入信息  用户名:年龄:联系方式  ').strip()
		name = useradd.split(':')[0]
		age = useradd.split(':')[1]
		tel = useradd.split(':')[2]
		is_exists=False
		for user in users:
			if name == user['name']:
				print('用户已存在')
				is_exists=True
				break
		if not is_exists:
			users.append({'name':name,'age':age,'tel':tel})
			print('添加用户成功')
			print(users)		
	elif action == 'delete':
		name = input('请输入要删除的用户名：')
		is_exists = False
		for user in users:
			if name == user['name']:
				is_exists=True
				users.remove(user)
				print('删除用户成功')
				break
		if not is_exists:
			print('用户不存在')
		print(users)			
	elif action == 'update':
		userupdate = input('请按格式输入信息  用户名:年龄:联系方式  ').strip()
		name = userupdate.split(':')[0]
		age = userupdate.split(':')[1]
		tel = userupdate.split(':')[2]
		is_exists = False
		for user in users:
			if name == user['name']:
				is_exists=True
				user.update({'name':name,'age':age,'tel':tel})
				print('更新用户成功.')
				break		
		if not is_exists:
			print('用户不存在')	
		print(users)			
	elif action == 'find':
		name = input('请输入要查找的用户名：')
		is_exists=False
		print(user_info_header)
		for user in users:
			if name == user['name']:
				is_exists=True
				print(user_info_dict.format(user['name'],user['age'],user['tel']))
		if not is_exists:
			print('用户不存在')		
			print(users)
	elif action == 'list':
		print(user_info_header)
		for user in users:
			print(user_info_dict.format(user['name'],user['age'],user['tel']))
	elif action == 'exit':
		print('退出程序')
		break
	else:
		print('输入错误')
