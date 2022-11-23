from sympy import integrate, init_printing, cos, sin
#from sympy.abc import 
import numpy as np
from sympy.abc import x




def pot_dir_den(H_lambda=1/4,I_max=1,r=1):
    #I_max = 1
    r = 1
    H_lambda = 1/4
    z_espacio = 120*np.pi
    KH = 2*np.pi*H_lambda


    Total = float(integrate((cos(KH*cos(x))-cos(KH))**2/sin(x),(x,0,np.pi)))
    Pot = Total*z_espacio*I_max**2/(4*np.pi)
    print(Pot)

    
    print("Densidad de potencia radiada")
    print(Total/(4*np.pi), "Imax^2/r [W/m^2]")

    print("Directividad")
    x1 = np.linspace(0.00001,np.pi-0.00001, num=1000)
    #print(x1)
    f = (np.cos(KH*np.cos(x1))-np.cos(KH))**2/np.sin(x1)
    max_f = max(f)
    print(Total/max_f, "rad")
    print(Total/(max_f*np.pi)*180, "grados")

    print("Resistencia de Radiacion")
    print(2*Pot, "Ohmios")
    
pot_dir_den(1/2)



