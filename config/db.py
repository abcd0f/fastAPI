from fastapi import HTTPException
from mysql.connector import pooling, Error

# 数据库配置
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "db",
}

# 连接池配置
POOL = pooling.MySQLConnectionPool(
    pool_name="mypool", pool_size=5, **DB_CONFIG  # 可根据实际情况调整连接池大小
)


# 数据库连接函数
def get_db_connection():
    try:
        conn = POOL.get_connection()
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise HTTPException(status_code=500, detail="数据库连接失败")


# 通用的 SQL 执行函数
def execute_sql(sql: str, params: tuple = (), fetchone=False, is_query=True):
    """
    执行 SQL 语句的通用函数。

    :param sql: 要执行的 SQL 语句。
    :param params: SQL 语句中的参数，默认为空元组。
    :param fetchone: 如果是查询操作，是否只返回第一行数据（默认为 False）。
    :param is_query: 是否是查询操作（默认为 True）。如果为 False，则执行更新操作。
    :return: 查询操作返回查询结果，更新操作返回受影响的行数。
    """
    conn = get_db_connection()
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            if is_query:  # 如果是查询操作
                if fetchone:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
                return result
            else:  # 如果是更新操作
                conn.commit()  #
                return cursor.rowcount  # 返回受影响的行数
    finally:
        conn.close()
