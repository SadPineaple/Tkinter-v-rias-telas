from tkinter import *

def tela1():
    frame2.place_forget()
    frame1.place(width=500, height=400)

def tela2():
    frame1.place_forget()
    frame2.place(width=500, height=400)

def voltar():
    frame1.place_forget()
    frame2.place_forget()



#Tela Principal
Janela = Tk()
Janela.geometry("500x400+700+200")
#Estrutura da Tela Principal
Label(Janela, text="Tela Principal").pack(pady=20)
Button(text="Tela1", command = tela1).pack()
Button(text="Tela2", command = tela2).pack(pady=10)
#----------------------------------------------------
#Criando As Telas

frame1 = Frame(Janela, bg="blue")


Button(frame1, text="Voltar", command=voltar).pack()

frame2 = Frame(Janela, bg="black")


Button(frame2, text="Voltar", command=voltar).pack()

Janela.mainloop()