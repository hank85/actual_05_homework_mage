#encoding: utf-8

import json
import pymysql
import queue
import hashlib
from contextlib import contextmanager
from pymysql.cursors import DictCursor
'''
1. 每一个用户存储信息修改为字典
{
    xx : {name : xxx, age : xxxx, tel: xxx, 'password' : 'xxx'},
    xxx: {}
}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''

HOST = '172.16.129.143'
PORT = 3306
DB = 'xiaozhi'
USER = 'root'
PASSWD = 'password'
CHARSET ='utf8'

SQL_MESSAGE_LIST = "select username, password from userlist where username=%s and password=%s"
SQL_MESSAGE_LIST_USERS = "select id, username, password, age, tel from userlist"
SQL_MESSAGE_DELETE = "delete from userlist where id = %s"

SQL_MESSAGE_INSERT = "insert into userlist(username, password, age, tel, create_date) " \
                     "values(%s,%s,%s, %s, %s);"

SQL_MESSAGE_UPDATE_SELECT = "select username, password from userlist where id=%s"
SQL_MESSAGE_UPDATE = "update userlist set age=%s, tel=%s, create_date='now()'" \
                     "WHERE id = %s; "

SQL_MESSAGE_UPDATE_PASSWORD = "update userlist set password=%s, create_date='now()'" \
                     "WHERE id = %s; "

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def load_users():
    users = get_users()
    return users

def dump_users(path, users):
    fhandler = open(path, 'wt')
    # for user in users.values():
    #     fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['age'], user['tel'], user['password']))
    fhandler.write(json.dumps(users))
    fhandler.close()


def validate_login(name, password):

    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()

    cur.execute(SQL_MESSAGE_LIST,(name, password))
    rt_list = cur.fetchone()

    cur.close()
    conn.close()
    return rt_list


def get_users():
    rt = {}
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_LIST_USERS)
    rt_list = cur.fetchall()
    for row in rt_list:
            userid = row['id']
            username = row['username']
            password = row['password']
            age = row['age']
            tel = row['tel']
            rt[username] = {'userid':userid,"username":username, 'password':password, 'age':age, 'tel':tel}

    rt = list(rt.values())
    cur.close()
    conn.close()
    return rt


'''
return True/False, ''
'''
def validate_add_user(name, age, tel, password):
    users=load_users()
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    if name in users:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def add_user(name, age, tel, password):
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET)
    cur = conn.cursor()
    print(SQL_MESSAGE_INSERT, (name, password, age, tel, 'now()'))
    cur.execute(SQL_MESSAGE_INSERT, (name, password, age, tel, 'now()'))
    conn.commit()



def input_add_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def input_delete_user():
    return input('请输入你要删除的用户名:')

def md5(password):
    m = hashlib.md5()
    m.update(password.encode(encoding='utf-8'))
    return m.hexdigest()

def validate_delete_user(name, users):
    user = users.get(name)
    if user:
        return True
    else:
        return False, '删除用户失败, 失败原因: 用户名不存在'


def delete_user(userid):
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_DELETE, (userid))
    print(SQL_MESSAGE_DELETE, (userid))
    conn.commit()
    cur.close()
    conn.close()


def get_user_by_name(name):
    users = load_users()
    user = users.get(name, '')
    return user

def input_modify_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def validate_modify_user(userid, age):

    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET,cursorclass=DictCursor)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_UPDATE_SELECT, (userid,))
    rt_list = cur.fetchone()
    cur.close()
    conn.close()
    if rt_list is None:

        return False, '更新用户失败, 错误原因: 用户不存在'


    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''


def modify_user(id, age, tel):
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()

    cur.execute(SQL_MESSAGE_UPDATE, (age, tel,id))
    conn.commit()
    cur.close()
    conn.close()

def validate_modify_user_password(userid, password, old_password):

    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_UPDATE_SELECT, (userid))
    rt_list = cur.fetchone()
    print()
    username = rt_list['username']
    user_password = rt_list['password']
    cur.close()
    conn.close()
    print(username, user_password)
    if rt_list is None:
        return False, '更新用户失败, 错误原因: 用户不存在'
    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'
    if old_password != user_password:
        return False, '密码验证错误'

    return True, ''


def modify_user_password(id, password):
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_UPDATE_PASSWORD, (password, id))
    conn.commit()
    cur.close()
    conn.close()



def find_user(name, users):
    rt_list = []
    for user in users.values():
        if user['name'].find(name) != -1:
            rt_list.append(user)

    return rt_list

def list_user():
    users = load_users()
    return  users




def main():
    users = load_users()

    is_valid = False
    #用户认证，最多3次，用户输入用户名和电话
    for i in range(3):
        name = input('请输入用户名:')
        password = input('请输入密码:')
        if validate_login(name, password, users):
            is_valid = True
            break
        else:
            print('认证失败, 请重试')

    if not is_valid:
        print('已超过最大认证次数，程序退出')
    else:
        while True:
            action = input('please input(find/list/add/delete/update/exit):')
            if action == 'add':
                #增加用户
                name, age, tel, password = input_add_user()
                rt_status, rt_reason = validate_add_user(name, age, tel, password, users)
                if rt_status:
                    add_user(name, age, tel, password, users)
                else:
                    print(rt_reason)
            elif action == 'delete':
                #删除用户
                name = input_delete_user()
                rt_status, rt_reason = validate_delete_user(name, users)
                if rt_status:
                    delete_user(name, users)
                    print('删除用户成功')
                else:
                    print(rt_reason)
            elif action == 'update':
                # 更改用户
                name, age, tel, password = input_modify_user()
                rt_status, rt_reason = validate_modify_user(name, age, tel, password, users)
                if rt_status:
                    modify_user(name, age, tel, password, users)
                    print('更新用户成功')
                else:
                    print(rt_reason)

            elif action == 'find':
                # 查找用户
                name = input('请输入你要查询的用户名:')
                rt_list = find_user(name, users)
                if rt_list:
                    print(user_info_header)
                    for user in rt_list:
                        print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
                else:
                    print('没有该用户信息')

            elif action == 'list':
                #罗列所有用户
                field = input('请输入排序的列(name, age, tel):')
                print(user_info_header)

                for user in list_user(field, users):
                    print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))

            elif action == 'exit':
                #退出程序
                dump_users(path, users)
                break
            else:
                print('命令错误')

class ConnectionPool:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 10)
        self.idle = kwargs.pop('idle', 3)
        self.kwargs = kwargs
        self.length = 0
        self.connections = queue.Queue(maxsize=self.idle)

    def _connect(self):
        if not self.connections.full():
            conn = pymysql.connect(**self.kwargs)
            self.connections.put(conn)
            self.length += 1
        else:
            raise RuntimeError('lot of connections')

    def _close(self, conn):
        conn.close()
        self.length -= 1

    def get(self, timeout=None):
        if self.connections.empty() and self.length < self.size:
            self._connect()
        conn = self.connections.get(timeout=timeout)
        conn.ping(reconnect=True)
        return conn

    def return_resource(self, conn):
        if self.connections.full():
            self._close(conn)
            return
        self.connections.put(conn)

    @contextmanager
    def __call__(self, timeout=None):
        conn = self.get(timeout)
        try:
            yield conn.cursor()
            conn.commit()
        except:
            conn.rollback()
        finally:
            self.return_resource(conn)



if __name__ == '__main__':
    main()
    pool = ConnectionPool(host='172.16.129.143',
                          port=3306,
                          user='root',
                          passwd='password',
                          db='xiaozhi',
                          charset="utf8",
                          cursorclass=DictCursor)
    with pool() as cur:
        cur.execute('''insert into userlist(username, password, age, tel, create_date)
                    values('za','123456','29', '123456', now());''')
        for res in cur.fetchall():
            print(res)

