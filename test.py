
def input_de_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {} , estas seguro? [si/no]:".format(dato_usuario))

        if seguro == "si":
            confirmacion = True
    return dato_usuario

nombre = input_de_confirmacion("Como te llamas: ")
print("Haz confirmado que te llamas {}, muchas gracias".format(nombre))

nombre = input_de_confirmacion("Que numero quieres elegir?:  ")
print("Haz confirmado que tu numero es {}, muchas gracias".format(nombre))

print("Excelente!")

