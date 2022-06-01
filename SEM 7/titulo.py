# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:36:49 2022

@author: Equipo
"""

#Importamos librería

import camelcase

nombre = "Joel Edwin Alanya Villar"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con camelcase.....")

#Imprimimos el nombre en formato título
#Utilizamos camelcase

print(cam.hump(nombre))

#Para resolver el problema 
#Creamos otro objeto cam2
#Al definir el objeto, incluimos los argumentos
#'joel' y 'villar'

cam2=camelcase.CamelCase('Joel','Villar')
print(cam2.hump(nombre))

