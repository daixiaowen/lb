# coding:utf-8


import requests
import unittest
import json
from lanbei import MysqlPython


class PaymentSelect(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.55.49.147:8082/salary-company'
        print('------>start')

    def tearDown(self):
        print('------>end')

    # 获取账户表主键ID
    def get_id(self):
        m = MysqlPython.MysqlHelp('lanbeigzt_test')
        params = m.getAll('select * from business_c_account where id = %s', [5])
        return params

    def test04_payment_select(self):
        path = '/account/queryCompanyBalance'
        data = {'id': PaymentSelect().get_id()[0]}
        response = requests.post(self.url+path, data)
        print(response.text)

if __name__ == '__main__':
    unittest.main()