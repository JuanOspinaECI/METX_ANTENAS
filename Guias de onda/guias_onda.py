import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math
pi = np.pi
c = 3*10**8
e0 = 8.854*10**(-12)
u0 = pi*4*10**(-7)


def frec_corte(a=2*10**(-3),b=1*10**(-3),er=1,m=1,n=0):
    # Fución para calcular la frecuencia de corte del modo
    # se debe enviar el tamaño de la guía en metros (a y b)
    # el valor de la permitividad relativa
    # el modo a calular (m y n)
    frec = c/(2*pi/(math.sqrt(er)))*math.sqrt((pi*m/a)**2+(n*pi/b)**2)
    return frec

def lambda_corte(a=2*10**(-3),b=1*10**(-3)):
    # Función que calcula la longitud de onda de corte
    # Se necetia como parametro las dimensiones de la guía
    lm_c = 2/math.sqrt((m/a)**2+(pi/b)**2)
    return lm_c

def lambda_op(f_c,f_op):
    # Función que calcular la longitud de onda respecto a la frecuencia de corte del modo y 
    #la frecuencia de la onda que se propagará
    l = c/math.sqrt(f_op**2 - f_c**2)
    return l

def c_fase(f_c,f_op,e=1,u=1):
    # Función que calcual la constante de fase según el modo y la frecuencia de la onda a propagar
    # Se debe enviar como parametro frecuencia de corte, de operacion y de ser necesario las permitividades
    b = 2*pi*f_op*math.sqrt(e*u)*1/c*math.sqrt(1-(f_c/f_op)**2)
    return b

def z_TE(f_c,f_op,e=1,u=1):
    # Función que calcula la resistencia del modo TE
    # Se debe enviar como parametos la freceuncia de corte del modo, la frecuencia de la onda a propagar
    # las permitividades si son distintas a 0
    n = math.sqrt((u0*u)/(e0*e))
    z = n/math.sqrt(1-(f_c/f_op)**2)
    return z

def z_TM(f_c,f_op,e=1,u=1):
    # Función que calcula la impedancia del modo TM
    # Se debe enviar como parametos la freceuncia de corte del modo, la frecuencia de la onda a propagar
    # las permitividades si son distintas a 0  
    n = math.sqrt((u0*u)/(e0*e))
    z = n*math.sqrt(1-(f_c/f_op)**2)
    return z

f_ak = True #variable que controla si se deben seguir calculando los parametros del siguiente modo
# Preguntar al usuario frecuencia de operación en la guía
frec_op = float(input("Ingrese la frecuencia de operación en la guía (GHz): "))
frec_op = frec_op*10**9
# Preguntar al usuario las dimensiones de la guía
a = float(input("Introduzca la dimensión a de la guía en (mm):"))
a = a*10**(-3)
b = float(input("Introduzca la dimensión b de la guía en (mm): "))
b = b*10**(-3)
# Preguntar al usuario la permitividad electrica relativa
e = float(input("Ingrese permitividad electrica relativa "))
# Preguntar al usuario la permitividad magnetica relativa
u = float(input("Ingrese permitividad magnetica relativa "))

#Inicio de cálculo de parametros según el modo
#Inicia en modo m = 1 n = 0
m = 1
n = 0
while(f_ak==True):
    fr_corte = frec_corte(a,b,e,m,n)
    if (fr_corte> frec_op): #Si la frecuencia de corte del siguiente modo es mayor a la de operacion cerrar ciclo
        print("La frecuencia máxima de operación es menor al modo TE "  + str(m) + " " + str(n))
        f_ak=False
        break
    print("Parámetros para modo TE " + str(m) + " " + str(n))
    print("   Frecuencia de corte: " + str(fr_corte) + " Hz")
    print("   Longitud de onda de operación en el modo: " + str(lambda_op(fr_corte,frec_op)) + " m")
    print("   Contanste de fase " + str(c_fase(fr_corte,frec_op,e,u)) + " rad/m")
    print("   Velocidad de fase " + str(2*pi*frec_op/c_fase(fr_corte,frec_op,e,u)) + " m/s")
    print("   Impedancia " + str(z_TE(fr_corte,frec_op,e,u)) + " ohms")
    print()
    if(n!=0):
        print(" Parametros adicionales para el modo TM "+ str(m) + " " + str(n))
        print("   Impedancia " + str(z_TM(fr_corte,frec_op,e,u)) + " ohms")
        print()
    else: print()
    if (n< m):
        n += 1
    elif(m==n):
        m += 1
        n = 0


