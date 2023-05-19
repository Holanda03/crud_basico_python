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

def readById(id):
    sql = f'SELECT * FROM produto WHERE idproduto = {id}'
    c.execute(sql)
    result = c.fetchall()
    print(result)


# UPDATE
def updateName(id, nome):
    sql = f'UPDATE produto SET nome = "{nome}" WHERE idproduto = {id}'    
    c.execute(sql)
    db.commit()


# Tests
#addProduto("panela", 2, 35)
#addProduto("tampa", 2, 7.50)
#readAll()
#readById(1)
#readById(2)
updateName(2, "facão")


c.close()
db.close()