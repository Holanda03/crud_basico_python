import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='123456',
    database='crudbasic',
)

c = db.cursor()

# Connection test
c.execute("SELECT CURDATE()")
row = c.fetchone()
print("Current Date: {0}".format(row[0]))


c.close()
db.close()