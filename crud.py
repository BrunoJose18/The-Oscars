import sqlite3 as con
#CRUD
def coletar_dados_ator():
    perguntas = {
        "nome": "Digite o nome do(a) Ator/Atriz: ",
        "ano_nasc": "Digite o ano de nascimento do(a) Ator/Atriz: ",
        "data_nasc": "Digite a data de nascimento do(a) Ator/Atriz: ",
        "local_nasc": "Digite o local de nascimento do(a) Ator/Atriz: ",
        "raca_etnia": "Digite a raça/etnia do(a) Ator/Atriz: ",
        "religiao": "Digite a religião do(a) Ator/Atriz: ",
        "orientacao_sexual": "Digite a orientação sexual do(a) Ator/Atriz: ",
        "ano_edicao": "Digite o ano de edição do filme: ",
        "categoria": "Digite a categoria do Oscar: ",
        "filme": "Digite o nome do filme: "
    }

    campos_inteiros = {"ano_nasc", "ano_edicao"}
    respostas = {}

    for chave, pergunta in perguntas.items():
        entrada = input(pergunta)
        respostas[chave] = int(entrada) if chave in campos_inteiros else entrada

    return respostas

def inserir_info_ator_oscar(dados):
    conexao = con.connect("bd_oscar")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO Oscar
        (nome, ano_nasc, data_nasc, local_nasc, raca_etnia, religiao,
         orientacao_sexual, ano_edicao, categoria, filme)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (
            dados["nome"], dados["ano_nasc"], dados["data_nasc"], dados["local_nasc"],
            dados["raca_etnia"], dados["religiao"], dados["orientacao_sexual"],
            dados["ano_edicao"], dados["categoria"], dados["filme"]
        ))
    conexao.commit()
    conexao.close()
    
    return cursor.lastrowid

     

#Teste de inserção de dados
#dados_ator = coletar_dados_ator()
#ator_id = inserir_info_ator_oscar(dados_ator)
#print(f"Ator/Atriz adicionado(a) com ID: {ator_id}")
     

def pesquisa_ator_por_id(ator_id):
  conexao = con.connect("bd_oscar")
  cursor = conexao.cursor()
  cursor.execute('''SELECT * FROM Oscar WHERE id = ?''',
                   (ator_id,))

  result = cursor.fetchone()

  print(f"\nResultados da busca:")
  if result:
      print(f"""
      ID: {result[0]}\n
      Nome: {result[1]}\n
      Ano de nascimento: {result[2]}\n
      Data de nascimento: {result[3]}\n
      Local de nascimento: {result[4]}\n
      Raça/Etnia: {result[5]}\n
      Religiao: {result[6]}\n
      Oritentação Sexual: {result[7]}\n
      Ano de edição do filme: {result[8]}\n
      Categoria do Oscar: {result[9]}\n
      Nome do filme: {result[10]}""")
  else:
      print("Usuario nao encontrado.")
  conexao.close()
     

#Teste de pesquisa por id
#ator_id = int(input("Digite o id do ator: "))
#pesquisa_ator_por_id(ator_id)
     

def pesquisa_ator_por_nome(nome):
  conexao = con.connect("bd_oscar")
  cursor = conexao.cursor()
  cursor.execute('''SELECT * FROM Oscar WHERE nome LIKE  ?''', ('%' + nome + '%',))
  result = cursor.fetchall()
  print(f"Busca por nome: '{nome}'")
  if result:
    for linha in result:
            print(f"""
ID: {linha[0]}
Nome: {linha[1]}
Ano de nascimento: {linha[2]}
Data de nascimento: {linha[3]}
Local de nascimento: {linha[4]}
Raça/Etnia: {linha[5]}
Religião: {linha[6]}
Orientação Sexual: {linha[7]}
Ano de edição do filme: {linha[8]}
Categoria do Oscar: {linha[9]}
Nome do filme: {linha[10]}
""")
            print("-" * 40)
  else:
    print("Ator/atriz não encontrado(a).")
  conexao.close()
     

#Teste de pesquisa por nome
#nome = input("Digite o nome do(a) ator/atriz: ")
#pesquisa_ator_por_nome(nome)
     

def dados_atualizado_ator():
    perguntas = {
        "ator_id" : "Digite o ID do(a) ator/atriz a ser atualizado: ",
        "nome": "Digite o nome do(a) Ator/Atriz: ",
        "ano_nasc": "Digite o ano de nascimento do(a) Ator/Atriz: ",
        "data_nasc": "Digite a data de nascimento do(a) Ator/Atriz: ",
        "local_nasc": "Digite o local de nascimento do(a) Ator/Atriz: ",
        "raca_etnia": "Digite a raça/etnia do(a) Ator/Atriz: ",
        "religiao": "Digite a religião do(a) Ator/Atriz: ",
        "orientacao_sexual": "Digite a orientação sexual do(a) Ator/Atriz: ",
        "ano_edicao": "Digite o ano de edição do filme: ",
        "categoria": "Digite a categoria do Oscar: ",
        "filme": "Digite o nome do filme: "
    }

    campos_inteiros = {"ator_id", "ano_nasc", "ano_edicao"}
    respostas = {}
    for chave, pergunta in perguntas.items():
        entrada = input(pergunta)
        respostas[chave] = int(entrada) if chave in campos_inteiros else entrada

    return respostas

def atualizar_ator(dados_atualizado):
    conexao = con.connect("bd_oscar")
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE Oscar
        SET nome = ?, ano_nasc = ?, data_nasc = ?, local_nasc = ?, raca_etnia = ?, religiao = ?, orientacao_sexual = ?, ano_edicao = ?, categoria = ?, filme = ?
        WHERE id = ?''',
        (
            dados_atualizado["nome"], dados_atualizado["ano_nasc"], dados_atualizado["data_nasc"], dados_atualizado["local_nasc"],
            dados_atualizado["raca_etnia"], dados_atualizado["religiao"], dados_atualizado["orientacao_sexual"],
            dados_atualizado["ano_edicao"], dados_atualizado["categoria"], dados_atualizado["filme"], dados_atualizado["ator_id"]
        ))
    conexao.commit()
    return cursor.rowcount
    conexao.close()
     

#Teste de atualização de dados
#dados_atualizado = dados_atualizado_ator()
#rows_updated = atualizar_ator(dados_atualizado)
#if rows_updated:
#    print(f"Ator/Atriz com ID {dados_atualizado['ator_id']} atualizado com sucesso.")
#else:
#    print(f"Nenhum usuario encontrado com ID {dados_atualizado['ator_id']}.")
     

def remover_ator(ator_id):
  conexao = con.connect("bd_oscar")
  cursor = conexao.cursor()
  cursor.execute('''DELETE FROM Oscar WHERE id = ?''', (ator_id,))
  conexao.commit()
  return cursor.rowcount
  conexao.close()
     

#Teste de remoção de ator/atriz
#ator_id = int(input("Digite o ID do ator/atriz a ser deletado: "))
#rows_deleted = remover_ator(ator_id)
#if rows_deleted:
#    print(f"Ator/Atriz com ID {ator_id} deletado com sucesso.")
#else:
#    print("Opção inválida. Tente novamente.")
     