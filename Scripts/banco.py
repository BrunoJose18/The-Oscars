import sqlite3
import pandas as pd

#Função para se conectar ao banco
def criar_conexao(nome_banco='bd_oscar'):
    return sqlite3.connect(nome_banco)

#Carregando as informações do CSV, criando uma tabela e adicionando nela os dados do CSV
def carregar_csv_e_criar_tabela(caminho_csv='oscar.csv'):
    df = pd.read_csv(caminho_csv)

    df.rename(columns={
        'name': 'nome',
        'birth_year': 'ano_nasc',
        'birth_date': 'data_nasc',
        'birthplace': 'local_nasc',
        'race_ethnicity': 'raca_etnia',
        'religion': 'religiao',
        'sexual_orientation': 'orientacao_sexual',
        'year_edition': 'ano_edicao',
        'category': 'categoria',
        'movie': 'filme'
    }, inplace=True)

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Oscar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            ano_nasc INTEGER,
            data_nasc TEXT,
            local_nasc TEXT,
            raca_etnia TEXT,
            religiao TEXT,
            orientacao_sexual TEXT,
            ano_edicao INTEGER,
            categoria TEXT,
            filme TEXT
        )
    ''')

    df.to_sql('Oscar', conexao, if_exists='append', index=False)
    conexao.commit()
    conexao.close()