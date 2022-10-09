import sqlalchemy



def connDB():
    conn = sqlalchemy.create_engine("mariadb+pymysql://root:root@127.0.0.1/meli?charset=utf8mb4")
    return conn

