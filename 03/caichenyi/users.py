# encoding: utf-8
# Author: Cai Chenyi
users = []
tpl = '|{:>10}|{:>5}|{:>15}|'
header = tpl.format('name', 'age', 'tel')

while True:
    action = input('Please input a command:\n(find/list/add/delete/update/exit):')
    action = action.strip()
    if action == 'add':
        name = input('请输入名字：')
        age = input('请输入年龄：')
        tel = input('请输入手机号：')
        user_dict = {'name':name, 'age':age, 'tel':tel}
        is_exists = False
        for user in users:
            if user['name'] == user_dict['name']:
                is_exists = True
                print('用户存在！')
                break
        if not is_exists:
            users.append(user_dict)
            print('添加成功')
    elif action == 'delete':
        name = input('请输入删除的用户：')
        is_exists = False
        for user in users:
            if user['name'] == name:
                is_exists = True
                users.remove(user)
        if not is_exists:
            print('用户不存在')
    elif action == 'update':
        name = input('请输入名字：')
        age = input('请输入年龄：')
        tel = input('请输入手机号：')
        user_dict = {'name':name, 'age':age, 'tel':tel}
        is_exists = False
        for user in users:
            if user['name'] == user_dict['name']:
                is_exists = True
                users.remove(user)
                users.append(user_dict)
                print('更新成功')
                break
        if not is_exists:
            print('没有这个用户')
    elif action == 'find':
        name = input('请输入查找的用户名：')
        is_exists = False
        for user in users:
            if user['name'] == name:
                print(header)
                print(tpl.format(user['name'], user['age'], user['tel']))
                is_exists = True
                break
        if not is_exists:
            print('用户不存在')
    elif action == 'list':
        print(header)
        for user in users:
            print(tpl.format(user['name'], user['age'], user['tel']))
    elif action == 'exit':
        print('exit')
        break
    else:
        print('输入错误')