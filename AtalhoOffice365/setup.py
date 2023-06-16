import sys
from cx_Freeze import setup, Executable

# As dependências são detectadas automaticamente, mas podem exigir um ajuste:
# para excluir algum módulo, acrescentar no parâmetro abaixo: "excludes": ["tkinter"]
# para incluir algum módulo, acrescentar no parâmetro abaixo: "includes": ["tkinter"]
build_exe_options = {"packages": ["os"],
                     "excludes": ['http']
                     }

# Interface grática somente descomentar, caso contrário será via Console:
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name="Acesso Microsoft 365",
    version="0.1",
    description="Para ter acesso Microsoft 365 gratuito",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
