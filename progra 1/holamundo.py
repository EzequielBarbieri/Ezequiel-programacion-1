"""contraseña_ingresada = "1234"
contraseña_almacenada = "1234"
acceso_permitido = False

if contraseña_almacenada == contraseña_ingresada:
    acceso_permitido = True
    print("Acceso permitido")

print("gracias por usar el sistema seguro del banco")"""

contraseña_solicitada = " "
contraseña_correcta = "1234"

while contraseña_solicitada != contraseña_correcta:
    contraseña_solicitada = input("ingrese su contraseña: ")

    if contraseña_solicitada != contraseña_correcta:
        print("contraseña incorrecta, intente nuevamente: ")
    else:
        print("contraseña valida. ¡bienvenido!")
    break

