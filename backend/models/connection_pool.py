import time
import mysql.connector.pooling


import configparser
config = configparser.ConfigParser()
config.read('C:/Users/pradi/Downloads/database.ini')

dbconfig = {
    "host":config.get('mysql', 'host'),
    "port":config.get('mysql', 'port'),
    "user":config.get('mysql', 'user'),
    "password":config.get('mysql', 'pass'),
    "database":config.get('mysql', 'database'),
}

class MySQLPool(object):
    def __init__(self):             
        self.pool = self.create_pool(pool_name='task_pool', pool_size=3)

    def create_pool(self, pool_name, pool_size):
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **dbconfig)
        return pool

    def close(self, conn, cursor):
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return cursor
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

    def executemany(self, sql, args, commit=False):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res


if __name__ == "__main__":
    mysql_pool = MySQLPool()
    sql = "select * from estudiantes"        
    rv = mysql_pool.execute(sql)
    for result in rv:
        print(result)
    print("done")