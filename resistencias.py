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
    Rs = math.sqrt((np.pi*frec*4*np.pi*10**(-7))/material)
    return Rs*(l/(2*np.pi*radio))

def reactancia(l_dipolo, radio, frecuencia):
    
    KH = 2*np.pi*l_dipolo/2
    H = l_dipolo/2
    z = 120*(np.log(2*H/radio)-1)
    #xc = z*1/math.tan(KH)
    xc=z ##revisar
    return -xc

def roe_coaxial(real,img):
    z = complex(real,img)
    ref = (z-70)/(z+70)
    ref_abs = abs(ref)
    ROE = (1+ref_abs)/(1-ref_abs)
    return ROE

    
