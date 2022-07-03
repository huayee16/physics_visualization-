# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 23:38:51 2022

@author: hua_yee
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import warnings
warnings.filterwarnings('ignore')


N=1000
L=1
n=50
M=10
c=3*10**8

x = np.linspace(0,L,N)
t=0.5
def psi(x,t):
    p1=(1/np.sqrt(2*M+1)) * (1/2*1j)* np.sqrt(2/L)
    p2=np.exp((1j*n*(np.pi*(x-c*t)))/L)
    p3=np.sin(((2*M+1)/2) * (np.pi/L) * (x-c*t)) / np.sin((1/2) * (np.pi/L) * (x-c*t))
    p4=np.exp((-1j*n*(np.pi*(x+c*t)))/L)
    p5=np.sin(((2*M+1)/2) * (np.pi/L) * (x+c*t)) / np.sin((1/2) * (np.pi/L) * (x+c*t))
    return p1*p2 * (p2*p3-p4*p5)

fig = plt.figure(figsize=(10,5))
ax1 = plt.subplot(1, 1, 1)
ax1.set_xlim(0, 1)
ax1.set_ylim(-1, 40)
title = ax1.set_title('')
line1, = ax1.plot([], [], "b", label=r"$\vert \psi \vert^2$")
plt.legend(loc=1, fontsize=8, fancybox=False)

def init():
    line1.set_data([],[])
    return line1,


def animate(i):
    line1.set_data(x, np.abs(psi(x,i*10**-10))**2)
    title.set_text('Time = {0:1.3f}'.format(i))
    return line1,


anim = animation.FuncAnimation(fig, animate, init_func=init,frames=10000, interval=200, blit=True)

plt.show()