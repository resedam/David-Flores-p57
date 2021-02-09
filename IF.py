# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:17:46 2020

@author: david
"""

nombre=input("ingrese su nombre""\n")
apellido=input("ingrese el apellido""\n")
edad=input("ingrese su edad""\n")
voto=input("escriba de la lista su candidato: Lasso, Noboa, Arauz, Hervas""\n" )
s= " "
print("El usuario se llama",nombre,s,apellido,s,"tiene",edad,s,"años")

if voto == "Lasso":
    print ("y también apoya a la derecha, la libertad, junto con la seguridad ciudadana")
elif voto == "Noboa":
    print("y también apoya a la derecha, las empresas y la banca fuerte")
elif voto == "Hervas":
    print ("y también apoya a la izquierda, el desarrollo sustentable, y un plan de gobierno innovador y de solidaridad")
elif voto == "Arauz":
    print("y también apoya a la izquierda, el desarrollo popular y el plan de gobierno Correista")
else:
    print("y al parecer tiene otro candidato,votará nulo o cometió algún error al ingresar la información")