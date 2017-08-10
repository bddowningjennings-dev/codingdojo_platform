from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='00000Crazyk.',
                                 host='127.0.0.1',
                                 port='3306',
                                 database='mydb')
cnx.close()