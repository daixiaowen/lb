# coding:utf-8

import pymysql


class MysqlHelp(object):
    def __init__(self, database, host='rm-bp1z3w2eooj7368825o.mysql.rds.aliyuncs.com', user='lbtest', password='lanbeitest@2018', port=3306):
        self.database = database  # 数据库名
        self.host = host
        self.port = port
        self.user = user  # 用户名
        self.password = password  # 密码

    # 链接数据库，创建游标
    def connect_database(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        # 创建游标
        self.cur = self.conn.cursor()

    # 执行sql(增，删，改)
    def execute_sql(self, sql, L=[]):
        # 打开数据库
        self.connect_database()
        try:
            self.cur.execute(sql, L)  # 执行sql
            self.conn.commit()  # 提交到数据库执行
        except Exception as e:
            self.conn.rollback()  # 回滚
            print('提交失败', e)
        # 关闭数据库
        self.close_database()

    # 获取数据（查询）
    def getData(self, sql, L=[]):
        # 打开数据库
        self.connect_database()
        try:
            self.cur.execute(sql,L)
            data = self.cur.fetchall()  # 获取所有数据
        except Exception as e:
            print('未查询到结果')
        return data

    # 关闭数据库
    def close_database(self):
        self.cursor.close()
        self.conn.close()

# m = MysqlHelp('lanbeigzt_test')
# d = m.getData('select enterprise_code from business_l_company_user where id = %s', [1])
# print(d)