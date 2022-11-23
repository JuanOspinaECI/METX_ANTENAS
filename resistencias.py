import numpy as np


def eficiencia(R_rad, R_per):
    ef = R_rad/(R_rad + R_per)
    return ef

def res_perdidas(material=1,radio=2,frec=10*10**6, long = 1/2 ):
    #Long (longitud) en término de lambda
    #1 - Cobre
    #2 - Plata
    #3 - Aluminio
    #4 - Hierro
    
    material = {
        1: 59.6*10**6,
        2: 63.09*10**6,
        3: 37.8*10**6,
        4: 15.3*10**6
    }
    lon_onda = (3*10**8)/(frec)
    l = lon_onda/long
    Rs = sqrt((np.pi*frec*4*np.pi*10**(-7))/material)
    return Rs*(l/(2*np.pi*radio))
    
    

    
