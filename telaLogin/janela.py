import tkinter

janela = tkinter.Tk()
janela.geometry("500x300")

def clique():
    print("Fazer Login ....... ")

texto = tkinter.Label(janela, text="Fazer login")
texto.pack(padx=10,pady=10)

botao = tkinter.Button(janela, text="Login", command=clique)
botao.pack(padx=20,pady=20)

janela.mainloop()


