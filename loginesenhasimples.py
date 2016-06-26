#TELA DE LOGIN E SENHA SIMPLES
from tkinter import *

telalogin = Tk()
telalogin.title("Login do Sistema")

lb1 = Label(telalogin, text="Usuário: ")
lb2 = Label(telalogin, text="senha: ")

entrada1 = Entry(telalogin,)
entrada2 = Entry(telalogin,)

botao = Button(telalogin, text="Login")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
entrada1.grid(row=0, column=1)
entrada2.grid(row=1, column=1)
botao.grid(row=2, column=1)

telalogin.geometry("250x80+150+150")

telalogin.mainloop()
