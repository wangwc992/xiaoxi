import xiaoxi_ai.database.mysql.mysql_connect as mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur
'''
CREATE TABLE `ai_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `school_name` varchar(50) DEFAULT NULL COMMENT '学校名称',
  `url_name` varchar(100) DEFAULT NULL COMMENT 'url',
  `un_url` varchar(500) DEFAULT NULL COMMENT 'url',
  `or_content` text COMMENT '原本的内容',
  `chat_content` text COMMENT 'chat的内容',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `delete_status` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `un_url` (`un_url`)
) ENGINE=InnoDB AUTO_INCREMENT=29081 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='学校数据库';
'''


# ai_school表对应的类


class AiSchool:
    def __init__(self, id, school_name, un_url, url_name, content, create_time, update_time, delete_status):
        self.id = id
        self.school_name = school_name
        self.un_url = un_url
        self.url_name = url_name
        self.content = content
        self.create_time = create_time
        self.update_time = update_time
        self.delete_status = delete_status

    def __str__(self):
        return f'id:{self.id}, school_name:{self.school_name}, un_url:{self.un_url}, url_name:{self.url_name}, content:{self.content}, create_time:{self.create_time}, update_time:{self.update_time}, delete_status:{self.delete_status}'


# 插入学校信息，返回主键id
def insert_ai_school(school_name, un_url, url_name):
    # 如果 un_url 中存在 @ 和 出去 : 这将插入为默认删除状态
    # https://www.sydney.edu.aujavascript:void()tel:1800 SYD HEL/courses/field-of-study/music.html  从第八个字符开始截取
    trimmed_link = un_url[7:]
    if '@' in trimmed_link or ':' in trimmed_link or '.pdf' in trimmed_link:
        mySQLConnectCur.execute(
            f"INSERT INTO `ai_school` (`school_name`, `un_url`, `url_name`, `delete_status`) VALUES ('{school_name}', '{un_url}', '{url_name}', 1)")
    else:
        mySQLConnectCur.execute(
            f"INSERT INTO `ai_school` (`school_name`, `un_url`, `url_name`) VALUES ('{school_name}', '{un_url}', '{url_name}')")
        mySQLConnectCur.connection.commit()
    return mySQLConnectCur.lastrowid


# 查询学校信息
def select_ai_school():
    # 查询状态为0的数据
    mySQLConnectCur.execute("SELECT * FROM `ai_school` WHERE `delete_status` = 0")
    return mySQLConnectCur.fetchall()


def select_ai_school_and_gt_id(id):
    # 查询状态为0的数据
    mySQLConnectCur.execute(f"SELECT * FROM `ai_school` WHERE `delete_status` = 0 and `id` >= {id} limit 1")
    return mySQLConnectCur.fetchall()


# 更新学校信息
def update_ai_school(id, or_content, chat_content):
    # 使用预编译的方式编写sql语句
    mySQLConnectCur.execute(
        "UPDATE `ai_school` SET `or_content` = %s, `chat_content` = %s WHERE `id` = %s",
        (or_content, chat_content, id))

    mySQLConnectCur.connection.commit()


# 关闭游标和连接
def close_connection():
    mySQLConnectCur.close()
    mysql_connect.MySQLConnect().conn.close()
