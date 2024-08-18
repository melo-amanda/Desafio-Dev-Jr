import sqlite3

#Funções para manipular o Banco de Dados

#Criação da tabela de leitura (deve ser chamada apenas uma vez)
def create_table():
    conexao = sqlite3.connect("BancoDesafio")
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE leitura_sensor(id INTEGER PRIMARY KEY, timestamp TIMESTAMP, equipmentId VARCHAR(30), value FLOAT)')
    conexao.commit()
    conexao.close
    return

#Adiciona ao banco de dados novos dados
def update_table(equipmentId, timestamp, value):
    conexao = sqlite3.connect("BancoDesafio")
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO leitura_sensor(timestamp,equipmentId,value) VALUES(?,?,?)', (timestamp,equipmentId,value))
    conexao.commit()
    conexao.close
    return

#Seleciona os dados da tabela e os transforma em dicionário
def select_data():
    conexao = sqlite3.connect("BancoDesafio")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM leitura_sensor')
    rows = cursor.fetchall()

    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]

    conexao.commit()
    conexao.close
    return data