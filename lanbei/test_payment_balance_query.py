# coding:utf-8


import unittest
import requests
import json
from lanbei.mysqlhelper import MysqlHelp

# 备付金余额查询
class PaymentBalanceQuery(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.55.49.147:8082/salary-company'
        print('start-----')
    def tearDown(self):
        print('end-----')

    def getId(self):
        m = MysqlHelp('lbgzt_test').getData('select id from business_c_account where name = %s', ['测试账户(公司)(富友)'])
        return m

    def test_paymanet_balance_qurey(self):
        path = '/account/queryCompanyBalance'
        data = {'id': PaymentBalanceQuery().getId()}
        response = requests.post(self.url+path, data)
        print(response.text)

if __name__ == '__main__':
    unittest.main()