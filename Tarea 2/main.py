# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import interpreteJSON
import interpreteCSV
import interpreteXML

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\nDatos desde JSON\n")
    interpreteJSON.CargarDatos('datos.json')
    print("\nDatos desde CSV\n")
    interpreteCSV.LeerDatos('datos.csv')
    print("\nDatos desde XML\n")
    interpreteXML.Cargar('datos.xml')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
