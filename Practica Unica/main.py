from turtle import pd

import leerJSON
import menu

if __name__ == '__main__':
    comando = None
    while comando != "salir":
        print("--------------------------------------------------------------------------------")
        menu.menu()
        comando = input()
        menu.identificarComando(comando)
        print("--------------------------------------------------------------------------------")

