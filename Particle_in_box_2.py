#Import libraries
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import numpy as np
import warnings
warnings.filterwarnings('ignore')

######################################################################


quantum_number = 500

a = 0.5
l = 50
m = 1
hbar = 1
c=3
L = 10
x0 = L/2
x = np.linspace(0,L,1000).astype(complex).reshape(1000,1)
n = np.arange(1,quantum_number+1).reshape(1,quantum_number)

def gaussan_wave_packet():
    psi0 = (np.exp(-(x-x0)**2 / (2.0 * a**2)) * np.exp(1j * l * x)).reshape(len(x),1)
    return psi0
    
def normalize(psi0):
    A = ( 1/(np.sqrt(np.trapz((np.conj(psi0[:,0])*psi0[:,0]), x[:,0]))))
    psi0_normalized = A*psi0
    return psi0_normalized

def psi_n():
        psi_nx = ( np.sqrt( 2/L ) * np.sin( (n * np.pi * x) /L ) )
        return psi_nx

def energy_eigenvalues():
        En_e = ((np.power(n,2)) * (np.pi**2)*(hbar**2))/(2*m*L**2)
        En_p = (c*(n*np.pi)/L)*hbar
        return En_e,En_p
    
def C_n(psi_nx,psi0_normalized):
    
    Cn = np.zeros((quantum_number,1),dtype=complex)
    for i in range(0,quantum_number):
        Cn[i,0] = np.trapz((np.conj(psi_nx)*psi0_normalized)[:,i], x[:,0])
    Cn = Cn.reshape(1,500)
    return Cn
        
psi0=gaussan_wave_packet()
psi0_normalized = normalize(psi0)
psi_nx = psi_n()
En_e,En_p = energy_eigenvalues()
Cn = C_n(psi_nx,psi0_normalized )


fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(121, xlim = [0,L], ylim = [-1,3])
ax2 = fig.add_subplot(122, xlim = [0,L], ylim = [-1,3])

psi_xt_abs_e, = ax1.plot([], [], c='y',label=r"$\vert \psi \vert^2$")

title1 = ax1.set_title('', fontsize=20)
ax1.legend(prop=dict(size=10), loc='upper center', shadow=True, ncol=3)
ax1.set_xlabel('$x$', fontsize=10)
ax1.set_ylabel(r"$\vert \psi \vert^2$", fontsize=10)
ax1.xaxis.set_tick_params(labelsize=10)
ax1.yaxis.set_tick_params(labelsize=10)

psi_xt_abs_p, = ax2.plot([], [], c='y',label=r"$\vert \psi \vert^2$")
title2 = ax2.set_title('', fontsize=10)
ax2.legend(prop=dict(size=10), loc='upper center', shadow=True, ncol=3)
ax2.set_xlabel('$x$', fontsize=10)
ax2.xaxis.set_tick_params(labelsize=10)
ax2.yaxis.set_tick_params(labelsize=10)
        


def init():
    psi_xt_abs_e.set_data([], [])
    psi_xt_abs_p.set_data([], [])
    title1 = ax1.set_title(r'E= $\frac{n^2\pi^2\hbar^2}{2mL^2}$', fontsize=20)
    title2 = ax2.set_title(r'E= c$\frac{n\pi\hbar}{L}$', fontsize=20)
    return psi_xt_abs_e,psi_xt_abs_p,title1,title2,
def animate(i):

    psi_xt_e = np.zeros((len(x),1),dtype=complex).reshape(len(x),1)
    psi_xt_p = np.zeros((len(x),1),dtype=complex).reshape(len(x),1)
    for k in range(0, quantum_number):
        psi_xt_e[:,0] = psi_xt_e[:,0] + (Cn[0,k] *psi_nx[:,k] * (np.exp((-1j *En_e[0,k] * i*0.002)/hbar)))
        psi_xt_p[:,0] = psi_xt_p[:,0] + (Cn[0,k] *psi_nx[:,k] * (np.exp((-1j *En_p[0,k] * i*0.036)/hbar)))
        psi_xt_abs_e.set_data(x, np.abs(psi_xt_e)**2)
        psi_xt_abs_p.set_data(x, np.abs(psi_xt_p)**2)
        
anim = matplotlib.animation.FuncAnimation(fig, animate,init_func=init, frames=500,interval=1, repeat=False)

plt.show()
