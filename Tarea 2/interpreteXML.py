import xml.etree.cElementTree as XML

def Cargar(Ruta):
    Archivo = XML.parse(Ruta)
    Registro = Archivo.getroot()

    for x in Registro.findall('Estudiante'):
        print("DPI: ",x.find('DPI').text)
        print("Carne: ",x.find('Carne').text)
        print("Nombre: ",x.find('Nombre').text)
        print("Apellido: ",x.find('Apellido').text)
        print('')