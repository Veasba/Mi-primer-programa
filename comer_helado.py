quieres_helado_input = input("Quieres un helado? (si/no): ").upper()

if quieres_helado_input == "SI":
    quieres_helado = True
elif quieres_helado_input == "NO":
    quieres_helado = False
else:
    print("Te he dicho que me digas si o no, no se que me has dicho entonces contare que es un no")
    quieres_helado = False

tienes_dinero_input = input("Tienes dinero para un helado? (si/no): ").upper()
esta_abierto_input = input("Esta el super abierto? (si/no): ").upper()
esta_tu_mama_input = input("Estas con tu madre? (si/no): ").upper()


tienes_dinero = tienes_dinero_input == "SI"
esta_tu_mama = esta_tu_mama_input == "SI"
puede_comprarlo = tienes_dinero or esta_tu_mama
esta_abierto = esta_abierto_input == "SI"


if quieres_helado and puede_comprarlo and esta_abierto:
    print("Pues comete un helado")
else:
    print("Pues no comas nada")


