# csv_oracle.py
import time

import cx_Oracle as oci
import csv
import time

# 테이블 생성 함수
def createDBTable(sql_sentence):

    print(sql_sentence.split(" ")[2].split("(")[0])
    sql_0 = 'DROP TABLE ' + sql_sentence.split(" ")[2].split("(")[0] + " CASCADE CONSTRAINTS"
    sql_1 = sql_sentence

    print(sql_0)
    print(sql_1)

    time.sleep(3)
    sql_command(sql_0)
    time.sleep(3)
    sql_command(sql_1)

# 저장 - 내역
def saveHistory(data):
    sql = """
        INSERT INTO history VALUES({}, '{}', {}, {})
        """.format(data[0], data[1], data[2], data[3])
    sql_command(sql)

# 저장 - 총 내역
def saveCotract(data):
    sql = """
        INSERT INTO contract VALUES(seq_contract_cid.nextval, {}, SYSDATE)
        """.format(data)
    sql_command(sql)

def find_sequence(column, table_name):
    # sql = "SELECT {}.CURRVAL FROM DUAL".format(str(seq_name).strip().upper())
    sql = "select MAX(TO_NUMBER({})) from {}".format(column, table_name)
    return sql_command(sql)

def viewDB(tableName):
    sql = 'SELECT * FROM {}'.format(tableName)
    return [record for record in sql_command(sql)]

def sql_command(sql_sentence, data=None):
    conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
    cursor = conn.cursor()
    sql = sql_sentence

    result = cursor.execute(sql) if data == None else cursor.execute(sql, data)

    result_list = []

    if result != None:
        result_list = result.fetchall()

    cursor.close()
    conn.commit() # *******
    conn.close()

    return result_list

# 실행파일
if __name__ == "__main__":
    '''INSERT INTO contract VALUES(seq_contract_cid.nextval, 1500000, SYSDATE)'''
    sql_command()


#     # 1) create table
#     createDBTable(''' CREATE TABLE product(
#     id varchar2(1) primary key,
#     supplier varchar2(100),
#     name varchar2(40),
#     price number(13),
#     regi_date date
# )''')
#
#     # 2) file data save
#     file_name = 'supply.csv'
#     f = open(file_name, 'r')
#     datas = csv.reader(f, delimiter=',')
#     header = next(datas, None) # read and not work
#
#     print("-"*50)
#
#     for row in datas:
#         print(row)
#         saveCotract(row)
#
#     # 3) table record search
#     viewDB('supply') # table search