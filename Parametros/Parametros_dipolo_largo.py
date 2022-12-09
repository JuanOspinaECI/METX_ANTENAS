import numpy as np
import os
import sys
from fractions import Fraction
import diagrama_rad
import parametros_1
import resistencias
import math


print("Parametros de radiacion de un dipolo largo en recepción")
#Se pregunta al usuario por longitud del dipolo en término de lambda
l_dipolo = float(Fraction(input("Ingrese longitud del dipolo en término de lambda > 1/10:  ")))
#Si el usuario ingrea un valor menor a 1/10 se pregunta de nuevo
while (l_dipolo<1/10):
    l_dipolo = float(Fraction(input("Ingrese longitud del dipolo en término de lambda > 1/10:  ")))
#Se pregunta al usuario la frecuencia de opración del dipolo
fr = float(input("Ingrese frecuencia de operación del dipolo:  "))
#Adicionalmente el factor Q para calcular reactancia y ancho de banda
fac_q = float(input("Ingrese el valor del factor Q del dipolo: "))

#Llamado a la funacion diag_rad para generar el diagrama de radiación
#El parametro que se debe ingresar el la longitud del dipolo en termino de lambda
diagrama_rad.diag_rad(l_dipolo)

print("")

#Calcular parametros

#Calculo de la longitud teórica de un brazo del dipolo
l_brazo = l_dipolo/2
#Se envia la longitud a la función pot_dir_den
#como parametro se debe enviar la longitud del brazo en términos de lambda

#A las soguientes funciones que calculan algunos parámetros,
#se debe enviar la longitud del brazo del dipolo

#Almacenar la potencia con la funcion pot_porm
Pot = parametros_1.pot_prom(l_brazo)
#Almacenar la densidad de potencia con la función densidad_pot
densidad_pot = parametros_1.densidad_pot(l_brazo)
#Almacenar la directividad con la función directividad
direct = parametros_1.directividad(l_brazo)
#Almacenar la resistencia de radiación con la función res_rad
res_rad = parametros_1.res_rad(l_brazo)

#Mostrar parametros previamente calculados
print("Potencia Radiada Promedio")
print(Pot, "Imax^2  [W]")

print()
print("Densidad de potencia radiada")
print(densidad_pot, "Imax^2/r [W/m^2]")


print()
print("Directividad")
print(direct, "Estero radianes")
print()
print("Resistencia de Radiacion")
print(2*Pot, "Ohmios")
print()

#Preguntar al usuario que tipo de material se usará en la antea
#Con el fin de calcular la resistencia de pérdidas
print("Ingrese numero de material de la antena")
print("1- Cobre")
print("2- Plata")
print("3- Aluminio")
print("4- Hierro")
mat = int(input())

print("Radio del material en mm")
rad = float(input())*10**-3

#Calculo de la resistencia de pérdidas con la función res_perdidas
#Como parametros la funcion necestia, el material, el radio, la frecuencia y la londitud del dipolo
r_perdidas = resistencias.res_perdidas(mat,rad,fr,l_dipolo)
print()
print("Resistencia de pérdidas: ", r_perdidas)
print()
#Para calcular la eficiencia se usa la función eficiencia
#Necesita como parametros la resistenica de radiación y la resistencia de pérdidas
ef = resistencias.eficiencia(res_rad,r_perdidas)
print("Eficiencia: ", ef)

#Mostrar los valores de ganancia en veces y dB
print("Ganancia: ", ef*direct, " veces")
print("Ganancia: ", 10*math.log(ef*direct,10), " dBi")
print()
print("Impedancia")

#Calculo de la reactancia con el valor de Q ingresado
reactancia = r_perdidas*fac_q/(2*np.pi*fr)
print(r_perdidas+res_rad, "+j", abs(reactancia))
print()
#Calculo de ROE según reactancia y resistencia real total 
roe = resistencias.roe_coaxial(r_perdidas+res_rad,reactancia)
#Calculo ancho de banda según ROE y Q
anc_ban = (roe-1)/(fac_q*math.sqrt(roe))
print("Ancho de banda de la antena con cable coaxial:", anc_ban, " Hz" )
