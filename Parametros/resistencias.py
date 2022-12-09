import numpy as np
import math 
import cmath

def eficiencia(R_rad, R_per):
    ef = R_rad/(R_rad + R_per)
    return ef

def res_perdidas(material=1,radio=2*10**-3,frec=10*10**6, long = 1/2 ):
    #Long (longitud) en término de lambda
    #1 - Cobre
    #2 - Plata
    #3 - Aluminio
    #4 - Hierro
    
    mat_lista = {
        1: 59.6*10**6,
        2: 63.09*10**6,
        3: 37.8*10**6,
        4: 15.3*10**6
    }
    material=mat_lista.get(material)
    #print(material)
    lon_onda = (3*10**8)/(frec)
    l = lon_onda*long
    #Calculo de la resitencia de pérdidas según el material y la frecuencia
    Rs = math.sqrt((np.pi*frec*4*np.pi*10**(-7))/material)
    return Rs*(l/(2*np.pi*radio))


def roe_coaxial(real,img):
    #Calculo del ROE según una impedancia de entrada (Parte real e imaginaria)
    z = complex(real,img)
    ref = (z-70)/(z+70)
    ref_abs = abs(ref)
    ROE = (1+ref_abs)/(1-ref_abs)
    return ROE

    
