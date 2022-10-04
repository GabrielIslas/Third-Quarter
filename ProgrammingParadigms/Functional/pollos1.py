from math import pi

pollo = lambda nombre, dias, peso: (nombre, dias, peso)

edad = lambda pollo: pollo[1] / (pi * 365 ** 2)

esAdulto = lambda pollo: edad(pollo) > 5

esJoven = lambda pollo: not esAdulto(pollo)

estaDesnutrido = lambda pollo: (esJoven(pollo) and pollo[2] < 50) or (esAdulto(pollo) and pollo[2] < 200) or (len(pollo[0]) % 2 == 0)

engordar = lambda alpiste, pollo: (pollo[0], pollo[1], pollo[2] + alpiste)

def alimentar(alpiste, pollo):
    if estaDesnutrido(pollo):
        return engordar(alpiste, pollo)
    if esAdulto(pollo):
        return engordar(alpiste * 0.5, pollo)
    return pollo

ginger = pollo("ginger", 8000000, 150)
rocky = pollo("rocky", 1000000, 300)
little = pollo("little", 500000, 100)

print(ginger)