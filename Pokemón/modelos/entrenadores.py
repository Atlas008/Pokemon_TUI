from modelos.pokemon import Pokemon
from modelos.tienda import Consumible as Consumible
from modelos.ataques import Ataque

from typing import Union

class Entrenador:
    def __init__(self, nombre: str, equipo: list, objetos: list, direccion: int, dinero: int):
        self.dinero = dinero
        self.objetos = objetos
        self.nombre = nombre
        self.equipo = equipo
        self.direccion = direccion

    def __repr__(self):
        return "{}".format(self.nombre)

    def usar(self, gana: Union[Pokemon, Ataque], usa: Consumible):
        if type(gana) == Pokemon:
            gana.hp += usa.r_hp
            return '''Tu pokemón {} ha recuperado {} hp!
Ahora {} tiene {} de hp'''.format(gana.nombre, usa.r_hp, gana.nombre, gana.hp)

        elif type(gana) == Ataque:
            gana.pp_actuales += usa.r_pp
            return '''El ataque {} ha ganado {} pp!
Ahora {} tiene {} pp'''.format(gana.nombre, usa.r_pp, gana.nombre, gana.pp_actuales)

    def comprar(self, item: Consumible, precio: int):
        if precio > self.dinero:
            print("El ítem {} cuesta {}, y tu tienes {}, 1 estás pobre, 2 no puedes comprarlo...".format(item.nombre, precio,
                                                                                                         self.dinero))
            return None
        elif precio <= self.dinero:
            self.dinero -= precio
            print("Felicidades has comprado {}!; te quedan {} CLP".format(item.nombre, self.dinero))
            return self.objetos.append(item)

    def obtener_objetos(self):
        return self.objetos

# @property
#    def vida_actual(self):
#        return self._hp
#    @vida_actual.setter
#    def vida_actual(self, vida_maxima=100):
#        if self._hp > vida_maxima:
#            self._hp = vida_maxima
#        elif self._hp < 0:
#            self._hp = 0
#        else:
#            self._hp = self._hp
