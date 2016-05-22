# -*- encoding:utf-8 -*-
import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursorDict
reload(sys)
sys.setdefaultencoding('utf-8')

host = 'yourhost'
port = 3306  # int
database = 'yourdb'
user = 'youruser'
password = 'youruserpassword'

sql_select = """
SELECT `id`, title
FROM test
WHERE `status`=1;
"""

db1 = mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    database=database,
    port=port,
    charset='utf8'
)
cs1 = db1.cursor(cursor_class=MySQLCursorDict)
cs1.execute(sql_select)

# TODO

cs1.close()
db1.close()

db2 = mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    database=database,
    port=port,
    charset='utf8',
    autocommit=True
)
cs2 = db2.cursor(cursor_class=MySQLCursorDict)

# TODO

cs2.close()
db2.close()
