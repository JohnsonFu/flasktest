import pymysql.cursors

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'new_schema',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:

        sql = 'select * from user'
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)

    connection.commit()

finally:
    connection.close();