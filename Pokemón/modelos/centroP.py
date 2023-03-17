# Acá va a estar la informacion relativa al centro pokemón
from modelos.ataques import Ataque

menu_centro = '''Bienvenido(a) al centro pokemón!
Tienes 3 opciones de acción
1) Restaurar los HP de tus pokemones
2) Restaurar los PP de todos los ataques de tus pokemones
3) Salir '''


# Restaurar los HP:
def restaurar_hp(entrenador):
    for l in range(0, len(entrenador.equipo)):
        entrenador.equipo[l].hp = 100
        print('''
        {} ha recuperado su HP!'''.format(entrenador.equipo[l]))
        return None


# Recuperar pp
# Falla en la función

def pp_nucleo(ataque: Ataque):
    return ataque.pp_base


def restaurar_pp(entrenador):
    for m in range(0, len(entrenador.equipo)):
        contador = 0
        while contador <= 3:
            entrenador.equipo[m].ataques[contador].pp_actuales = pp_nucleo(entrenador.equipo[m].ataques[contador])
            print('''Felicidades! {} ha recuperado sus pp y ahora tiene {}'''
                  .format(entrenador.equipo[m].ataques[contador].nombre,
                          entrenador.equipo[m].ataques[contador].pp_actuales))
            contador += 1
    return None
