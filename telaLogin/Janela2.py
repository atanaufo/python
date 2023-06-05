# Para utilizar o customtkinter deverá ser instalado via terminal:
# pip install customtkinter
import tkinter

import customtkinter

customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Botão pressionado")


texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digita sua senha", show="*")
senha.pack(padx=10, pady=10)

checagem = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checagem.pack(padx=10,pady=10)

botao = customtkinter.CTkButton(janela, text="Login ...", command=clique)
botao.pack(padx=10, pady=10, anchor=tkinter.CENTER)



janela.mainloop()




