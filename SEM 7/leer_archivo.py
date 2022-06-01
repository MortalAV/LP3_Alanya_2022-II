# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:42:32 2022

@author: Equipo
"""

noticia = open("noticia.txt","rt",encoding='utf-8')

datos_noticias = noticia.read()

print(datos_noticias)