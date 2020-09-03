import json

def CargarDatos(ruta):
    with open(ruta) as contenido:
        Datos = json.load(contenido)
        for atributo in Datos:
            print(atributo.get('DPI'))
            print(atributo.get('Carne'))
            print(atributo.get('Nombre'))
            print(atributo.get('Apellido'))
            print('')
