# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:42:20 2022

@author: Joel Alanya
"""

import gestion_de_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")
    
def crear():
    print("*** CREAR ARCHIVO ***")
    archivo = input("Crear archivo: ")
    contenido = input("Contenido del archivo: ")
    gestion_de_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("*** ELIMINAR ARCHIVO ***")
    archivo = input("Quiero eliminar el archivo")
    gestion_de_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("*** AGREGAR CONTENIDO A UN ARCHIVO ***" )
    archivo = input("Quiero agregar contenido alarchivo: ")
    contenido = input("El contenido adicional del archivo es: ")
    gestion_de_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("*** MOSTRAR CONTENIDO DE UN ARCHIVO ***")
    archivo = input("Quiero mostrar el contenido del archivo: ")
    print(gestion_de_archivos.leer_archivo(archivo))
    
def salir():
    print("Gracias por su paso. Chaito")

def error():
    print("Opción invalida")
    
#La lógica para el menú de opciones
opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Seleccione una opción [1-5]: "))
    if opcion==1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion==3:
        agregar()
    elif opcion==4:
        listar()
    elif opcion==5:
        salir()
    else:
        error