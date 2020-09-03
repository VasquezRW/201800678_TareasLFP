import re
import leerJSON


def menu():
    print("--------------SimpleQL--------------\n\n")
    print("* Para cargar archivos ingrese el comando seguido de la(s) ruta(s) de los archivos separdos por comas: "
          "CARGAR archivo1,archivo2....archivoN\n")
    print("* Para realizar una consulta ingrese el comando seguido de la(s) consulta(s) separadas por comas seguido "
          "de la condicion: "
          "SELECCIONAR atributo1,atributo2....atributoN DONDE atributo1=N \n")
    print("* Para consultar un valor maximo ingrese el comando seguido del atributo: "
          "MAXIMO atributo \n")
    print("* Para consultar un valor minimo ingrese el comando seguido del atributo: "
          "MINIMO atributo \n")
    print("* Para sumar los valores de un atributo ingrese el comando seguido del atributo: "
          "SUMAR atributo \n")
    print("* Para contar los datos cargados ingrese el comando seguido del atributo: "
          "CUENTA \n")
    print("* Para crear un reporte ingrese el comando seguido del atributo: REPORTAR  N \n")


def separarArchivos(texto):
    instruccion = re.split("\s", texto)
    if instruccion[0].lower() == "cargar":
        archivos = re.split(",", instruccion[1])
        for archivo in archivos:
            leerJSON.CargarDatos(archivo)
    else:
        print("El comando ingresado no se ha reconocido")


def separarSelecciones(texto):
    instruccion = re.split("\s", texto)
    if len(instruccion) < 2:
        if instruccion[0].lower() == "seleccionar":
            realizarSelecionSincondicion()
    elif len(instruccion) > 1:
        if instruccion[0].lower() == "seleccionar" and instruccion[2].lower() == "donde":
            print("nel")

    else:
        print("El comando ingresado no se ha reconocido")


def obtenerCondicion(condicion):
    instruccion = re.split("=", condicion)
    if instruccion[0] == "nombre":
        return "nombre"
    elif instruccion[0] == "edad":
        return "edad"
    elif instruccion[0] == "activo":
        return "activo"
    elif instruccion[0] == "promedio":
        return "promedio"
    else:
        print("No se ha podido verificar")


def realizarSelecionSincondicion(atributos):
    selecciones = re.split(",", atributos)
    for seleccion in selecciones:
        if seleccion.lower() == "nombre":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        if seleccion.lower() == "edad":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        if seleccion.lower() == "activo":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        if seleccion.lower() == "promedio":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)
