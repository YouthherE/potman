
import unittest
import pymysql
from parameterized import parameterized


class MySql(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = pymysql.connect(host='localhost', user='root',
                                   password='root', database='books', autocommit=True)
        cls.cursor = cls.conn.cursor()

        return cls.conn, cls.cursor

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    @parameterized.expand()
    def test1_insert(self):
        sql = "insert into t_book (`id`,`title`,`pub_date`) values ('4','西游记后传','1986-3-25')"
        self.cursor.execute(sql)
        sql2 = "SELECT `id`,`title`,`read`,`comment` from t_book;"
        self.cursor.execute(sql2)
        print('全部的书是:', self.cursor.fetchall())

    def test2_update(self):
        sql = "update t_book set `read`=`read`+1 where `id`=4"
        self.cursor.execute(sql)
        sql2 = "SELECT `id`,`title`,`read`,`comment` from t_book;"
        self.cursor.execute(sql2)
        print('全部的书是:', self.cursor.fetchall())

    def test3_delete(self):
        sql = "delete from t_book where `id`=4"
        self.cursor.execute(sql)
        sql2 = "SELECT `id`,`title`,`read`,`comment` from t_book;"
        self.cursor.execute(sql2)
        print('全部的书是:', self.cursor.fetchall())
