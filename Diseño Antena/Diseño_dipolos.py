
import math

print("Cual diseño desea realizar")
print("1. lambda/2")
print("2. lambda")
print("3. 3 lambda/2")
print("4. 2 lambda")

practica_lista = {
        1: 0.48,
        2: 0.96,
        3: 1.44,
        4: 1.92
    }

longitud_lista = {
        1: 1/2,
        2: 1,
        3: 3/2,
        4: 2
    }

opc = float (input())

print("Frecuencia central de operación en Hz")
frec = float(input())

print("Diametro del dipolo en mm")
D = float(input()) * 10**-3

lmbd = 3*10**8/frec
L = lmbd*longitud_lista.get(opc)
A = (L/D)/(1+L/D)

L_f = A*lmbd*practica_lista.get(opc)
Rn = 150*math.log(L/D)  
factor_lista = {
        1: 67,
        2: Rn**2/67,
        3: 95,
        4: Rn**2/95,
    }

print("Longitud del brazo práctica: ", L_f/2, "[m]")
print("Resistencia de entrada: ", factor_lista.get(opc), "Ohmios")
