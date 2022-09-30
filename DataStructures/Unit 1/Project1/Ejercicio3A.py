# binary tree structure
def ArbolBinario(raiz):
    return [raiz,[],[]]
# insert element to the left of the node
def insertIzquierda(raiz,nuevoValor):
    rama_izquierda = raiz.pop(1)
    if len(rama_izquierda) > 1:
        raiz.insert(1,[nuevoValor,rama_izquierda,[]])
    else:
        raiz.insert(1, [nuevoValor,[],[]])
        return raiz
# insert element to the right of the node
def insertDerecha(raiz,nuevoValor):
    rama_derecha = raiz.pop(2)
    if len(rama_derecha) > 1:
        raiz.insert(2,[nuevoValor,[],rama_derecha])
    else:
        raiz.insert(2,[nuevoValor,[],[]])
        return raiz
# returns de list of nodes with their levels [nodeValue, level]
def niveles(raiz, nivel = 0, listaNiveles = []):
    nivelesI(raiz, nivel, listaNiveles)
    print(listaNiveles)
    return listaNiveles
# secondary function for the list of nodes, this one actually modifies the list
# previous function is in charge of starting the process, and returning the finished list
def nivelesI(raiz, nivel = 0, listaNiveles = []):
    listaNiveles.append([raiz[0], nivel])
    if raiz[1] != []:
        nivelesI(raiz[1], nivel + 1, listaNiveles)
    if raiz[2] != []:
        nivelesI(raiz[2], nivel + 1, listaNiveles)
# this takes the levels list made and prints it like the exercise asked
def printNiveles(raiz):
    listaNiveles = niveles(raiz)
    nodosPorNiveles = []
    for nodo in listaNiveles:
        if len(nodosPorNiveles) < nodo[1] + 1:
            nodosPorNiveles.append([])
        nodosPorNiveles[nodo[1]].append(nodo[0])
    for nivel in nodosPorNiveles:
        print(nivel)
# building tree
raiz = ArbolBinario(8)
insertIzquierda(raiz, 3)
insertDerecha(raiz, 10)
insertDerecha(raiz[2], 14)
insertIzquierda(raiz[2][2], 13)
insertIzquierda(raiz[1], 1)
insertDerecha(raiz[1], 6)
insertIzquierda(raiz[1][2], 4)
insertDerecha(raiz[1][2], 7)
printNiveles(raiz)