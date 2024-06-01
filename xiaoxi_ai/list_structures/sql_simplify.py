import os
import re

def simplify_sql(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sql = f.read()

    # Match table name and table comment
    table_pattern = re.compile(r'CREATE TABLE `(\w+)`.*?COMMENT = \'(.*?)\'', re.S)
    # Match field name and field comment
    field_pattern = re.compile(r'`(\w+)`.*?COMMENT \'(.*?)\'', re.S)

    table_matches = table_pattern.findall(sql)
    simplified_tables = []

    for table in table_matches:
        table_name, table_comment = table
        simplified_table = f"{table_name}：{table_comment}("
        field_matches = field_pattern.findall(sql)
        simplified_fields = []

        for field in field_matches:
            field_name, field_comment = field
            simplified_fields.append(f"{field_name}:{field_comment}")

        simplified_table += ',\n '.join(simplified_fields)
        simplified_table += f")"
        simplified_tables.append(simplified_table)

    return simplified_tables

directory = 'D:\\DevelopmentTool\\Python\\Project\\xiaoxi\\xiaoxi_ai\\list_structures\\table'

for filename in os.listdir(directory):
    if filename.endswith('.sql'):
        file_path = os.path.join(directory, filename)
        simplified_sql = simplify_sql(file_path)
        # print(simplified_sql)
        with open(file_path, 'w', encoding='utf-8') as f:
            for table in simplified_sql:
                f.write(table + '\n')