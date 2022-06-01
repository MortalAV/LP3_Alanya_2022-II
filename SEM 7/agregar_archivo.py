# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:58:17 2022

@author: Equipo
"""

archivo = open("noticia.txt","at")

#\n es para agregar el contenido en una línea final

contenido = "\nFuente: La Vanguardia"

archivo.write(contenido)

archivo.close()