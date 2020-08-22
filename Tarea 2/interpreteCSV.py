import csv

def LeerDatos(ruta):
    with open(ruta) as contenido:
        reader = csv.reader(contenido)
        for row in reader:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print('')