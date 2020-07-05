'''
3.请使用pymysql完成以下需求：
插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的
值：250
老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？'''
# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root',
                       password='root', database='books', autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行插入一本书（需求）
sql = "insert into t_book(`title`,`read`,`comment`,`pub_date`) " \
      "values('python从入门到放弃',50,0,'2020-01-01')"
cursor.execute(sql)
# 更新评论量250
sql2 = "update t_book set `comment`=`comment`+250 where `title`='python从入门到放弃'"
cursor.execute(sql2)
# 删除python从入门到放弃这本书
sql3 = "delete from t_book where `title`='python从入门到放弃'"
cursor.execute(sql3)
# 查看是否还有python从入门到放弃这本书
sql4 = "select `title` from t_book"
cursor.execute(sql4)
print(cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
