from sympy import integrate, init_printing, cos, sin
#from sympy.abc import 
import numpy as np
from sympy.abc import x

from scipy import integrate



Pot = 0
Total = 0
direct = 0

def pot_dir_den(H_lambda=1/4,I_max=1,r=1,j=0):
    #I_max = 1
    #r = 1
    #H_lambda = 1/4
    z_espacio = 120*np.pi
    KH = 2*np.pi*H_lambda

    x1 = np.linspace(0.00001,np.pi-0.00001, num=1000)
    y1 = (np.cos(KH*np.cos(x1))-np.cos(KH))**2/np.sin(x1)
    I1 = integrate.simpson(y1, x1)

    Total = I1
    Pot = Total*z_espacio*I_max**2/(4*np.pi)

    f = (np.cos(KH*np.cos(x1))-np.cos(KH))**2/np.sin(x1)
    max_f = max(f)
    direct = (4*np.pi)/Total*max_f

    
    if (j==1):
        return Pot
    elif (j==2):
        return Total/(4*np.pi)
    elif (j==3):
        return direct
    elif (j==4):
        return 2*Pot
    else:
        return print()

def pot_prom(H_lambda=1/4,I_max=1,r=1):
    return pot_dir_den(H_lambda,I_max,r,1)
def densidad_pot(H_lambda=1/4,I_max=1,r=1):
    return pot_dir_den(H_lambda,I_max,r,2)
def directividad(H_lambda=1/4,I_max=1,r=1):
    return pot_dir_den(H_lambda,I_max,r,3)
def res_rad(H_lambda=1/4,I_max=1,r=1):
    return pot_dir_den(H_lambda,I_max,r,4)


