def ordenacion_insercion(lista):
    for indice in range(1, len(lista)):
        valor = lista[indice]
        posicion = indice

        while posicion > 0 and lista[posicion - 1] > valor:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
        lista[posicion] = valor

lista = [5, 4, 3, 2, 1]
ordenacion_insercion(lista)
print(lista)