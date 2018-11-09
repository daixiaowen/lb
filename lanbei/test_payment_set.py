# coding:utf-8


import requests
import unittest
from lanbei import MysqlPython
import json

class PaymentSet(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.55.49.147:8082'
        print('开始测试')

    def tearDown(self):
        print('结束测试')

    def get_id_risk(self):
        m = MysqlPython.MysqlHelp('lanbeigzt_test')
        params = m.getAll('select id, risk from business_c_account where id = %s', [1])
        return params

# print(PaymentSet().get_id_risk()[0][1])

    def test02_panyment_set(self):
        path = '/salary-company/account/updateAccountById'
        data = {
            'id': PaymentSet().get_id_risk()[0][0],
            'risk': PaymentSet().get_id_risk()[0][1]
        }
        response = requests.post(self.url+path, data)
        js_data = response.json()
        self.assertEqual('200', js_data['status'])

if __name__ == '__main__':
    unittest.main()
