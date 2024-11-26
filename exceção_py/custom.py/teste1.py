import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Função que será chamada ao clicar no botão
def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá! Você clicou no botão.")

# Criar a janela principal
janela = tk.Tk()

# Definir título e tamanho da janela
janela.title("Teste Tkinter")
janela.geometry("300x200")

# Criar um botão
botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack(pady=50)  # Adiciona o botão na janela com um espaço superior

# Iniciar o loop principal
janela.mainloop()
