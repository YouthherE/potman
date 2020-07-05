'''
4.使用pymysql操作MySQL数据库，具体操作如下： 1).在“books”数据库中，新增评论表t_comment，
包含字段：主键、图书id、评论人名称、评论内容、评论时间。 2).在评论表中新增一条数据，并更新图
书表t_book中的评论量comment字段。
'''
# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root',
                       password='root', database='books', autocommit=False)
# 获取游标
cursor = conn.cursor()
# 创建评论表（需求）
table = "CREATE TABLE `t_comment`(`id` int(11) NOT NULL AUTO_INCREMENT," \
        "`book_id` int(11) NOT NULL COMMENT '所属图书ID'," \
        "`com_name` varchar(20) NOT NULL COMMENT '评论人名称'," \
        "`com_title` varchar(20) NOT NULL COMMENT '评论内容'," \
        "`com_date` date NOT NULL COMMENT '评论日期'," \
        "PRIMARY KEY (`id`));"
cursor.execute(table)
conn.commit()
try:
    # 添加数据
    sql = "insert into t_comment(`book_id`,`com_name`,`com_title`,`com_date`) " \
          "values(2,'此间少年','这本书真的挺不错哦','2020-01-01')"
    cursor.execute(sql)
    sql2 = "update t_book set `comment`=`comment`+1 where `id`=2"
    cursor.execute(sql2)
    conn.commit()
except Exception as e:
    conn.rollback()
    print("系统处理有误：", e)
finally:
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
