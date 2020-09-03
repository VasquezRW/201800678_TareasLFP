import re
import webbrowser

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


def identificarComando(comando):
    x = re.split("\s", comando)
    if x[0].lower() == "cargar":
        separarArchivos(comando)
    elif x[0].lower() == "seleccionar":
        separarSelecciones(comando)
    elif x[0].lower() == "maximo":
        maximo(comando)
    elif x[0].lower() == "minimo":
        minimo(comando)
    elif x[0].lower() == "cuenta":
        print(len(leerJSON.datosPersonas))
    elif x[0].lower() == "reportar":
        reportar(int(x[1]))


# Metodo que separa y carga cada archivo
def separarArchivos(texto):
    instruccion = re.split("\s", texto)
    if instruccion[0].lower() == "cargar":
        archivos = re.split(",", instruccion[1])
        for archivo in archivos:
            leerJSON.CargarDatos(archivo)
    else:
        print("El comando ingresado no se ha reconocido")


def imprimir():
    for persona in leerJSON.datosPersonas:
        print("Persona ")
        print("Nombre  : ", persona.getNombre())
        print("Edad    : ", persona.getEdad())
        print("Activo  : ", persona.getActivo())
        print("Promedio: ", persona.getPromedio())
        print("\n")


# Metodo que separa y realiza cada seleccion
def separarSelecciones(texto):
    instruccion = re.split("\s", texto)
    if len(instruccion) == 2:
        if instruccion[0].lower() == "seleccionar":
            realizarSelecionSincondicion(instruccion[1])
    elif len(instruccion) == 4:
        if instruccion[0].lower() == "seleccionar" and instruccion[2].lower() == "donde":
            realizarSelecionConcondicion(instruccion[1], instruccion[3])
    else:
        print("El comando ingresado no se ha reconocido")


# Metodo que separa la condicion del DONDE
def separarCondicion(condicion):
    instruccion = re.split("=", condicion)
    return instruccion


# Metodo que imprime cada seleccion
def realizarSelecionSincondicion(atributos):
    selecciones = re.split(",", atributos)
    for seleccion in selecciones:
        if seleccion.lower() == "nombre":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        if seleccion.lower() == "edad":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.edad)

        if seleccion.lower() == "activo":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.activo)

        if seleccion.lower() == "promedio":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.promedio)


# Metodo que imprime cada seleccion con condicion
def realizarSelecionConcondicion(atributos, condicion):
    selecciones = re.split(",", atributos)
    comparar = separarCondicion(condicion)
    for seleccion in selecciones:
        # imprimir nombre
        if seleccion.lower() == "nombre" and comparar[0] == "nombre":
            for persona in leerJSON.datosPersonas:
                nom = condicion.replace("\"", "")
                if persona.nombre == nom:
                    print(seleccion.lower(), ": ", persona.nombre)
        elif seleccion.lower() == "nombre":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        # imprimir edad
        if seleccion.lower() == "edad" and comparar[0] == "edad":
            for persona in leerJSON.datosPersonas:
                if persona.edad == condicion[1]:
                    print(seleccion.lower(), ": ", persona.edad)
        elif seleccion.lower() == "edad":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.edad)

        # imprimir activo
        if seleccion.lower() == "activo" and comparar[0] == "activo":
            for persona in leerJSON.datosPersonas:
                if persona.activo == condicion[1]:
                    print(seleccion.lower(), ": ", persona.activo)
        elif seleccion.lower() == "activo":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.nombre)

        # imprimir promedio
        if seleccion.lower() == "promedio" and comparar[0] == "promedio":
            for persona in leerJSON.datosPersonas:
                if persona.promedio == condicion[1]:
                    print(seleccion.lower(), ": ", persona.promedio)
        elif seleccion.lower() == "promedio":
            for persona in leerJSON.datosPersonas:
                print(seleccion.lower(), ": ", persona.promedio)

        else:
            print("Error")


# Metodo que devuelve el maximo de edad o promedio
def maximo(comando):
    instruccion = re.split("\s", comando)
    if instruccion[0].lower() == "maximo" and instruccion[1].lower() == "edad":
        lista = sorted(leerJSON.datosPersonas, key=lambda persona: float(persona.edad))
        print(lista[len(lista) - 1])

    elif instruccion[0].lower() == "maximo" and instruccion[1].lower() == "promedio":
        lista = sorted(leerJSON.datosPersonas, key=lambda persona: float(persona.promedio))
        print(lista[len(lista) - 1])


# Metodo que devuelve el minimo de edad o promedio
def minimo(comando):
    instruccion = re.split("\s", comando)
    if instruccion[0].lower() == "maximo" and instruccion[1].lower() == "edad":
        lista = sorted(leerJSON.datosPersonas, key=lambda persona: float(persona.edad))
        print("La persona con edad minima es: ", lista[0])

    elif instruccion[0].lower() == "maximo" and instruccion[1].lower() == "promedio":
        lista = sorted(leerJSON.datosPersonas, key=lambda persona: float(persona.promedio))
        print("La persona con promedio minima es: ", lista[0])


# Metodo que suma edad o promedio
def suma(comando):
    instruccion = re.split("\s", comando)
    if instruccion[0].lower() == "suma" and instruccion[1].lower() == "edad":
        sum = 0
        for persona in leerJSON.datosPersonas:
            sum += persona.edad
        print("La suma de las edades es: ", sum)

    elif instruccion[0].lower() == "suma" and instruccion[1].lower() == "edad":
        sum = 0
        for persona in leerJSON.datosPersonas:
            sum += persona.promedio
        print("La suma de las edades es: ", sum)


# Metodo que suma edad o promedio
def reportar(rango):
    f = open('reporte.html', 'w')
    inicio = ("<html>\n"
              "    <head><h1>Reporte</h1></head>\n"
              "    <body>\n<table border=\"1\">\n"
              "    <tr>\n"
              "    <th>Nombre</th>\n"
              "    <th>Edad</th>\n"
              "    <th>Activo</th>\n"
              "    <th>Promedio</th>\n"
              "    </tr>\n"
              )
    f.write(inicio)
    i = 1
    for persona in leerJSON.datosPersonas:
        if i < rango:
            datos = (f"""<tr>
                <td> {persona.nombre} </td>\n
                <td> {persona.edad} </td>\n
                <td> {persona.activo} </td>\n
                <td> {persona.promedio} </td>\n</tr>""")
            f.write(datos)
            i += i
        elif i == rango:
            break

    fin = ("""</table>\n</body>\n
</html>""")
    f.write(fin)
    f.close()
    webbrowser.open_new_tab('reporte.html')
