import EscribirHTML
import webbrowser


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    Wilmer = EscribirHTML.Persona('Wilmer', 22, 'si', 500)
    Pablo = EscribirHTML.Persona('Pablo', 32, 'si', 5000)
    Gerardo = EscribirHTML.Persona('Gerardo', 18, 'no', 1500)
    Alejandro = EscribirHTML.Persona('Alejandro', 21, 'si', 100)
    Eduardo = EscribirHTML.Persona('Eduardo', 20, 'no', 400)
    David = EscribirHTML.Persona('David', 35, 'si', 5100)
    Noe = EscribirHTML.Persona('Noe', 25, 'si', 200)
    Pedro = EscribirHTML.Persona('Pedro', 17, 'no', 600)
    Luis = EscribirHTML.Persona('Luis', 30, 'no', 400)
    Manuel = EscribirHTML.Persona('Manuel', 27, 'si', 100)

    lista = {Wilmer, Pablo, Gerardo, Alejandro, Eduardo, David, Noe, Pedro, Luis, Manuel}

    EscribirHTML.escribirHTML(lista)
