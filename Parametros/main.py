import numpy as np
import os
import sys
from fractions import Fraction
import diagrama_rad
import parametros_1
import resistencias
import math


print("Parametros de radiacion de un dipolo largo en recepción")
l_dipolo = float(Fraction(input("Ingrese longitud del dipolo en término de lambda > 1/10:  ")))
while (l_dipolo<1/10):
    l_dipolo = float(Fraction(input("Ingrese longitud del dipolo en término de lambda > 1/10:  ")))
fr = float(input("Ingrese frecuencia de operación del dipolo:  "))

fac_q = float(input("Ingrese el valor del factor Q del dipolo: "))

diagrama_rad.diag_rad(l_dipolo)

print("")

#Calcular parametros

l_brazo = l_dipolo/2
parametros_1.pot_dir_den(l_brazo)

Pot = parametros_1.pot_prom(l_brazo)
densidad_pot = parametros_1.densidad_pot(l_brazo)
direct = parametros_1.directividad(l_brazo)
res_rad = parametros_1.res_rad(l_brazo)
print("Potencia Radiada Promedio")
print(Pot, "Imax^2  [W]")

print()
print("Densidad de potencia radiada")
print(densidad_pot, "Imax^2/r [W/m^2]")

    #r_1 = ["Densidad de potencia radiada", Total/(4*np.pi),"Imax^2/r [W/m^2]" ]

print()
print("Directividad")
print(direct, "Estero radianes")
print()
print("Resistencia de Radiacion")
print(2*Pot, "Ohmios")
print()

print("Ingrese numero de material de la antena")
print("1- Cobre")
print("2- Plata")
print("3- Aluminio")
print("4- Hierro")
mat = int(input())

print("Radio del material en mm")
rad = float(input())*10**-3

r_perdidas = resistencias.res_perdidas(mat,rad,fr,l_dipolo)
print()
print("Resistencia de pérdidas: ", r_perdidas)
print()
ef = resistencias.eficiencia(res_rad,r_perdidas)
print("Eficiencia: ", ef)

print("Ganancia: ", ef*direct, " veces")
print("Ganancia: ", 10*math.log(ef*direct,10), " dBi")
print()
#print("Impedancia")
#reactancia = resistencias.reactancia(l_dipolo,rad,fr)
#print(r_perdidas+res_rad, "-j", abs(reactancia))
#print()
#Q = abs(reactancia)/r_perdidas
#print("Factor Q:", Q)
#print()
reactancia = r_perdidas*fac_q/(2*np.pi*fr)
roe = resistencias.roe_coaxial(r_perdidas+res_rad,reactancia)
anc_ban = (roe-1)/(fac_q*math.sqrt(roe))
print("Ancho de banda de la antena con cable coaxial:", anc_ban, " Hz" )
