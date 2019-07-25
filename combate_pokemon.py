pokemon_elegido = input("Contra que pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur): ")

vida_picachu = 100
vida_enemigo = 0
ataque_pokemon = 0
if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
        vida_enemigo = 80
        nombre_pokemon = "Charmander"
        ataque_pokemon = 7

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 10

while vida_picachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque quieres elejir? (Chispazo / Bola Voltio): ")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido== "Bola Voltio":
        vida_enemigo -= 12

    print("La vida de {} es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_picachu -= ataque_pokemon

    print("La vida de tu pokemon es de {}".format(vida_picachu))

if vida_enemigo <= 0:
    print("Haz Ganado!")
elif vida_picachu <= 0:
    print("Haz Perdido!")

print("El combate a finalizado")