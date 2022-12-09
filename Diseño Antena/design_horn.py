# Programa de diseño de bocina piramidal
#
# Juan Camilo Ospina

import numpy as np
import math


def dsg():

    #Adquirir datos de usuario
    #Ganancia en db
    #frecuencia en GHz
    #Tamaño a de la guia de onda en cm
    #Tamaño b de la guia de onda en cm
    ganancia = float(input("Ingrese la ganancia requerida en dB: "))
    #ganancia = 15 #db
    frecuencia = float(input("Ingrese frecuencia de operacion en GHz: "))
    #frecuencia = 11 #GHz
    guia_a = float(input("Ingrese la longitud a de la guia de onda en cm: "))
    guia_a = guia_a *10**-2
    #guia_a = 2.286*10**-2 #cm
    guia_b = float(input("Ingrese la longitud b de la guia en cm: "))
    guia_b = guia_b *10**-2
    #guia_b = 1.016*10**-2 #cm

    #Calcular longitud de onda
    lmbd = 3*10**8/(frecuencia*10**9) 

    #Calcular la ganancia en veces
    gan_veces = 10**(ganancia/10)

    #Inicio de diseño

    #Calculo de primer valor de prueba para las iteraciones
    x = gan_veces/(np.pi*2*(np.pi*2)**(1/2))

    #Creacion de ambas variables que tienen que converger A y B
    A = 1
    B = 2
    ak=0

    #Se haran máximo 10 iteraciones, si no se cumple el criterio de diseño
        #Se pregunta de nuevo los datos al usuario porque el diseño no es posible          
    for k in range(10000000):
        
        ## Parte A de la ecuacion

        A_1 = ((x*2)**(1/2)- guia_b/lmbd)**(2)
        A = A_1 * (2*x-1)

        ## Parte B de la ecuacion

        B_1 = gan_veces/(2*np.pi)
        B_1 = B_1*(3/(2*np.pi))**(1/2)
        B_1 = B_1*((x)**(-1/2))
        B_1 = B_1 - guia_a/lmbd
        B_1 = B_1**2
        
        B_2 = gan_veces*gan_veces/(6*(np.pi**3))
        B_2 = B_2 * (1/x)
        B_2 += -1

        B = B_1 * B_2

        
        #Check si los valores convergen y estan dentro del rango aceptado
        
        if(abs(A-B)<0.1):
            #print(A)
            #print(B)
            ak = 1
            break
        #Si aun no convergen modificar el valor de x segun la diferencia
        else:
            if(A>B):
                if(abs(A-B)<0.02):
                    x = x -0.0001
                else:
                    x = x-0.0005
            else:
                if(abs(A-B)<0.02):
                    x = x +0.0001
                else:
                    x = x+0.0005
    # Si al final de la iteraciones el modelo no logró converger
        #Se pregunta nuevamente al usuario los datos para un nuevo diseño
    if (ak == 0):
        print("Luego de 10 millones de iteraciones no se logro cumplir con la condicion")
        print("Intente nuevamente con dimensiones distintas o menor ganancia")
        ##LLamar nuevamente funcion
    else:
        #calculo de los parametros pe y ph con el valor encontrado x
        p_e = x*lmbd
        p_h = gan_veces**2*lmbd
        p_h = p_h/(8*np.pi**3*x)

        #tamaño a y b de la bocina piramidal
        hor_a = (3*lmbd*p_h)**(1/2)
        hor_b = (2*lmbd*p_e)**(1/2)

        #Calculo de P_1 Y P_2
        P_1 = (-guia_b + hor_b)*((p_e/hor_b)**2 - 0.25)**(1/2)
        P_2 = (-guia_a + hor_a)*((p_h/hor_a)**2 - 0.25)**(1/2)

        
        #Curva de aproximacion Gh
        A_d = hor_a/lmbd * (50*lmbd/p_h)**(1/2)
        #Si es igual o menor a 10.6 y = 6.7x + 19.6
        #Si es un valor entre 10.6 y 12.65 aplicar 2.44*x +69.15
        #Si esta en el rango entre 12.65 y 14.7 
            #x = x - (x-12.65)
            #Luego utilizar ecuación de entre 10.6 y 12.65
        #Si es un valor mayor a 14.7 y = -6.58x + 191.8

        #Calculo de directividad Dh
        
        #Primero se calcula la ganancia Gh según curva de aproximación de Gh
        if(A_d<= 10.6):
            Gh = 6.7*A_d +19.6
        elif(A_d>10.6 and A_d<=12.65):
            Gh = 2.44*A_d +69.15
        elif(A_d>12.65 and A_d<14.7):
            A_d = A_d - (A_d-12.65)
            Gh = 2.44*A_d +69.15
        else:
            Gh = -6.58*A_d + 191.8

        Dh = guia_b/lmbd * Gh
        Dh = Dh * 1/((50*lmbd/(p_h))**(1/2))


        #Curva de aproximacion de Ge
        B_d = hor_b/lmbd * (50*lmbd/p_e)**(1/2)
        #Si es igual o menor a 8 y = 6.66x + 21.7
        #Si es un valor entre 8 y 10.1 aplicar 3.21*x + 49.3
        #Si esta en el rango entre 10.1 y 12.2 
            #x = x - (x-10.1)
            #Luego utilizar ecuación de entre 8 y 10.1
        #Si es un valor mayor a 12.2 y menor a 18 y = -9.74x + 193.85
        #Si es mayor a 18 y = 18.5

        #Calculo de directividad De

        #Primero se calcula Ge según curva de aproximación
        if(B_d<= 8):
            Ge = 6.66*B_d +21.7
        elif(B_d>8 and B_d<=10.1):
            Ge = 3.21*B_d + 49.3
        elif(B_d>10.1 and A_d<=12.2):
            B_d = B_d - (B_d-10.1)
            Ge = 3.21*B_d + 49.3
        elif(B_d>12.2 and B_d<18):
            Ge = -9.74*B_d + 193.85
        else:
            Ge = 18.5

        De = guia_a/lmbd * Ge
        De = De * 1/((50*lmbd/(p_e))**(1/2))


        #Directividad total

        Dt = np.pi*lmbd**2/(32*guia_a*guia_b)*De*Dh #en veces

        Dt_dB = np.log(Dt)*10 


        # Calculo de ganancia

        G_dBi = 8.1 + 10*np.log(hor_a*hor_b/(lmbd**2)) 
        print("Parameros del diseño:")
        print("Longiud A de la bocina: ",hor_a, "m" )
        print("Longitud B de la bocina: ", hor_b, "m")
        print("P1: ", P_1)
        print("P2: ", P_2)
        print("pe: ", p_e)
        print("ph: ", p_h)

        print("Directividad")
        print("En el plano H: ", Dh , "veces")
        print("En el plano E: ", De, "veces")
        print("Total: ", Dt, " veces")
        print("Total: ", Dt_dB, "dB")

        print("Ganancia: ", G_dBi , "dBi")
        
