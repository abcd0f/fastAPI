from config.db import execute_sql
from utils.response import res_success, res_error


def findAll():
    try:
        sql = "select * from list"
        data = execute_sql(sql)
        return res_success(data)

    except:
        return None


def findOne(id):
    try:
        sql = f"select * from list where id = {id}"
        data = execute_sql(sql)
        return res_success(data)
    except:
        return None


def update(id, item):
    try:
        print(f"111{id,item}")
        sql = "UPDATE list SET title = %s, txt = %s WHERE id = %s"
        params = (item.title, item.txt, id)
        data = execute_sql(sql, params, is_query=False)
        return res_success(data)

    except:
        return {"msg": "error"}


def create(item):
    try:
        sql = "INSERT INTO list (title, txt) VALUES (%s, %s)"
        params = (item.title, item.txt)
        data = execute_sql(sql, params, is_query=False)
        return res_success(data)
    except Exception as e:
        print(f"Error: {e}")
        return {"msg": "error"}


def delete(id):
    try:
        sql = f"DELETE FROM list WHERE id = {id}"
        data = execute_sql(sql, is_query=False)
        return res_success(data)
    except:
        return {"msg": "error"}
