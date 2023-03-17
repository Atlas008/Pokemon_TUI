from random import randint as dado
import textos.dialogos as relleno
from modelos.entrenadores import Entrenador
from modelos.pokemon import pikachu, charmander, bulbasaur, squirtle, rattata, snorlax, gloom, rayquaza
from modelos.tienda import leche_mumu, eter, menu_tienda
from modelos.centroP import menu_centro, restaurar_pp, restaurar_hp

# [leche_mumu, eter]
entrenador = Entrenador("Jp", [charmander], [leche_mumu, eter, leche_mumu, eter, leche_mumu, eter], 0, 0)

while entrenador.equipo[0].hp > 0 and rayquaza.hp > 0:
    print('Elige si vas a atacar ("a"), o si vas a utilizar algún objeto ("o"):')
    modalidad = input("Typea A para ataque u O para objetos: ").lower()
    modalidad_op = ['a', 'o']
    while modalidad not in modalidad_op:
        print("Opción inválida...")
        modalidad = input("Typea A para ataque u O para objetos: ").lower()

    if modalidad == 'a':
        ataque_elegido = input("Typea el ataque que quieras realizar: ")
        ataque_elegido_op = ['1', '2', '3', '4']
        while ataque_elegido not in ataque_elegido_op:
            print("Opción inválida...")
            ataque_elegido = input("Typea el ataque que quieras realizar: ")
        ataque_elegido = int(ataque_elegido)

        print(entrenador.equipo[0].atacar(rayquaza, ataque_elegido))
        print(relleno.espacios)

    elif modalidad == 'o':
        if len(entrenador.objetos) == 0:
            print("Tu mochila está vacía....")
        else:
            print('''Las posiciones de objetos se entienden de la siguiente manera:
ej: [leche mumu, eter], pos 1: leche mumu, pos 2: eter'.''')
            print(entrenador.objetos)
            objeto_seleccionado = input('''Selecciona la posición del objeto que quieres utilizar.
Typea tu elección: ''')
            objeto_seleccionado_op = [str(l) for l in range(0, len(entrenador.objetos) + 1)]
            while objeto_seleccionado not in objeto_seleccionado_op:
                print("Opción inválida...")
                objeto_seleccionado = input('''Selecciona la posición del objeto que quieres utilizar.
Typea tu elección: ''')
            objeto_seleccionado = int(objeto_seleccionado) - 1

            objeto_usado = entrenador.objetos[objeto_seleccionado]
            if objeto_usado == leche_mumu:
                print(entrenador.usar(entrenador.equipo[0], leche_mumu))
                print(relleno.espacios)
                objeto_desechado = entrenador.objetos.pop(objeto_seleccionado)
            elif objeto_usado == eter:
                print(entrenador.equipo[0].ataques)
                ataque_objetivo = int(input('''Selecciona el ataque de la misma manera que el objeto
Typea tu elección: ''')) - 1
                print(entrenador.usar(entrenador.equipo[0].ataques[ataque_objetivo], eter))
                print(relleno.espacios)
                objeto_desechado = entrenador.objetos.pop(objeto_seleccionado)
        if rayquaza.hp > 0:
            print(rayquaza.atacar(entrenador.equipo[0], dado(0, 3)))

