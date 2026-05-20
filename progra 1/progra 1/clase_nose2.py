lineas = [
    " AnA ;8;7;9",
    " JuAn ;4;5;3",
    " LucIA ;10;9;10"
]
nueva_lista = []
for linea in lineas:
    datos = linea.split(";")
    nombre = [i.replace(";", "") for i in datos]
    notas = [x for x in nombre if x.isdigit()]
    nombre = nombre[0].strip()
    nombre = nombre.capitalize()
    nueva_lista = "-".join(notas)
    print(f"Alumno {nombre} - Notas: {nueva_lista}")