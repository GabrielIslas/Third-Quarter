from math import pi
# 
pollo = lambda nombre, dias, peso, habilidades: (nombre, dias, peso, habilidades)

edad = lambda pollo: pollo[1] / (pi * 365 ** 2)

esAdulto = lambda pollo: edad(pollo) > 5

esJoven = lambda pollo: not esAdulto(pollo)

estaDesnutrido = lambda pollo: (esJoven(pollo) and pollo[2] < 50) or (esAdulto(pollo) and pollo[2] < 200) or (len(pollo[0]) % 2 == 0)

engordar = lambda alpiste, pollo: (pollo[0], pollo[1], pollo[2] + alpiste, pollo[3])

arguiniano = lambda pollo: engordar(100, pollo)

miyagi = lambda pollo: (pollo[0], pollo[1], pollo[2], pollo[3] + ["karate"]) if "karate" not in pollo[3] else pollo

marcelito = lambda pollo: (pollo[0], pollo[1], pollo[2], [])

marceñano = lambda pollo: arguiniano(marcelito(pollo))

planeta = lambda pollo: [pollo]

addPollo = lambda planeta, pollo: [] + [pollo]

polloDebil = lambda pollo: pollo[3] > 2

esDebil = lambda planeta: sum(map(polloDebil, planeta)) == 0

entrenar = lambda planeta, entrenador: list(map(entrenador, planeta))

hacerViajeEspiritual = lambda entrenadores, pollo: [f(pollo) for f in entrenadores]

raton = lambda peso, altura, bigotes: (peso, altura, bigotes)

brujaTapita = lambda raton, pollo: (pollo[0], pollo[1], pollo[2] + (raton[0] * raton[1] - raton[2]), pollo[3])

marioBross = lambda smn, arteMarcial, pollo: (pollo[0] + "super mario" * smn, pollo[1], pollo[2], pollo[3] + ["saltar", "agacharse"] + [arteMarcial]) if arteMarcial not in pollo[3] else (pollo[0] + "super mario" * smn, pollo[1], pollo[2], pollo[3] + ["saltar", "agacharse"])

chickenNorris = lambda: ("Chicken Norris", 9000000, 90, ["karate1", "karate2", "karate3"])

def alimentar(alpiste, pollo):
    if estaDesnutrido(pollo):
        return engordar(alpiste, pollo)
    if esAdulto(pollo):
        return engordar(alpiste * 0.5, pollo)
    return pollo

ginger = pollo("ginger", 8000000, 150, [])
rocky = pollo("rocky", 1000000, 300, [])
little = pollo("little", 500000, 100, [])