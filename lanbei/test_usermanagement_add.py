# coding:utf-8


import requests
import json
import unittest
from lanbei import MysqlPython



class UserManageMentAdd(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.55.49.147:8082'
        print('start------->')

    def tearDown(self):
        print('end--------->')

    # def get_params(self):
    #     m = MysqlPython.MysqlHelp('lanbeigzt_test')
    #     m.sql_execute('INSERT into business_l_company_user (login_name, name, phone, role, enterprise_code) '
    #                            'VALUES (%s, %s, %s, %s, %s)',
    #                            ['登录名', '姓名', '13322221115', '1', 'qy000002'])
    #     params = m.getAll('select * from business_l_company_user where phone = %s', ['13322221115'])
    #     return params

    def test03_user_management_add(self):
            path = '/salary-company/login/saveOrUpdate'
            data = {'loginName': '登录名1',
                    'name': 'test1',
                    'phone': 13326262655,
                    'role': 1,
                    'enterprise_code': 'qy000001'
            }
            response = requests.post(self.url+path, data)
            print(response.text)
            # self.assertIn(d[0][7], d)

if __name__ == '__main__':
    unittest.main()