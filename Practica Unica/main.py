from turtle import pd

import leerJSON
import menu

if __name__ == '__main__':
    menu.menu()
    # texto = "Seleccionar nombre,apellido,carne,edad dOnde edad=20"
    # menu.separarSelecciones(texto)


    menu.separarArchivos("cargar archivo1.json,archivo2.json,archivo3.json")
    for persona in leerJSON.datosPersonas:
        print("Persona ")
        print("Nombre  : ", persona.getNombre())
        print("Edad    : ", persona.getEdad())
        print("Activo  : ", persona.getActivo())
        print("Promedio: ", persona.getPromedio())
        print("\n")
