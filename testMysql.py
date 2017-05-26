from datetime import date, datetime, timedelta
import pymysql.cursors

#连接数据库
# 连接配置信息
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'xy521521',
    'db': 'xx',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)

# 获取明天的时间
#tomorrow = datetime.now().date() + timedelta(days=1)
#print(tomorrow)
# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO user (user_name) VALUES ( %s)'
        cursor.execute(sql, ('Robin'))
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close()