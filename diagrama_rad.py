

import numpy as np
import matplotlib.pyplot as plt


def diag_rad(H_lambda=1/4,i_max=1,r=1):

    #H_lambda = 1/40
    theta  = np.linspace(0.00001,np.pi-0.00001, num=1000)
    theta = np.concatenate((theta,np.linspace(np.pi+0.00001,2*np.pi-0.00001)), axis=None)
    #print(theta)
    z_espacio = 120*np.pi
    #i_max = 1
    KH = 2*np.pi*H_lambda
    #r = 1
    E = (z_espacio*i_max/(2*np.pi*r)) * ((np.cos(KH*np.cos(theta))-np.cos(KH))/np.sin(theta))
    E_abs = np.absolute(E)
    E_abs = E_abs/max(E_abs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="polar")
    ax.plot(theta,E_abs)


    plt.show()


#diag_rad(1/4)
