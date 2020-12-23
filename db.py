import mysql.connector
import constant


def connectDb():
    return mysql.connector.connect(
        host=constant.dbInfor["host"],
        user=constant.dbInfor["user"],
        password=constant.dbInfor["password"],
        database=constant.dbInfor["database"]
    )

# "CREATE TABLE IF NOT EXISTS students (id int(11) NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL UNIQUE, username VARCHAR(255) NOT NULL UNIQUE, status bool default 0, PRIMARY KEY (id))"


def updateStudentsStatus(mydb, cursor, data):
	sql = "UPDATE attenders set status = %s WHERE username = %s"
	cursor.execute(sql, data)
	mydb.commit()
	print(cursor.rowcount, "student(s) affected.")

