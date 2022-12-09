

import numpy as np
import matplotlib.pyplot as plt


def diag_rad(H_lambda=1/4,i_max=1,r=1):

    #Generación de vector theta para coordenadas poolares
    theta  = np.linspace(0.00001,np.pi-0.00001, num=1000)
    theta = np.concatenate((theta,np.linspace(np.pi+0.00001,2*np.pi-0.00001)), axis=None)
    #Calculo de la impedancia del espacio libre
    z_espacio = 120*np.pi
    #Calulo de KH número de onda y longitud del brazo del dipolo
    KH = 2*np.pi*H_lambda
    #Generacion del los valores de E con el vector theta
    E = (z_espacio*i_max/(2*np.pi*r)) * ((np.cos(KH*np.cos(theta))-np.cos(KH))/np.sin(theta))
    #Normalizar campo Electrico
    E_abs = np.absolute(E)
    E_abs = E_abs/max(E_abs)
    #Graficar en coordenadas poolares
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="polar")
    ax.plot(theta,E_abs)


    plt.show()


#diag_rad(1/4)
