# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root',
                       password='root', database='books', autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行增加一本书（需求）
sql = "insert into t_book (`id`,`title`,`pub_date`) values ('4','西游记后传','1986-3-25')"
cursor.execute(sql)
sql2 = "SELECT `id`,`title`,`read`,`comment` from t_book;"
cursor.execute(sql2)
print('全部的书是:', cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
