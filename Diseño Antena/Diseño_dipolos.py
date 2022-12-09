
import math

#Preguntar usuario por el tipo de dipolo resonante que desea diseñar:

print("Cual diseño desea realizar")
print("1. lambda/2")
print("2. lambda")
print("3. 3 lambda/2")
print("4. 2 lambda")

#Diccionario que tiene el valor de la longitud resonante a calcular, segpun el dipolo seleccionado
practica_lista = {
        1: 0.48,
        2: 0.96,
        3: 1.44,
        4: 1.92
    }

#Diccionario de longitud en términos de lambda según la que el usuario eligió
longitud_lista = {
        1: 1/2,
        2: 1,
        3: 3/2,
        4: 2
    }
#Adquirir el tipo de dipolo que desea el usuario
opc = int (input())

#Adquirir la frecuencia de operación del dipolo
print("Frecuencia central de operación en Hz")
frec = float(input())

#Adquirir el diametro del dipolo a diseñar 
print("Diametro del dipolo en mm")
D = float(input()) * 10**-3

#Calculo de londitud de onda
lmbd = 3*10**8/frec
#Calculo de longitud teorica
L = lmbd*longitud_lista.get(opc)
#Calculo del parametro A
A = (L/D)/(1+L/D)
#Calculo de la longitu resonante según parametro A y valor del diccionario
L_f = A*lmbd*practica_lista.get(opc)
#Calculo de la resistencia de entrada del dipolo según el dipolo legido
Rn = 150*math.log(L/D)  
factor_lista = {
        1: 67,
        2: Rn**2/67,
        3: 95,
        4: Rn**2/95,
    }
#Motrar resultado de la longitud de cada brazo y la resistencia de entrada calculada
print("Longitud del brazo práctica: ", L_f/2, "[m]")
print("Resistencia de entrada: ", factor_lista.get(opc), "Ohmios")
