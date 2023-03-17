# Aquí voy a darle definiciones básicas al proyecto#

from modelos import ataques
class Pokemon:
    def __init__(self, nombre: str, hp: float, lista_ataques: list, tipo: str):
        self.nombre = nombre
        self.hp = hp
        self.ataques = lista_ataques
        self.tipo = tipo

    def __repr__(self):
        return "{}".format(self.nombre)

    def atacar(self, enemigo, valor: int):

        if self.ataques[valor - 1].pp_actuales > 0:
            a = enemigo.hp - self.ataques[valor - 1].dano
            print(self.nombre, "ha usado", self.ataques[valor - 1].nombre, "!!!")
            enemigo.hp = a
            b = self.ataques[valor - 1].pp_actuales - 1
            self.ataques[valor - 1].pp_actuales = b
            return '''{} HP: {}
{}: {} pp'''.format(enemigo.nombre, enemigo.hp, self.ataques[valor-1].nombre, self.ataques[valor-1].pp_actuales)

        elif self.ataques[valor - 1].pp_actuales <= 0:
            print("A este movimiento no le quedan pp :o")
            return "{} pp = 0".format(self.ataques[valor - 1].nombre)


# Falta el dado

# Definicion de pokémones

pikachu = Pokemon("Pikachu", 100, ataques.a_pikachu, "Tipo: Electrico")
bulbasaur = Pokemon("Bulbasaur", 100, ataques.a_bulbasaur, "Tipo: Planta / Veneno")
squirtle = Pokemon("Squirtle", 100, ataques.a_squirtle, "Tipo: Agua")
charmander = Pokemon("Charmander", 100, ataques.a_charmander, "Tipo: Fuego")
# Salvajes
rattata = Pokemon("Rattata", 50, ataques.a_rattata, "Tipo: Normal")
gloom = Pokemon("Gloom", 60, ataques.a_gloom, "Tipo: Planta / Veneno")
snorlax = Pokemon("Snorlax", 60, ataques.a_snorlax, "Tipo Normal")
rayquaza = Pokemon("Rayquaza", 80, ataques.a_rayquaza, "Tipo Dragón / Volador")

# Gym 1
vileplume = Pokemon("Vileplume", 80, ataques.a_vileplume, "Tipo: Planta / Veneno")
victreebel = Pokemon("Victreebel", 80, ataques.a_victreebel, "Tipo: Planta / Veneno")

# Gym 2
tentacruel = Pokemon("Tentacruel", 80, ataques.a_tentacruel, "Tipo: Agua / Veneno")
gyarados = Pokemon("Gyarados", 80, ataques.a_gyarados, "Tipo: Agua / Volador")

# Gym 3
golem = Pokemon("Golem", 70, ataques.a_golem, "Tipo: Roca / Tierra")
onix = Pokemon("Onix", 70, ataques.a_onix, "Tipo: Roca / Tierra")
rhydon = Pokemon("Rhydon", 70, ataques.a_rhydon, "Tipo: Tierra / Roca")

# Liga Ἄτλας

# 1°: RipperZero
# Bulbasaur
"mew"
"Entei"

# 2°: Lily416
"Eevee"
"Chikorita"
"Pachirisu"

# 3°: Sufiquema
"Cyndaquil"
"Vaporean"
"Dragonite"

# 4°: Monte
"Aggron"
"Araquanid"
"Spiritoms"

# 5°: Blueben
"Arceus"
"Bidoof" #Cambiar ataques con nombre ej: placaje_bidoof para mejorar el daño
"Jigglypuff" #Agregar ataque que en 1/30 mata xd (Ding); a revisar funcionalidad

# 6°: Allmoz
'Larvitar "evolucion->Tyranitar"'
"Sneasel"
"Forretress"
