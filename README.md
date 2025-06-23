## 📦 Plataforma Oscar — CRUD e Visualização do Mapa-Múndi

Este repositório contém scripts para gerenciar dados de atores e atrizes vencedores do Oscar, 
além de uma interface gráfica para visualizar um mapa-múndi interativo com filtros por categoria e continente. 
O sistema utiliza um banco de dados SQLite para armazenar informações sobre filmes e premiações, permitindo operações de CRUD (Criar, Ler, Atualizar e Deletar) e consultas avançadas.

### Projeto realizado pelos seguintes alunos dos cursos de T.I da Unifavip Wyden:

*  Bruno José Barboza - 202408755813
*  Italo Soares Santos - 202408162073
*  João Luiz Pereira Filho - 202402973614
*  Arthur Batista Braga - 202403124386

## SEÇÃO 1 (ARQUIVOS DOS BANCOS DE DADOS):

## 📁 Arquivo: `banco.py`

### Objetivo

Este módulo lida com a criação da base de dados `bd_oscar` e a inserção de dados provenientes de um arquivo CSV (`oscar.csv`) com informações sobre vencedores do Oscar.

### Funções

#### `criar_conexao(nome_banco='bd_oscar')`

* **Descrição**: Estabelece uma conexão com o banco de dados SQLite especificado.
* **Parâmetros**: `nome_banco` *(str)* – nome do arquivo do banco de dados.
* **Retorno**: Objeto de conexão SQLite.

#### `carregar_csv_e_criar_tabela(caminho_csv='oscar.csv')`

* **Descrição**:

  1. Carrega dados de um arquivo CSV.
  2. Renomeia colunas para nomes mais amigáveis.
  3. Cria uma tabela chamada `Oscar` no banco de dados (se não existir).
  4. Insere os dados do CSV na tabela.
* **Parâmetros**: `caminho_csv` *(str)* – caminho para o arquivo CSV.
* **Requisitos**: Pandas, SQLite.

---

## 📁 Arquivo: `user_banco.py`

### Objetivo

Este script gerencia a criação de um banco de dados separado (`Usuario`) e define a tabela `Usuarios`, que pode ser usada para controle de acesso, autenticação, etc.

### Estrutura do Banco

* **Tabela**: `Usuarios`

  * `id` (chave primária)
  * `nome` (texto, obrigatório)
  * `email` (texto, obrigatório)
  * `senha` (texto, obrigatório)

### Funções

#### `criar_conexao_usuario(nome_banco='Usuario')`

* **Descrição**: Retorna uma conexão com o banco de dados dos usuários.

#### `criar_tabela_usuario()`

* **Descrição**: Cria a tabela `Usuarios` caso ela ainda não exista.

---

## 📁 Arquivo: `criar_banco.py`

### Objetivo

Este script inicializa um banco de dados `oscar.db` contendo informações sobre filmes e premiações, com estrutura relacional entre as tabelas `Filmes` e `Premiacoes`.

### Estrutura das Tabelas

#### Tabela: `Filmes`

* `id`: chave primária
* `titulo`: nome do filme
* `pais_origem`: país de origem do filme

#### Tabela: `Premiacoes`

* `id`: chave primária
* `nome_premiacao`: nome da premiação
* `ano`: ano da premiação
* `categoria`: categoria da premiação
* `vencedor`: booleano indicando se foi vencedor
* `filme_id`: chave estrangeira referenciando `Filmes(id)`

### Fluxo

1. Conecta ao banco `oscar.db`.
2. Cria as tabelas `Filmes` e `Premiacoes` com as devidas relações.
3. Fecha a conexão e imprime mensagem de sucesso.

## SEÇÂO 2 (SCRIPTS):


---

## 🔐 login_oscar.py — Tela de Login e Cadastro

### Descrição
Este script é responsável pela tela de autenticação do usuário, com login e criação de conta. Ele se conecta a um banco SQLite e oferece uma interface intuitiva.

### Funcionalidades

- Login com verificação no banco de dados
- Cadastro de novos usuários
- Alternância de visibilidade da senha
- Mensagens de feedback ao usuário
- Interface com tema escuro e imagens personalizadas

### Componentes principais

- `username_entry`, `password_entry`: campos de entrada
- `login()`: verifica se o usuário está registrado
- `tela_register()`: abre a tela de cadastro
- `save_user()`: registra novo usuário no banco
- `toggle_button`: alterna visibilidade da senha

### Banco de Dados

- Tabela: `Usuarios`
- Campos: `nome`, `email`, `senha`
- Operações: `SELECT`, `INSERT`

---

## 🏁 Tela de inicio.py — Tela Inicial da Plataforma

### Descrição
Exibe a interface inicial da aplicação após o login. Oferece botões para acessar futuras funcionalidades como a lista de ganhadores e as estatísticas por continente.

### Funcionalidades

- Exibição de imagem de fundo personalizada
- Botões para:
  - Lista de ganhadores
  - Estatísticas mundiais
- Mensagens simuladas via `messagebox`
- Layout centralizado com `CustomTkinter`

### Componentes principais

- `label1`: título da tela
- `lista()`: placeholder para abrir a lista de ganhadores
- `mapa_mundi()`: placeholder para abrir o mapa com estatísticas
- `back_button`: botão para retornar à tela de login

---

## ✅ Requisitos

- Python 3.8+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- `sqlite3` (biblioteca padrão)
- Diretório `Src/` com as imagens:
  - `ocar.png`
  - `lista.png`
  - `mundio.png`
  - `oscares.ico`

---

### `crud.py` — Operações CRUD no Banco de Dados SQLite

Este script implementa funções para criar, ler, atualizar e buscar informações sobre atores/atrizes no banco de dados `bd_oscar`.

#### Funcionalidades:

- Coleta de dados do ator/atriz via terminal
- Inserção de novos registros na tabela `Oscar`
- Pesquisa de registros por ID
- Pesquisa de registros por nome (busca parcial)
- Atualização de registros existentes pelo ID

#### Estrutura dos dados armazenados:

| Campo             | Descrição                         |
|-------------------|---------------------------------|
| id (automático)   | Identificador único              |
| nome              | Nome do ator/atriz               |
| ano_nasc          | Ano de nascimento (inteiro)     |
| data_nasc         | Data completa de nascimento     |
| local_nasc        | Local de nascimento             |
| raca_etnia        | Raça/Etnia                      |
| religiao          | Religião                       |
| orientacao_sexual | Orientação sexual               |
| ano_edicao        | Ano de edição do Oscar (inteiro)|
| categoria         | Categoria do Oscar              |
| filme             | Nome do filme                  |

---

### `mapa.py` — Interface Gráfica do Mapa-Múndi com Filtros

Aplicação gráfica feita com `CustomTkinter` que exibe um mapa-múndi e oferece filtros para seleção de categoria (Ator, Atriz, Todos) e continente.

#### Funcionalidades:

- Janela fixa (1200x700), tema escuro com cor azul
- Combobox para seleção de categoria
- Combobox para seleção de continente
- Exibição da imagem do mapa (`Src/mapamundi.jpg`) em um canvas do Tkinter
- Callback para ação ao selecionar uma opção (no momento, imprime no console e chama método `destacar_regiao` que pode ser implementado)

#### Requisitos:

- Imagem do mapa no caminho `Src/mapamundi.jpg`
- Ícone da aplicação em `Src/oscares.ico`
- Bibliotecas: `customtkinter`, `PIL` (Pillow), `tkinter` (padrão Python)

---

## ⚙️ Como usar

### Para o `crud.py`:

- Execute o script ou importe as funções em outro módulo
- Use as funções para coletar dados, inserir, buscar e atualizar atores/atrizes
- Exemplo rápido para inserir dados:

```python
from crud import coletar_dados_ator, inserir_info_ator_oscar

dados = coletar_dados_ator()
id_inserido = inserir_info_ator_oscar(dados)
print(f"Ator/Atriz inserido com ID {id_inserido}")

Aqui está uma documentação que você pode adicionar ao README do seu repositório no GitHub. Esta documentação descreve cada um dos scripts, suas funcionalidades e como utilizá-los.

---
### `importar_dados.py`

Este script é responsável por importar dados de um arquivo CSV compactado contendo informações sobre os vencedores do Oscar e armazená-los em um banco de dados SQLite.

#### Funcionalidades:
- Abre um arquivo CSV compactado (`world_ampas_oscar_winner_demographics.csv.gz`).
- Conecta ao banco de dados SQLite (`oscar.db`).
- Limpa valores nulos e evita duplicatas.
- Insere informações sobre filmes e premiações no banco de dados.

#### Uso:
Execute o script para importar os dados para o banco de dados:
```bash
python importar_dados.py
```

### `listar_filmes.py`

Este script lista os primeiros 20 filmes armazenados no banco de dados.

#### Funcionalidades:
- Conecta ao banco de dados SQLite (`oscar.db`).
- Executa uma consulta para selecionar os títulos dos filmes.

#### Uso:
Execute o script para visualizar os filmes:
```bash
python listar_filmes.py
```

### `consulta_oscar_script.py`

Este script fornece uma interface gráfica para consultar informações sobre atores premiados.

#### Funcionalidades:
- Permite adicionar novos atores e suas premiações.
- Permite buscar informações sobre um ator específico.
- Oferece uma consulta avançada com filtros por filme, categoria e ano.
- Lista todos os atores registrados.

#### Uso:
Execute o script para abrir a interface gráfica:
```bash
python consulta_oscar_script.py
```

### `grafico.py`

Este script gera um gráfico interativo utilizando a biblioteca Plotly, mostrando a quantidade de vencedores do Oscar por continente.

#### Funcionalidades:
- Cria um gráfico de linha com dados sobre vencedores do Oscar.
- Exibe o gráfico em uma nova janela.

#### Uso:
Execute o script para visualizar o gráfico:
```bash
python grafico.py
```

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install pandas sqlite3 customtkinter plotly pillow
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório, crie uma nova branch e envie um pull request.
