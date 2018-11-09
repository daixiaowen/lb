# coding:utf-8
import requests
import unittest
import json
from lanbei import MysqlPython

class LanBei(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.55.49.147:8082'
        print('测试开始')

    def tearDown(self):
        print('测试结束')

    # 获取企业编号
    def get_enterprise_code(self):
        m = MysqlPython.MysqlHelp('lanbeigzt_test')
        params = m.getAll('select enterprise_code from business_l_company_user where id = %s', [1])
        return params

    # 备付金列表
    def test01_get_payment_list(self):
        path = '/salary-company/account/queryAccountInfo'
        data = {"enterprise_code": LanBei().get_enterprise_code(),  # 企业编码
                "pageIndex": "1",  # 页数
                "pageSize": "10"}  # 每页显示数
        respone = requests.post(self.url+path, data)
        # print(respone.text)
        js_data = respone.json()
        self.assertEqual('qy000001', js_data["data"]['accountList'][0]['enterprise_code'])
        print('备付金管理列表')

if __name__ == '__main__':
    unittest.main()