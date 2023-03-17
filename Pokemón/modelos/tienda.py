# Aqui se van a definir lo necesario para la tienda pokémon.
# Falta buscar los nombres de los objetos en la wikidex pero por ahora es la base.

from typing import NamedTuple


class Consumible:
    def __init__(self, r_hp: int, r_pp: int, nombre: str):
        self.r_pp = r_pp
        self.r_hp = r_hp
        self.nombre = nombre

    def __repr__(self):
        return '{}'.format(self.nombre)


# Items de vida
leche_mumu = Consumible(15, 0, "Leche Mumú")
bayas_vida = Consumible(10, 0, "Bayas Vida")

# Items de pp
eter = Consumible(0, 7, "Eter")
bayas_pp = Consumible(0, 5, "Bayas PP")

# Item S-tier
restaurar_todo = Consumible(20, 100, "Restaurar Todo")

menu_tienda = '''Bienvenido a la tienda pokemon!
En este local vendemos principalmente 2 objetos
1) Leche mumú: 500 CLP 
2) Éter: 500 CLP
3) Salir '''


