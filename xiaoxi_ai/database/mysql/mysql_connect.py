import MySQLdb
from django.conf import settings


class MySQLConnect:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            db=settings.MYSQL_DB,
            # host="120.92.116.101",
            # user="read",
            # passwd="Xxedu_only_Read123!@#",
            # db="xxlxdb",
            # port=9200,
        )

        # 创建游标对象
        self.__cur = self.conn.cursor()

    # __cur的getter方法
    @property
    def cur(self):
        return self.__cur
