#TESTE DE INTERFACE
import tkinter

from tkinter import *

app = Tk()
app.title("Cadastro Zero")
app.geometry('500x200+100+100')

b1 = Button(app, text = "Entrar", width = 20)
b1.pack(side = 'left', padx = 20, pady = 20)

b2 = Button (app, text = "Sair", width = 20)
b2.pack(side = 'right', padx = 20, pady = 20)

app.mainloop() 
