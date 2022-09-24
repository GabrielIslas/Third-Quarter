# -*- coding: utf-8 -*-
"""
Escribir un programa que alamcene tus asignaturas en una lista
Pregunte al usuario la nota que ha sacado en cada asignatura y despues las
muestre en pantalla con el mensaje:
En <asignatura> has sacado <nota>
donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una
de las correspondientes notas introducidas por el usuario
"""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Programacion", "Ingles"]
notas = []

for x in asignaturas:
    nota = input("Que nota has sacado en " + x + "? ")
    notas.append(nota)
    
print("\n")

for x in range(len(asignaturas)):
    print("En " + asignaturas[x] + " has sacado: " + notas[x])    


