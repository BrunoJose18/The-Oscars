import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk  # necessário para o Canvas

class Application():
    
    def __init__(self):
        self.janela = ctk.CTk()
        self.tema()
        self.configurar_janela()
        self.criar_widgets()
        self.mostrar_mapa()

    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")     

    def configurar_janela(self):
        self.janela.resizable(False, False)
        self.janela.geometry("1200x700")
        self.janela.title("The Oscars - Mapa")

    def combobox_callback(self, choice):
        print("Selecionado:", choice)
        self.destacar_regiao(choice)

    def criar_widgets(self):
        frame = ctk.CTkFrame(self.janela)
        frame.pack(pady=50)

        label1 = ctk.CTkLabel(frame, text="Categoria:")
        label1.grid(row=0, column=0, padx=10)

        self.combo_categoria = ctk.CTkComboBox(frame, 
                                               values=["Ator", "Atriz", "Todos"],
                                               command=self.combobox_callback)
        self.combo_categoria.set("Ator")
        self.combo_categoria.grid(row=0, column=1, padx=10)

        label2 = ctk.CTkLabel(frame, text="Continente:")
        label2.grid(row=0, column=2, padx=10)

        self.combo_continente = ctk.CTkComboBox(frame, 
                                                values=["América do Sul", "América Central", "América do Norte", "Ásia", "África", "Europa", "Oceania"],
                                                command=self.combobox_callback)
        self.combo_continente.set("América do Sul")
        self.combo_continente.grid(row=0, column=3, padx=10)

    def mostrar_mapa(self):
        try:
            self.imagem_original = Image.open("mapamundi.jpg").resize((700, 448))
            self.tk_image = ImageTk.PhotoImage(self.imagem_original)

            self.canvas = tk.Canvas(self.janela, width=700, height=448, bg="black", highlightthickness=0)
            self.canvas.pack()
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        except Exception as e:
            print("Erro ao carregar o mapa:", e)

    def run(self):
        self.janela.mainloop()

app = Application()
app.run()
