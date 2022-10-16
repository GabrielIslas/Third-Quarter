grito = lambda onomatopeya, intensidad, mojoLaCama: (onomatopeya, intensidad, mojoLaCama)

ninio = lambda nombre, edad, altura: (nombre, edad, altura)

energiaDeGrito = lambda grito: len(grito[0]) * (grito[1] ** 2) if grito[2] else 3 * len(grito[1]) + grito[2]

sullivan = lambda ninio: ("A" * len(ninio[0] + "GH"), 20 / ninio[1], True if ninio[1] < 3 else False)

conteoVocales = lambda cadena: cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u")

randall = lambda ninio: ("¡Mamadera!", conteoVocales(ninio[0]), True if ninio[2] > 0.8 and ninio[2] < 1.2 else False)

chuck = lambda ninio: ("abcdefghijklmnopqrstuvwxyz", 1000, True)

aplicarFunciones = lambda funciones, elemento: list(map(lambda funcion: funcion(elemento), funciones))

equipo = lambda monstruos, ninio: aplicarFunciones(monstruos, ninio)