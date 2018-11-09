# coding:utf-8

# 首先导入pymysql，我们目前只用连接的方法
from pymysql import connect
import json

# 创建类
class MysqlHelp(object):
    # 初始化方法
    def __init__(self, database, host='rm-bp1z3w2eooj7368825o.mysql.rds.aliyuncs.com', user='lbtest', password='lanbeitest@2018', port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        # self.charset = charset
        self.port = port

    # 初始化完后连接到数据库并创建好游标
    def open(self):
        # 连接数据库
        self.conn = connect(host=self.host, user=self.user, password=self.password,
                            database=self.database, port=self.port)
        # 创建游标
        self.cur = self.conn.cursor()

    # 有连接数据库，就得有关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()

    # 光连接关闭数据库不行啊，中间还要对数据库操作呢
    def sql_execute(self, sql, L=[]):  # 增删改
        # 操作就得打开数据库吧
        self.open()
        # 对sql语句处理（即开始操作数据库了）,有成功有失败
        try:
            self.cur.execute(sql, L)  # 执行sql命令
            self.conn.commit()  # 提交到数据库执行
            print('ok')
        except Exception as e:
            self.conn.rollback()
            print('failed', e)
        # 打开数据库就得关闭吧
        self.close()

    # 增删改有了，查呢
    def getAll(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        result = self.cur.fetchall()  # 查询结果用result绑定
        self.close()
        return result  # 将查询到的结果返回回去

# if __name__ == '__main__':
#     m = MysqlHelp('lanbeigzt_test')
#     sql_data = m.getAll('select enterprise_code from business_l_company_user where id = %s', [1])
#     print(sql_data[0][0], type(sql_data[0][0]))







