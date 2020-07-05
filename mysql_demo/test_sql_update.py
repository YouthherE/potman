# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root',
                       password='root', database='books', autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行查询版本的SQL（需求）
sql = "update t_book set `read`=`read`+1 where `id`=4"
cursor.execute(sql)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
