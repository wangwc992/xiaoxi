import pandas as pd
import xiaoxi_ai.database.mysql.mysql_connect as mysql_connect



cursor = mysql_connect.MySQLConnect().cur

def get_student_info(cla, student_name: str, service_id: str) -> str:
    # student_name 和 service_id 都是空直接结束
    if not student_name and not service_id:
        return "学生姓名和service_id都为空，请重新输入"
    search_apply_id = ''
    if service_id:
        search_apply_id = f"SELECT id from apply_main where service_id =  '{service_id}';"
    else:
        search_apply_id = f'''
        SELECT id  from apply_main where service_id =
        (SELECT id from service_master where user_real_name = '{student_name}' );
        '''
    cla.cursor.execute(search_apply_id)
    rows = cla.cursor.fetchall()
    apply_main_id_list = [str(row['id']) for row in rows]
    if not apply_main_id_list:
        return "未查询到该学生信息"
    apply_main_id_str = ','.join(apply_main_id_list)
    # Rest of the code remains the same

    sql = f'''
        SELECT * from apply_basic_info where main_id in ({apply_main_id_str});
        SELECT * from apply_credit_card where main_id in ({apply_main_id_str});
        SELECT * from apply_education where main_id in ({apply_main_id_str});
        SELECT * from apply_job_exp where main_id in ({apply_main_id_str});
        SELECT * from apply_paper_exp where main_id in ({apply_main_id_str});
        SELECT * from apply_parent_info where main_id in ({apply_main_id_str});
        SELECT * from apply_referrer_info where main_id in ({apply_main_id_str});
        SELECT * from apply_transcript where main_id in ({apply_main_id_str});
        SELECT * from apply_visa where main_id in ({apply_main_id_str});
        SELECT * from apply_willfill_log where main_id in ({apply_main_id_str});
    '''

    sql_commands = sql.split(';')
    reference_data = []
    for command in sql_commands:
        if command.strip() != '':
            cla.cursor.execute(command)
            # 假设 rows 是你从数据库查询得到的结果
            rows = cla.cursor.fetchall()

            # 将 rows 转换为 pandas DataFrame
            df = pd.DataFrame(rows)

            # 删除除 'id', 'main_id', 'create_time', 'update_time' 外其他字段相同的重复行
            df = df.drop_duplicates(
                subset=df.columns.difference(['id', 'main_id', 'create_time', 'update_time', 'married']))

            # 将 DataFrame 转换回字典列表
            rows = df.to_dict('records')
            # 删除值为 None 或空字符串的键值对
            rows = [{k: v for k, v in row.items() if v is not None and v != ''} for row in rows]
            for row in rows:
                reference_data.append(row)

    return reference_data
