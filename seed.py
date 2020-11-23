import mysql.connector
import constant

mydb = mysql.connector.connect(
    host=constant.dbInfor["host"],
    user=constant.dbInfor["user"],
    password=constant.dbInfor["password"],
    database=constant.dbInfor["database"]
)

mycursor = mydb.cursor()

mycursor.execute(
    "insert into attenders (name, username) values ('Bao Huy', 'huy')")
mycursor.execute(
    "insert into attenders (name, username) values ('Phuc Thinh', 'tonyngu')")
mycursor.execute(
    "insert into attenders (name, username) values ('Quang Truong Ne', 'truong')")


mydb.commit()
