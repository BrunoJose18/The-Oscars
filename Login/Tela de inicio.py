import sqlite3  
import customtkinter as ctk
from tkinter import PhotoImage
from tkinter import *
from tkinter import messagebox  

janela = ctk.CTk() 


# Criando a janela principal
class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela_inicio()
        janela.mainloop()

    # Definindo o tema da aplicação
    def tema(self):    
        ctk.set_appearance_mode("sistem")  # Modo de aparência do sistema
        ctk.set_default_color_theme("dark-blue")    # Tema de cores padrão
    
    def tela_inicio(self):
        #Imagem de fundo
        img = PhotoImage(file="podio.png", master=janela, width=1000) 
        label_img = ctk.CTkButton(master=janela, image=img, fg_color="#1a1a1a",text = None, hover = False,)
        label_img.place(x=-15, y=0)
        #trabalhando com a imagem da tela
        
        # Configurações da janela
        janela.resizable(False, False) #Desabilitando o redimensionamento da janela
        janela.geometry("870x600") #Tamanho da janela
        janela.title("Tela Inicial")    #Titulo da janela
        janela.iconbitmap("oscares.ico")  # Ícone da janela
        
        #frame
        inicio_frame = ctk.CTkFrame(master= janela , width=400, height=370, fg_color="#313131",)
        inicio_frame.pack_propagate(False)  # Impede que o frame redimensione automaticamente
        inicio_frame.pack(pady=20, padx=20,) 
        inicio_frame.place(x=245, y=120,) # Posicionando o frame na janela
        # widgets dentro do frame da tela de login
        
        label1 = ctk.CTkLabel(master= inicio_frame, text="Escolha uma das opções \nabaixo para prosseguir ", font=("Helvetica", 30), text_color="#D8D8D8", width=350, height=80,) 
        label1.place(x=25, y=10)
        
        def lista():
            # Aqui você pode adicionar o código para abrir a lista de ganhadores
            msg = messagebox.showinfo(title= "Lista de Ganhadores", message= "Abrindo a lista de ganhadores...")
            pass
        
        
        #imagem do botão da lista de ganhadores
        label = ctk.CTkLabel(master= inicio_frame, text="LISTA DE GANHADORES ", font=("Helvetica", 18), text_color="#D8D8D8", width=100, height=50,anchor="center") 
        label.place(x=95, y= 95)
        img1 = PhotoImage(file="lista.png", width=25, height=50, master=janela)
        label_img = ctk.CTkButton(master=janela, image=img1, fg_color="#383838",text= None, hover_color= "#3C556D", anchor="center")
        label_img.place(x=365, y= 265)
        label_img.configure(command=lista)  # Configurando o comando do botão
        
        def mapa_mundi():
            # Aqui você pode adicionar o código para abrir o mapa mundi
            msg = messagebox.showinfo(title= "Mapa Mundi", message= "Abrindo as estatísticas mundiais...")
            pass
        #imagem do botão do mapa mundi
        inicio_frame.pack_propagate(False)
        label2 = ctk.CTkLabel(master= inicio_frame, text="ESTATÍSTICAS MUNDIAIS", font=("Helvetica", 18), text_color="#D8D8D8", width=100, height=50,anchor="center") 
        label2.place(x=90, y= 195)
        img2 = PhotoImage(file="mundio.png", width=100, height=50, master=janela,) 
        label_img2 = ctk.CTkButton(master=janela, image=img2, fg_color="#383838",text= None, hover_color= "#3C556D",anchor="center")
        label_img2.place(x=365, y=360)
        label_img2.configure(command=mapa_mundi) # Configurando o comando do botão

        
        
        
        back_button = ctk.CTkButton(master= inicio_frame, text="Retornar para \ntela de login", width=115, fg_color="#026623", hover_color="#042C16",).place(x=20, y=320)
        
        

Application()