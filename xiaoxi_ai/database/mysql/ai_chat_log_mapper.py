import xiaoxi_ai.database.mysql.mysql_connect as mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur

'''
CREATE TABLE `ai_chat_log` (
  `id` varchar(50) NOT NULL COMMENT '会话id',
  `model_name` varchar(50) NOT NULL COMMENT '模型名称',
  `input` longtext NOT NULL COMMENT '用户输入',
  `prompt` longtext NOT NULL COMMENT 'prompt',
  `prompt_tokens` int(11) NOT NULL COMMENT 'prompt token',
  `content` longtext NOT NULL COMMENT 'ai回答',
  `completion_tokens` int(11) NOT NULL COMMENT 'ai token',
  `total_tokens` int(11) NOT NULL COMMENT '总token',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `delete_status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='AI聊天日志';
'''


# 插入AI聊天日志，返回主键id
def insert_ai_chat_log(id, model_name, input, prompt, prompt_tokens, content, completion_tokens, total_tokens):
    # 使用预编译的方式插入数据，判断数据空值不插入
    query = "INSERT INTO `ai_chat_log` (`id`, `model_name`, `input`, `prompt`, `prompt_tokens`, `content`, `completion_tokens`, `total_tokens`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id, model_name, input, prompt, prompt_tokens, content, completion_tokens, total_tokens)
    mySQLConnectCur.execute(query, values)
    mySQLConnectCur.connection.commit()
    return mySQLConnectCur.lastrowid


# 查询AI聊天日志
def select_ai_chat_log():
    mySQLConnectCur.execute("SELECT * FROM `ai_chat_log` LIMIT 0,10")
    rows = mySQLConnectCur.fetchall()
    return rows


# 关闭游标和连接
def close_connection():
    mySQLConnectCur.close()
    mysql_connect.MySQLConnect().conn.close()
