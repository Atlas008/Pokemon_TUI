# Aquí se definirán todos los ataque ha usar con sus pp respectivos
# Clase 1: 10% fallo (10 daño)
# Clase 2: 20% fallo (15 daño, porcentual y healing)
# Clase 3: 30% fallo (20 daño)
# Clase 4: 100% accurate

# Los pp base son para recuperarlos con los refil, pero los actuales son los "reales"
class Ataque:
    def __init__(self,  posicion, nombre, dano, pp_acutales, clase: int, pp_base):
        self.posicion = posicion
        self.pp_base = pp_base
        self.nombre = nombre
        self.dano = dano
        self.pp_actuales = pp_acutales
        self.clase = clase

    def __repr__(self):
        return '''{}: {} ({} daño,{} pp)'''.format(self.posicion, self.nombre, self.dano, self.pp_actuales)


# Ataques Bulbasaur
placaje = Ataque(1, "Placaje", 10, 25, 1, 25)
latigo_cepa = Ataque(2, "Látigo cepa", 15, 20, 2, 20)
polvo_veneno = Ataque(3, "Polvo veneno", 15, 15, 2, 15)
doble_filo = Ataque(4, "Doble filo", 20, 15, 3, 15)

# Ataques Charmander
aranazo = Ataque(1, "Arañazo", 10, 25, 1, 25)
ascuas = Ataque(2, "Ascuas", 15, 20, 2, 20)
furia_dragon = Ataque(3, "Furia Dragón", 20, 15, 3, 15)
colmillo_igneo = Ataque(4, "Colmillo Ígneo", 15, 15, 2, 15)

# Ataques Squirtle
# Placaje
burbuja = Ataque(2, "Burbuja", 15, 15, 2, 15)
pistola_agua = Ataque(3, "Pistola de agua", 15, 20, 2, 20)
hidropulso = Ataque(4, "Hidropulso", 20, 15, 3, 15)

# Ataques Rattata
golpes_furia = Ataque(1, "Golpes Furia", 15, 20, 2, 20)
alboroto = Ataque(2, "Alboroto", 10, 25, 1, 25)
mordisco = Ataque(3, "Mordisco", 15, 20, 2, 20)
chirrido = Ataque(4, "Chirrido", 10, 20, 1, 20)

# Ataques Gloom
acido = Ataque(1, "Ácido", 15, 20, 2, 20)
toxico = Ataque(2, "Tóxico", 10, 20, 1, 20)
# polvo veneno
fuerza_lunar = Ataque(4, "Fuerza Lunar", 15, 20, 2, 20)

# Ataques Pikachu
imapctrueno = Ataque(1, "Impactrueno", 25, 15, 3, 15)
ataque_rapido = Ataque(2, "Ataque Rápido", 15, 20, 2, 20)
cola_ferrea = Ataque(3, "Cola Ferrea", 15, 20, 2, 20)
onda_trueno = Ataque(4, "Onda Trueno", 20, 15, 3, 15)

# Ataques Vileplume
tormenta_floral = Ataque(1, "Tormenta Floral", 15, 20, 2, 20)
campo_hierba = Ataque(2, "Campo Hierba", 15, 20, 2, 20)
#polvo veneno
#fuerza lunar

# Ataques Victreebel
ciclon_hojas = Ataque(1, "Ciclón de Hojas", 15, 20, 2, 20)
# latigo cepa
hoja_afilada = Ataque(3, "Hoja Afilada", 15, 20, 2, 20)
puya_nociva = Ataque(4, "Puya Nociva", 15, 20, 2, 20)

# Ataques Tentacruel
pictazo_veneno = Ataque(1, "Picotazo Veneno", 17, 20, 2, 20)
# Burbuja
armadura_acida = Ataque(3, "Armadura Ácida", 17, 20, 2, 20)
# hidropulso

# Ataques Gyarados
triturar = Ataque(1, "Triturar", 17, 20, 2, 20)
salpicadura = Ataque(2, "Salpicadura", 17, 20, 2, 20)
# Mordisco
acua_cola = Ataque(4, "Acua Cola", 17, 20, 2, 20)

# Gym 3
# Ataques Golem roca/tierra
# Placaje
rodar = Ataque(2, "Rodar", 19, 20, 2, 20)
bofeton_lodo = Ataque(3, "Bofetón Lodo", 19, 20, 2, 20)
avalancha = Ataque(4, "Avalancha", 19, 20, 2, 20)

# Ataques Onix roca/tierra
terratemblor = Ataque(1, "Terratemblor", 19, 20, 2, 20)
# Rodar
trampa_rocas = Ataque(3, "Trampa Rocas", 19, 20, 2, 20)
# Avalancha

# Ataques Rhydon
puno_dinamico = Ataque(1, "Puño Dinámico", 19, 20, 2, 20)
gigaimpacto = Ataque(2, "Gigaimpacto", 19, 20, 2, 20)
# Trampa Roca
# Avalancha"

# Ataques Snorlax
#terratemblor
# triturar
# mordisco
# doble filo

# Ataques Rayquaza
ciclon = Ataque(1, "Ciclón", 20, 20, 2, 20)
garra_dragon = Ataque(2, "Garra Dragón", 21, 20, 2, 20)
pulso_dragon = Ataque(3, "Pulso Dragón", 23, 20, 2, 20)
vuelo = Ataque(4, "Vuelo", 20, 20, 3, 20)

# Listas de ataques
a_pikachu = [imapctrueno, ataque_rapido, cola_ferrea, onda_trueno]
a_bulbasaur = [placaje, latigo_cepa, polvo_veneno, doble_filo]
a_charmander = [aranazo, ascuas, furia_dragon, colmillo_igneo]
a_squirtle = [placaje, burbuja, pistola_agua, hidropulso]
a_rattata = [golpes_furia, alboroto, mordisco, chirrido]
a_gloom = [acido, toxico, polvo_veneno, fuerza_lunar]
a_vileplume = [tormenta_floral, campo_hierba, polvo_veneno, fuerza_lunar]
a_victreebel = [ciclon_hojas, latigo_cepa, hoja_afilada, puya_nociva]
a_tentacruel = [pictazo_veneno, burbuja, armadura_acida, hidropulso]
a_gyarados = [triturar, salpicadura, mordisco, acua_cola]
a_golem = [placaje, rodar, bofeton_lodo, avalancha]
a_onix = [terratemblor, rodar, trampa_rocas, avalancha]
a_rhydon = [puno_dinamico, gigaimpacto, trampa_rocas, avalancha]
a_snorlax = [terratemblor, alboroto, mordisco, doble_filo]
a_rayquaza = [ciclon, garra_dragon, pulso_dragon, vuelo]