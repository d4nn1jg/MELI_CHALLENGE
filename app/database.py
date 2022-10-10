import sqlalchemy

def connDB():
    conn = sqlalchemy.create_engine("mariadb+pymysql://root:root@mydb/meli?charset=utf8mb4")
    return conn

