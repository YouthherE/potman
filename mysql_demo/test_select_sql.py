# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root',
                       password='root', database='books')
# 获取游标
cursor = conn.cursor()
# 执行查询版本的SQL（需求）
cursor.execute("SELECT `id`,`title`,`read`,`comment` from t_book;")
# 打印书的数量
print('有几本书：', cursor.rowcount)
# 打印第一本书
print('第一本书是：', cursor.fetchone())
# 打印全部的书
cursor.rownumber = 0
print('全部的书是:', cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()