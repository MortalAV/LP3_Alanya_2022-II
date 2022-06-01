# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:58 2022

@author: Equipo
"""

archivo = open("archivo_de_prueba.txt","wt")

contenido = "Línea1 Hola gente estoy en clases. No molestar\nLínea2 Siguiente semana parciales pipipip :c"

archivo.write(contenido)

archivo.close()