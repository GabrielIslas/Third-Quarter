def ordenacion_seleccion(lista):
    for numero in range(len(lista) - 1, 0, -1):
        indiceMax = 0
        for indice in range(1, numero + 1):
            if lista[indice] > lista[indiceMax]:
                indiceMax = indice
        temporal = lista[numero]
        lista[numero] = lista[indiceMax]
        lista[indiceMax] = temporal

lista = [5, 4, 3, 2, 1]
ordenacion_seleccion(lista)
print(lista)