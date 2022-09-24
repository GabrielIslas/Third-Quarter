# -*- coding: utf-8 -*-
"""
Un estudiante universitario decidio armar un programa que permitira a los
potenciales estudiantes en linea del extranjero llenar el formulario
y buscar mas informacion sobre los cursos que les interesan.
El formulario debe tener lo siguiente
Bienvenido a la universidad ABC
Por favor introduzca la informacion necesaria para comenzar
Introduzca su nombre
Introduzca su numero de telefono
Introduzca su correo electronico
Elija el curso
Imprimir todo
"""

print("Bienvenido a la universidad ABC")
nombre = input("Introduzca su nombre: ")
telefono = input("Introduzca su numero telefonico: ")
correo = input("Introduzca su correo electronico: ")
curso = input("Elija su curso: ")

print(f'\nBienvenido {nombre} a la universidad ABC')
print(f'Esperamos que el curso de {curso} sea de su agrado')
print(f'Su numero de telefono es {telefono}')
print(f'Su correo electronico es {correo}')


