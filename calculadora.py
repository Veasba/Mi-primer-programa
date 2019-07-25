operacion = input("Que operacion quieres realizar? (Suma / Resta / Multiplicar / Dividir): ")

primer_numero = int (input("Primer numero: "))

segundo_numero = int (input("Segundo numero: "))

resultado_operacion = 0

if operacion == "Suma":
    resultado_operacion = primer_numero + segundo_numero
    print("El resultado es {}".format(resultado_operacion))

elif operacion == "Resta":
    resultado_operacion = primer_numero - segundo_numero
    print("El resultado es {}".format(resultado_operacion))

elif operacion == "Multiplicar":
    resultado_operacion = primer_numero * segundo_numero
    print("El resultado es {}".format(resultado_operacion))

elif operacion == "Dividir":
    resultado_operacion = primer_numero / segundo_numero
    print("El resultado es {}".format(resultado_operacion))







