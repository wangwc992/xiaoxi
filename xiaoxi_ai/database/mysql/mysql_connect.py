import MySQLdb


class MySQLConnect:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="192.168.0.137",
            user="root",
            passwd="mirandA123!@#",
            db="test_xxlxdb",
            # host="127.0.0.1",
            # user="root",
            # passwd="root",
            # db="ai_knowledge_base"
        )

        # 创建游标对象
        self.__cur = self.conn.cursor()

    # __cur的getter方法
    @property
    def cur(self):
        return self.__cur
