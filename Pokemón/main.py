from random import randint as dado
import textos.dialogos as relleno
from modelos.entrenadores import Entrenador
from modelos.pokemon import pikachu, charmander, bulbasaur, squirtle, rattata, snorlax, gloom, rayquaza
from modelos.tienda import leche_mumu, eter, menu_tienda
from modelos.centroP import menu_centro, restaurar_pp, restaurar_hp
from time import sleep
from colorama import Fore as colores_consola, init as color

color()

print(relleno.cargando)
sleep(1)
print(relleno.cargando)
sleep(1)
print(relleno.cargando)
sleep(1)
print(relleno.sello_autor)
print(relleno.saludo_inicial)
nombre = input("Apodo: ")
entrenador = Entrenador(nombre, [], [], 0, 0)
print("Bienvenid@ entrendor(a): {}".format(entrenador.nombre))
print(relleno.eleccion, colores_consola.RED + relleno.eleccion_1 + ',',
      colores_consola.BLUE + relleno.eleccion_2 + ',', colores_consola.GREEN + relleno.eleccion_3)
print(colores_consola.RESET)
inicial = input("Selecciona tu pokemón: ")
inicial_op = ['0', '1', '2', '3']
while inicial not in inicial_op:
    print("Opción inválida...")
    inicial = input("Selecciona tu pokemón: ")

lista_iniciales = [pikachu, charmander, squirtle, bulbasaur]
entrenador.equipo.append(lista_iniciales[int(inicial)])
print(relleno.nuevo_equipo.format(entrenador.nombre, entrenador.equipo))

print(relleno.combate_inicial)
print(relleno.hint)
print(relleno.espacios)
# Combate 1 | Lógica de peleas base

print("Tu oponente es un {} con {} de Hp".format(rattata.nombre, rattata.hp))
print(relleno.espacios)
print(entrenador.equipo[0].ataques)
# Rattata

while entrenador.equipo[0].hp > 0 and rattata.hp > 0:
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

        print(entrenador.equipo[0].atacar(rattata, ataque_elegido))
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
    if rattata.hp > 0:
        print(rattata.atacar(entrenador.equipo[0], dado(0, 3)))

if entrenador.equipo[0].hp == 0:
    print(relleno.perdio_combate)
    input("Typea cualquier cosa para terminar el programa c:")
    quit()


else:
    print(relleno.gano_combate_0.format(entrenador.nombre))
    entrenador.dinero += 500
    objetos_iniciales = [leche_mumu, leche_mumu, eter, eter]
    for consumible in objetos_iniciales:
        entrenador.objetos.append(consumible)
    print("Ahora este es su inventario: {}".format(entrenador.objetos))
    print("Tu billetera ahora tiene {} CLP".format(entrenador.dinero))

print(relleno.lugar_1)
print(entrenador.equipo[0].ataques)
while entrenador.equipo[0].hp > 0 and snorlax.hp > 0:
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

        print(entrenador.equipo[0].atacar(snorlax, ataque_elegido))
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
            objeto_usado = entrenador.obtener_objetos()[objeto_seleccionado]
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
    if snorlax.hp > 0:
        print(snorlax.atacar(entrenador.equipo[0], dado(0, 3)))

if entrenador.equipo[0].hp == 0:
    print(relleno.perdio_combate)
    input("Typea cualquier cosa para terminar el programa c:")
    quit()
else:
    entrenador.dinero += 500
    print(relleno.gano_l1.format(entrenador.dinero))

print(relleno.ruido_arbusto)
op_arbusto = ['si', 'no']
eleccion_arbusto = input("Typea Si o No: ").lower()
while eleccion_arbusto not in op_arbusto:
    print("Opción inválida...")
    eleccion_arbusto = input("Typea Si o No: ").lower()

if eleccion_arbusto == 'no':
    print("Nah, demás que era algún ingeniero sufriendo por dinámica")
elif eleccion_arbusto == 'si':
    print(relleno.lugar_2)
    print(relleno.hint)
    print(entrenador.equipo[0].ataques)

    while entrenador.equipo[0].hp > 0 and gloom.hp > 0:
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

            print(entrenador.equipo[0].atacar(gloom, ataque_elegido))
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
        if gloom.hp > 0:
            print(gloom.atacar(entrenador.equipo[0], dado(0, 3)))

    if entrenador.equipo[0].hp == 0:
        print(relleno.perdio_combate)
        input("Typea cualquier cosa para terminar el programa c:")
        quit()

    else:
        print(relleno.gano_combate.format(entrenador.nombre, gloom.nombre))
        entrenador.dinero += 500

print(relleno.cruce_2)
# conjunto_plaza_rea = ['Centro Pokemón', 'Pokemart', 'Fuente Rea'] preguntar como implemetar diccionarios
plaza = [0, 1, 2, 3]
eleccion_plaza = int(input("Typea tu elecciíon: "))
while eleccion_plaza not in plaza:
    print("Opción inválida...")
    eleccion_plaza = int(input("Typea tu elecciíon: "))

entrenador.direccion = eleccion_plaza

while entrenador.direccion in plaza:
    if entrenador.direccion == 0:
        print(relleno.cruce_2)
        eleccion_plaza = int(input("Typea tu elecciíon: "))
        while eleccion_plaza not in plaza:
            print("Opción inválida...")
            eleccion_plaza = int(input("Typea tu elecciíon: "))
        entrenador.direccion = int(eleccion_plaza)

    elif entrenador.direccion == 1:
        print(menu_tienda)
        eleccion_tienda = int(input("Typea tu elección: "))
        eleccion_tienda_op = [1, 2, 3]
        while eleccion_tienda not in eleccion_tienda_op:
            print("Opción inválida...")
            eleccion_tienda = int(input("Typea tu elección: "))

        if eleccion_tienda == 1:
            entrenador.comprar(leche_mumu, 500)
            print(relleno.espacios)
        elif eleccion_tienda == 2:
            entrenador.comprar(eter, 500)
            print(relleno.espacios)
        elif eleccion_tienda == 3:
            print("Decides salir del Pokemart ->")
            print(relleno.espacios)
            entrenador.direccion = 0

    elif entrenador.direccion == 2:
        print(menu_centro)
        eleccion_centro = int(input("Typea tu elección: "))
        eleccion_centro_op = [0, 1, 2, 3]
        while eleccion_centro not in eleccion_centro_op:
            print("Opción inválida...")
            eleccion_tienda = int(input("Typea tu elección: "))

        if eleccion_centro == 1:
            restaurar_hp(entrenador)
            print(relleno.espacios)
        elif eleccion_centro == 2:
            restaurar_pp(entrenador)
            print(relleno.espacios)
        elif eleccion_centro == 3:
            print("Decides salir del Centro Pokemón ->")
            print(relleno.espacios)
            entrenador.direccion = 0

    elif entrenador.direccion == 3:
        print("Decides seguir con tu camino ->")
        print(relleno.espacios)
        entrenador.direccion = 4

print(relleno.seguir_recto)
print(relleno.hint)
print(entrenador.equipo[0].ataques)

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

if entrenador.equipo[0].hp == 0:
    print(relleno.perdio_combate)
    input("Typea cualquier cosa para terminar el programa c:")
    quit()
else:
    print(relleno.creditos)
