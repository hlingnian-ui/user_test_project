import pymysql
from common.config import *

conn = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB,
    charset="utf8mb4",
    autocommit=True
)

def query(sql):
    with conn.cursor() as cursor:
        rows = cursor.execute(sql)
        result = cursor.fetchall()
        return result