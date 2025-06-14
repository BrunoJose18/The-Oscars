import sqlite3 as con

#Realizando a conexão ao BD e criação do cursor
conexao = con.connect('Usuario')
cursor = conexao.cursor()

#Função para conexão da tabela Usuario
def criar_conexao_usuario(nome_banco='Usuario'):
    return con.connect(nome_banco)

#Criando a tabela do usuário
def criar_tabela_usuario():
    conexao = criar_conexao_usuario()
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   senha TEXT NOT NULL)''')
    conexao.commit()
    cursor.close()
    conexao.close()



