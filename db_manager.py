import sqlite3
from contextlib import contextmanager

#定义连接数据库方法
@contextmanager
def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:conn.close()
 
 #定义查询方法   
def execute_query(db_path, query, params=()):
    with connect_to_db(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        data = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        json_data = [dict(zip(columns, row)) for row in data]
        return json_data

def fetch_data(db_path, query, params=()):
    with connect_to_db(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        json_data = [dict(zip(columns, row)) for row in data]      
        return json_data