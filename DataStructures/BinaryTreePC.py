def ArbolBinario(raiz):
    return [raiz,[],[]]

def insertIzquierda(raiz,nuevoValor):
    (rama_izquierda) = raiz.pop(1)
    if len(rama_izquierda) > 1:
        raiz.insert(1,[nuevoValor,rama_izquierda,[]])
    else:
        raiz.insert(1, [nuevoValor,[],[]])
        return raiz

def insertDerecha(raiz,nuevoValor):
    rama_derecha = raiz.pop(2)
    if len(rama_derecha) > 1:
        raiz.insert(2,[nuevoValor,[],rama_derecha])
    else:
        raiz.insert(2,[nuevoValor,[],[]])
        return raiz

def identificarPadreHijo(raiz):
    if raiz[1] != [] or raiz[2] != []:
        print("Padre: " + str(raiz[0]))
        print("Hijos: ")
        if raiz[1] != []:
            print(raiz[1][0])
        if raiz[2] != []:
            print(raiz[2][0])
    if raiz[1] != []:
        identificarPadreHijo(raiz[1])
    if raiz[2] != []:
        identificarPadreHijo(raiz[2])

raiz = ArbolBinario(1)
insertIzquierda(raiz, 2)
insertDerecha(raiz, 3)
insertIzquierda(raiz[1], 4)
insertIzquierda(raiz[2], 5)
insertDerecha(raiz[2], 7)

identificarPadreHijo(raiz)