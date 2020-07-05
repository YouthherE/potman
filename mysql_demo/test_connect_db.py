# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root', password='root')
# 获取游标
cursor = conn.cursor()
# 执行查询版本的SQL（需求）
cursor.execute("select version();")
# 打印结果
result = cursor.fetchone()
print('result=', result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
