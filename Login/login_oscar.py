
import sqlite3
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

janela = ctk.CTk() 

# Criando a janela principal
class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela_login()
        janela.mainloop()

    # Definindo o tema da aplicação
    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")  
    
    def tela_login(self):
        #trabalhando com a imagem da tela
        title_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha \na plataforma", font=("Roboto", 20), fg_color= "green", text_color="#000000")
        title_label.place(x=15, y=10)
        #Imagem 
        img = PhotoImage(file="ocar.png", width=500, height=500, master=janela) 
        label_img = ctk.CTkButton(master=janela, image=img, fg_color="#1a1a1a",text = None, hover = False,)
        label_img.place(x=-15, y=0)

        # Configurações da janela
        janela.resizable(False, False) #Desabilitando o redimensionamento da janela
        janela.geometry("896x410") #Tamanho da janela
        janela.title("Login-in")    #Titulo da janela
        janela.iconbitmap("oscares.ico")  # Ícone da janela
        
        #frame  
        login_frame = ctk.CTkFrame(master=janela, width=400, height=500, fg_color="#2B2B2B") 
        login_frame.pack(side=RIGHT)
        

        # widgets dentro do framde da tela de login
        label = ctk.CTkLabel(master= login_frame, text="Log in with your account", font=("Roboto", 30), text_color="#D8D8D8", width=350, height=80,) 
        label.place(x=25, y=5)

        #Caixa de texto para o usuário
        username_entry = ctk.CTkEntry(master= login_frame, placeholder_text="Username", width=300, font=("Roboto", 14)).place(x=50, y=105)   
        username_label = ctk.CTkLabel(master= login_frame, text="*O campo de usuário é de caratér obrigatório", text_color="green", font=("Roboto", 14)).place(x=50, y=135)
        #Caixa de texto para a senha
        password_entry = ctk.CTkEntry(master= login_frame, placeholder_text="Password", width=300, font=("Roboto", 14), show="*").place(x=50, y=165)
        password_label = ctk.CTkLabel(master= login_frame, text="*O campo de senha é de caratér obrigatório", text_color="green", font=("Roboto", 14)).place(x=50, y=195)
        senha_visivel = False
        def alternar_senha():
            global senha_visivel
            senha_visivel = not senha_visivel
            if senha_visivel:
                password_entry.configure(show="")  # mostra a senha
                toggle_button.configure(text="Ocultar")
            
            else:
                password_entry.configure(show="*")  # oculta a senha
                toggle_button.configure(text="Mostrar")

            #Botão de alternar visibilidade
                toggle_button = ctk.CTkButton(login_frame, text="Mostrar", command=alternar_senha)
                toggle_button.place(x=100, y=165)

        #checkbox para lembrar o usuário
        checkbox = ctk.CTkCheckBox(master= login_frame, text="Lembrar-se de mim", font=("Roboto", 16)).place(x=50, y=225)

        def login():
            # Aqui você pode adicionar a lógica de autenticação do usuário
            # Exemplo de mensagem de sucesso
                msg = messagebox.showinfo(title="Login", message="Login realizado com sucesso!")
                
            # Aqui você pode adicionar a lógica para verificar o usuário e senha
                pass

        login_button = ctk.CTkButton(master= login_frame, text="Login", width=300, fg_color="#396581", command=login).place(x=50, y=260)
        
        # Função para abrir a tela de registro
        def tela_register():

            #Remover o Frame do Login
            login_frame.pack_forget()
            #Criando tela de cadastro dos usuários
            rg_frame = ctk.CTkFrame(master=janela, width=400, height=500, fg_color="#333333")
            rg_frame.pack(side=RIGHT) 
            # widgets dentro do frame de registro
            label = ctk.CTkLabel(master= rg_frame, text="Create our Account", font=("Roboto", 30), text_color="#D8D8D8", width=350, height=80,)
            label.place(x=25, y=5)

            #Criando os campos de entrada de dados
            username2_entry = ctk.CTkEntry(master= rg_frame, placeholder_text="Username", width=300, font=("Roboto", 15)).place(x=50, y=95)

            email_entry = ctk.CTkEntry(master= rg_frame, placeholder_text="Email", width=300, font=("Roboto", 15), ).place(x=50, y=135)

            password2_entry = ctk.CTkEntry(master= rg_frame, placeholder_text="Password", width=300, font=("Roboto", 15), show= "*").place(x=50, y=175)

            cPass_entry = ctk.CTkEntry(master= rg_frame, placeholder_text="Confirm password", width=300, font=("Roboto", 15), show= "*").place(x=50, y=215)

            checkbox = ctk.CTkCheckBox(master= rg_frame, text="Aceitos todos os termos e políticas", font=("Roboto", 16)).place(x=50, y=255)
            # Função para voltar para a tela de login
            def back():
                #Remover o Frame de Registro
                rg_frame.pack_forget()

                #Voltar para a tela de login
                login_frame.pack(side=RIGHT)

            back_button = ctk.CTkButton(master= rg_frame, text="Voltar", width=125, fg_color="#838282", hover_color="#4D4C4C", command=back).place(x=50, y=300)
            # Função para salvar o usuário
            def save_user():
                # Exemplo de mensagem de sucesso
                msg = messagebox.showinfo(title="Cadastro", message="Usuário cadastrado com sucesso!",)
                # Aqui você pode adicionar a lógica para salvar o usuário no banco de dados

            # Botão para salvar o usuário
            save_button = ctk.CTkButton(master= rg_frame, text="CADASTRAR", width=170, fg_color="#0B8800", hover_color= "#123A00", command=save_user).place(x=180, y=300)
            # Botão para abrir a tela de registro
            
        register_span = ctk.CTkLabel(master= login_frame, text="Não tem uma conta? ", font=("Roboto", 15), text_color="#FFFFFF").place(x=50, y=305)
        register_button = ctk.CTkButton(master= login_frame, text="Registre-se", width=150, font=("Roboto", 15), fg_color= "#0F6822", command= tela_register).place(x=200, y=305)

        def sair():
            # Função para sair da aplicação
            janela.destroy() 
        sair_button = ctk.CTkButton(master= login_frame, text="Sair", width=20, font=("Roboto", 15), fg_color= "#440707", command=sair, hover_color= "#270505").place(x=45, y=340,)
        # Botão para alternar a visibilidade da senha
        
        show_button = ctk.CTkButton(login_frame, text="Show", command=alternar_senha, width= 10, font=("Roboto", 12), fg_color="#4D4D4D", hover_color="#6B6B6B")
        # Posicionando o botão de alternar visibilidade
        show_button.place(x=350, y=165)


Application()