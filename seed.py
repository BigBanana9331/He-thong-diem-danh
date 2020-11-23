import mysql.connector
import constant

mydb = mysql.connector.connect(
    host=constant.dbInfor["host"],
	user=constant.dbInfor["user"],
	password=constant.dbInfor["password"],
	database=constant.dbInfor["database"]
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS students (id int(11) NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL UNIQUE, username VARCHAR(255) NOT NULL UNIQUE, status bool default 0, PRIMARY KEY (id))")
mycursor.execute("insert into students (name, username) values ('Bao Huy', 'huy')")
mycursor.execute("insert into students (name, username) values ('Phuc Thinh', 'tonyngu')")
mycursor.execute("insert into students (name, username) values ('Quang Truong Ne', 'truong')")


mydb.commit()