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
    try:
        sql = f'INSERT INTO produto (nome, quantidade, valor) VALUES ("{nome}", {quantidade}, {valor})'
        c.execute(sql)
        db.commit()
    
    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')


# READ
def readAll():
    sql = f'SELECT * FROM produto'
    c.execute(sql)
    result = c.fetchall()
    print(result)

def readById(id):
    try:
        sql = f'SELECT * FROM produto WHERE idproduto = {id}'
        c.execute(sql)
        result = c.fetchall()
        print(result)
    
    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')



# UPDATE
def updateName(id, nome):
    try:
        sql = f'UPDATE produto SET nome = "{nome}" WHERE idproduto = {id}'    
        c.execute(sql)
        db.commit()
    
    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')

def updatePrice(id, valor):
    try:
        sql = f'UPDATE produto SET valor = {valor} WHERE idproduto = {id}'
        c.execute(sql)
        db.commit()
    
    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')

def updateQuantity(id, quantidade):
    try:
        sql = f'UPDATE produto SET quantidade = {quantidade} WHERE idProduto = {id}'
        c.execute(sql)
        db.commit()

    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')

# DELETE
def delete(id):
    try:
        sql = f'DELETE FROM produto WHERE idproduto = {id}'
        c.execute(sql)
        db.commit()
    
    except Exception as e:
        print(f'SOMETHING WENT WRONG: {e}')


# Tests
#addProduto("panela", 2, 35)
#addProduto("tampa", 2, 7.50)
#readAll()
#readById(1)
#readById(2)
#updateName(2, "facão")
#updatePrice(1, 37.90)
#updateQuantity(1, 4)
#delete(2)
#readById("adsd")


c.close()
db.close()