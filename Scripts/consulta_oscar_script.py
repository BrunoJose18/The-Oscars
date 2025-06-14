import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Janela principal
janela = ctk.CTk()
janela.title("Consulta de Atores Premiados")
janela.geometry("800x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# === Funções ===

def abrir_formulario_adicionar():
    janela_add = ctk.CTkToplevel(janela)
    janela_add.title("Adicionar Ator")
    janela_add.geometry("500x500")

    ctk.CTkLabel(janela_add, text="Registrar Novo Ator", font=("Roboto", 20, "bold")).pack(pady=10)

    frame = ctk.CTkFrame(janela_add)
    frame.pack(pady=10)

    ctk.CTkLabel(frame, text="Nome do Ator/Atriz:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = ctk.CTkEntry(frame, width=200)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame, text="Filme:").grid(row=1, column=0, padx=5, pady=5)
    entry_filme = ctk.CTkEntry(frame, width=200)
    entry_filme.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame, text="Categoria:").grid(row=2, column=0, padx=5, pady=5)
    entry_categoria = ctk.CTkEntry(frame, width=200)
    entry_categoria.grid(row=2, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame, text="Ano:").grid(row=3, column=0, padx=5, pady=5)
    entry_ano = ctk.CTkEntry(frame, width=200)
    entry_ano.grid(row=3, column=1, padx=5, pady=5)

    def salvar_dados():
        nome = entry_nome.get().strip()
        filme = entry_filme.get().strip()
        categoria = entry_categoria.get().strip()
        ano = entry_ano.get().strip()

        if not (nome and filme and categoria and ano):
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        conn = sqlite3.connect("oscar.db")
        cursor = conn.cursor()

        # Verificar se o filme já existe
        cursor.execute("SELECT id FROM Filmes WHERE LOWER(titulo) = LOWER(?)", (filme,))
        resultado = cursor.fetchone()

        if resultado:
            filme_id = resultado[0]
        else:
            cursor.execute("INSERT INTO Filmes (titulo, pais_origem) VALUES (?, ?)", (filme, "Desconhecido"))
            filme_id = cursor.lastrowid

        cursor.execute("INSERT INTO Premiacoes (nome_premiado, filme_id, categoria, ano, vencedor, nome_premiacao) VALUES (?, ?, ?, ?, 1, 'Oscar')", (nome, filme_id, categoria, ano))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Ator/Atriz adicionado com sucesso!")
        janela_add.destroy()

    ctk.CTkButton(janela_add, text="Salvar", command=salvar_dados, fg_color="#4CAF50").pack(pady=10)
def buscar_ator():
    nome = entry_ator.get()

    if not nome.strip():
        messagebox.showwarning("Atenção", "Digite o nome de um ator ou atriz.")
        return

    conn = sqlite3.connect("oscar.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Premiacoes.nome_premiado, Filmes.titulo, Premiacoes.categoria, Premiacoes.ano
        FROM Premiacoes
        JOIN Filmes ON Premiacoes.filme_id = Filmes.id
        WHERE LOWER(Premiacoes.nome_premiado) = LOWER(?)
        ORDER BY Premiacoes.ano ASC
    """, (nome,))
    resultados = cursor.fetchall()
    conn.close()

    if not resultados:
        messagebox.showerror("Erro", "Ator/Atriz não encontrado(a).")
        label_resultado.configure(text="")
        return

    texto = f"\n🎭 Nome: {nome}\n"
    texto += f"🏆 Total de prêmios: {len(resultados)}\n"
    texto += "\nDetalhes:\n"
    for nome, filme, categoria, ano in resultados:
        texto += f"🎬 Filme: {filme} | 🏆 Categoria: {categoria} | 📅 Ano: {ano}\n"

    label_resultado.configure(text=texto)

def abrir_consulta_avancada():
    janela_avancada = ctk.CTkToplevel(janela)
    janela_avancada.title("Consulta Avançada")
    janela_avancada.geometry("700x500")

    ctk.CTkLabel(janela_avancada, text="Consulta Avançada de Premiações", font=("Roboto", 20, "bold")).pack(pady=10)

    frame_filtros = ctk.CTkFrame(janela_avancada)
    frame_filtros.pack(pady=10)

    ctk.CTkLabel(frame_filtros, text="Nome do Filme:").grid(row=0, column=0, padx=5, pady=5)
    entry_filme = ctk.CTkEntry(frame_filtros, placeholder_text="Ex: Parasite", width=180)
    entry_filme.grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_filtros, text="Categoria:").grid(row=1, column=0, padx=5, pady=5)
    entry_categoria = ctk.CTkEntry(frame_filtros, placeholder_text="Ex: Melhor Atriz", width=180)
    entry_categoria.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_filtros, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
    entry_ano = ctk.CTkEntry(frame_filtros, placeholder_text="Ex: 2020", width=180)
    entry_ano.grid(row=2, column=1, padx=5, pady=5)

    resultado_label = ctk.CTkLabel(janela_avancada, text="", font=("Roboto", 14))
    resultado_label.pack(pady=10)

    def executar_filtros():
        filme = entry_filme.get().strip().lower()
        categoria = entry_categoria.get().strip().lower()
        ano = entry_ano.get().strip()

        query = """
            SELECT Premiacoes.nome_premiado, Filmes.titulo, Premiacoes.categoria, Premiacoes.ano
            FROM Premiacoes
            JOIN Filmes ON Premiacoes.filme_id = Filmes.id
            WHERE 1=1
        """
        params = []

        if filme:
            query += " AND LOWER(Filmes.titulo) LIKE ?"
            params.append(f"%{filme}%")
        if categoria:
            query += " AND LOWER(Premiacoes.categoria) LIKE ?"
            params.append(f"%{categoria}%")
        if ano:
            query += " AND Premiacoes.ano = ?"
            params.append(ano)

        conn = sqlite3.connect("oscar.db")
        cursor = conn.cursor()
        cursor.execute(query, tuple(params))
        resultados = cursor.fetchall()
        conn.close()

        if not resultados:
            resultado_label.configure(text="Nenhum resultado encontrado.")
        else:
            texto = "\n".join([f"🎭 {nome} - 🎬 {filme} - 🏆 {categoria} - 📅 {ano}" for nome, filme, categoria, ano in resultados])
            resultado_label.configure(text=texto)

    ctk.CTkButton(janela_avancada, text="Filtrar", command=executar_filtros).pack(pady=10)

# === Interface Principal ===

def listar_atores():
    janela_lista = ctk.CTkToplevel(janela)
    janela_lista.title("Atores Registrados")
    janela_lista.geometry("400x400")

    ctk.CTkLabel(janela_lista, text="Atores Registrados", font=("Roboto", 18, "bold")).pack(pady=10)

    conn = sqlite3.connect("oscar.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nome_premiado FROM Premiacoes ORDER BY nome_premiado ASC")
    nomes = cursor.fetchall()
    conn.close()

    for nome in nomes:
        ctk.CTkLabel(janela_lista, text=f"🎭 {nome[0]}", font=("Roboto", 14)).pack(pady=2)
titulo_label = ctk.CTkLabel(janela, text="Consulta de Atores Premiados", font=("Roboto", 22, "bold"))
titulo_label.pack(pady=10)

frame_input = ctk.CTkFrame(janela)
frame_input.pack(pady=10)

ctk.CTkLabel(frame_input, text="Nome do Ator/Atriz:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_ator = ctk.CTkEntry(frame_input, width=300, font=("Roboto", 14))
entry_ator.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkButton(janela, text="Buscar", command=buscar_ator, fg_color="#4CAF50").pack(pady=5)
ctk.CTkButton(janela, text="Consulta Avançada", command=abrir_consulta_avancada, fg_color="#145da1").pack(pady=5)

label_resultado = ctk.CTkLabel(janela, text="", font=("Roboto", 14), justify="left")
label_resultado.pack(pady=10)

ctk.CTkButton(janela, text="Adicionar Ator", command=abrir_formulario_adicionar, fg_color="#888888").pack(pady=5)
ctk.CTkButton(janela, text="Atores Registrados", command=listar_atores, fg_color="#777777").pack(pady=5)

janela.mainloop()
