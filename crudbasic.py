import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='123456',
    database='crudbasic',
)

c = db.cursor()

# Connection test
#c.execute("SELECT CURDATE()")
#row = c.fetchone()
#print("Current Date: {0}".format(row[0]))


# CREATE
def addProduto(nome, quantidade, valor):
    sql = f'INSERT INTO produto (nome, quantidade, valor) VALUES ("{nome}", {quantidade}, {valor})'
    c.execute(sql)
    db.commit()

# READ
def readAll():
    sql = f'SELECT * FROM produto'
    c.execute(sql)
    result = c.fetchall()
    print(result)


# Tests
#addProduto("panela", 2, 35)
#addProduto("tampa", 2, 7.50)
#readAll()


c.close()
db.close()