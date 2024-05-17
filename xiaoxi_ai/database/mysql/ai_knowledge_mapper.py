import xiaoxi_ai.database.mysql.mysql_connect as mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur
'''
CREATE TABLE `ai_knowledge` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `weaviate_id` varchar(100) DEFAULT NULL COMMENT '向量数据库id',
  `school_name` varchar(100) DEFAULT NULL COMMENT '学校名称',
  `country_name` varchar(100) DEFAULT NULL COMMENT '国家名称',
  `question` varchar(500) DEFAULT NULL COMMENT '用户问题',
  `answer` longtext COMMENT '问题回答',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `delete_status` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16135 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='学校数据库';
'''

class AiKnowledge:
    def __init__(self, id, weaviate_id, school_name, country_name, question, answer, create_time, update_time, delete_status):
        self.id = id
        self.weaviate_id = weaviate_id
        self.school_name = school_name
        self.country_name = country_name
        self.question = question
        self.answer = answer
        self.create_time = create_time
        self.update_time = update_time
        self.delete_status = delete_status

# 插入知识库数据
def insert_ai_knowledge(weaviate_id, school_name, country_name, question, answer):
    mySQLConnectCur.execute(
        "INSERT INTO `ai_knowledge` (`weaviate_id`, `school_name`, `country_name`, `question`, `answer`) VALUES (%s, %s, %s, %s, %s)",
        (weaviate_id, school_name, country_name, question, answer))
    mySQLConnectCur.connection.commit()
    return mySQLConnectCur.lastrowid

# 根据id查询学校信息
def select_ai_knowledge_by_id(id, limit):
    mySQLConnectCur.execute('select * from ai_knowledge where id>=%s limit %s', (id, limit))
    results = mySQLConnectCur.fetchall()

    # Convert each tuple to an AiKnowledge object
    ai_knowledge_list = [AiKnowledge(*result) for result in results]

    return ai_knowledge_list


# 预编译更新知识库数据
def update_ai_knowledge(id, weaviate_id, school_name=None, country_name=None, question=None, answer=None):
    # Start with the base update statement and mandatory fields
    query = 'UPDATE ai_knowledge SET weaviate_id=%s'
    params = [weaviate_id]

    # Add optional fields to the query if they are not None
    if school_name is not None:
        query += ', school_name=%s'
        params.append(school_name)
    if country_name is not None:
        query += ', country_name=%s'
        params.append(country_name)
    if question is not None:
        query += ', question=%s'
        params.append(question)
    if answer is not None:
        query += ', answer=%s'
        params.append(answer)

    # Add the WHERE clause and id parameter
    query += ' WHERE id=%s'
    params.append(id)

    # Execute the query
    mySQLConnectCur.execute(query, params)
    mySQLConnectCur.connection.commit()

    return mySQLConnectCur.rowcount


def update_ai_knowledge_uuid(uuid_list):
    # [{'id': 1, 'uuid': 7ab69d16-095e-4791-bcc0-6e7282bd27a3}, {'id': 2, 'uuid': b8b6dc01-550a-49db-ad87-bfb193657f35}, {'id': 3, 'uuid': c5c509e4-9279-465a-b693-4e2c5984fc96}]
    for uuid in uuid_list:
        mySQLConnectCur.execute('UPDATE ai_knowledge SET weaviate_id=%s WHERE id=%s', (uuid['uuid'], uuid['id']))
        mySQLConnectCur.connection.commit()