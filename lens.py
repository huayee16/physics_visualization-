import numpy as np
import matplotlib.pyplot as plt
###
n1=1
n2=1.5
d=0
R1=2
R2=-2
###
def lens_getF():

    f=((n2/n1)-1) * (1/R1 - 1/R2 + ((n1-1)*d)/n2*R1*R2)
    return 1/f

def light_yF(x,F,p):
    A=np.array([[p[0],1],[F,1]])
    B=np.array([p[1],0])
    
    a,b=np.linalg.solve(A, B)
    
    return a*x+b

def find_image(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [[x, 0],[x,y]]

plt.figure(figsize=(10,5))
#
origin=[[0,0],[0,5]]
lens=[[5,-8],[5,8]]
#First
plt.quiver(origin[0][0],origin[0][1],origin[1][0]-origin[0][0],origin[1][1]-origin[0][1], angles='xy', scale_units='xy', scale=1)
plt.quiver(lens[0][0],lens[0][1],lens[1][0]-lens[0][0],lens[1][1]-lens[0][1], angles='xy', scale_units='xy', scale=1)
###
F=lens_getF()
plt.scatter(lens[0][0]-F, 0, color='r')
plt.scatter(F+lens[0][0], 0, color='r')
plt.text(lens[0][0]-F, -0.5, 'F1', fontsize=8,verticalalignment='top')
plt.text(F+lens[0][0], -0.5, 'F2', fontsize=8,verticalalignment='top')

###
lightx=np.linspace(0,lens[0][0],10)
lighty1=np.linspace(origin[1][1],origin[1][1],10)
lighty2=light_yF(lightx,lens[0][0],[origin[0][0],origin[1][1]])
lighty3=light_yF(lightx,lens[0][0]-F,[origin[0][0],origin[1][1]])


plt.plot(lightx,lighty1,color='r')
plt.plot(lightx,lighty2,color='g')
plt.plot(lightx,lighty3,color='b')

###
lightxr=np.linspace(lens[0][0],12,10)
lightyr1=light_yF(lightxr,F+lens[0][0],[lightx[-1],lighty1[-1]])
lightyr2=light_yF(lightxr,lens[0][0],[origin[0][0],origin[1][1]])
lightyr3=np.linspace(lighty3[-1],lighty3[-1],10)


plt.plot(lightxr,lightyr1,color='r')
plt.plot(lightxr,lightyr2,color='g')
plt.plot(lightxr,lightyr3,color='b')

img = find_image([[lightxr[0],lightyr1[0]],[lightxr[-1],lightyr1[-1]]], [[lightxr[0],lightyr2[0]],[lightxr[-1],lightyr2[-1]]])
plt.quiver(img[0][0],img[0][1],img[1][0]-img[0][0],img[1][1]-img[0][1], angles='xy', scale_units='xy', scale=1)


textstr = '\n'.join((r'$n1=%.2f$' % (n1, ),r'$n2=%.2f$' % (n2, ),r'$R1=%.2f$' % (R1, ),r'$R2=%.2f$' % (R2, )))
plt.text(8.5, 8, textstr, fontsize=14,verticalalignment='top')
plt.axhline(y=0,lw=1,ls='--',color='black')
plt.xlim(-1, 12)
plt.ylim(-10, 10)
plt.show()

