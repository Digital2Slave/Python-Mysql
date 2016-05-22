# -*- encoding:utf-8 -*-
import sys
import MySQLdb
from MySQLdb.cursors import SSDictCursor
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

db1 = MySQLdb.connect(
    host,
    user,
    password,
    database,
    port=port,
    charset='utf8',
    cursorclass=SSDictCursor
)
cs1 = db1.cursor()
cs1.execute(sql_select)

# TODO

cs1.close()
db1.close()


db2 = MySQLdb.connect(
    host,
    user,
    password,
    database,
    port=port,
    charset='utf8'
)
db2.autocommit(True)
cs2 = db2.cursor()

# TODO

cs2.close()
db2.close()
