import webbrowser


def escribirHTML(lista, rango):
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
    for x in range(rango):
        datos = (f"""<tr>
<td> {x.n} </td>\n
<td> {x.e} </td>\n
<td> {x.a} </td>\n
<td> {x.s} </td>\n</tr>""")
        f.write(datos)
    fin = ("""</table>\n</body>\n
        </html>""")
    f.write(fin)
    f.close()
    webbrowser.open_new_tab('reporte.html')
