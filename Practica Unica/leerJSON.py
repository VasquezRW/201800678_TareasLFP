import json
import Datos


datosPersonas = []


def CargarDatos(ruta):

    with open(ruta) as contenido:
        datos = json.load(contenido)
        for atributo in datos:
            persona = Datos.Persona()
            persona.setNombre(atributo.get('nombre'))
            persona.setEdad(atributo.get('edad'))
            persona.setActivo(atributo.get('activo'))
            persona.setPromedio(atributo.get('promedio'))
            datosPersonas.append(persona)