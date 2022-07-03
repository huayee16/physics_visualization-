# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:38:06 2022

@author: hua_yee
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
###
class ABCD:
    def __init__(self, _type,f,n1,n2,d,R1,R2,t):
        self._type=_type
        self.f=f
        self.n1=n1
        self.n2=n2
        self.d=d
        self.R1=R1
        self.R2=R2
        self.t=t
            
    def space(self):
        self.s=np.array([[1,self.d],[0,1]])
    def lens_t(self):
        if self.f:
            self.len_t=np.array([[1,0],[-1/self.f,1]])
        else:
            F=((self.n2/self.n1)-1) * (1/self.R1 - 1/self.R2)
            self.len_t=np.array([[1,0],[-F,1]])
        
    def lens_w(self):
        if self.f:
            self.len_t=np.array([[1,0],[-1/self.f,1]])
        else:
            A=np.array([[1,0],[(self.n2-self.n1)/(self.R2*self.n1),self.n2/self.n1]])
            B=np.array([[1,self.t],[0,1]])
            C=np.array([[1,0],[(self.n1-self.n2)/(self.R1*self.n2),self.n1/self.n2]])
            self.len_w=A.dot(B).dot(C)
    def Mirro(self):
        self.M=np.array([[1,0],[0,1]])
    def Mirro_R(self):
        self.M=np.array([[1,0],[-2/self.R1,1]])
    def flat(self):
        self.F=np.array([[1,0],[0,self.n1/self.n2]])
    def flat_R(self):
        self.F_R=np.array([[1,0],[(self.n1-self.n2)/(self.R1*self.n2),self.n1/self.n2]])
    def get_d(self):
        return self.d
    def get_t(self):
        return self.t
    def get_type(self):
        return self._type      
    def get_matrix(self):
        if self._type=='S':
            self.space()
            return self.s
        elif self._type=='L_t':
            self.lens_t()
            return self.len_t
        elif self._type=='L_w':
            self.lens_w()
            return self.len_w
        elif self._type=='M':
            self.Mirro()
            return self.M
        elif self._type=='M_R':
            self.Mirro_R()
            return self.M_R
        elif self._type=='F':
            self.flat()
            return self.F
        elif self._type=='F_R':
            self.flat_R()
            return self.F_R
####################################
R1=ABCD('L_t',-1.5,None,None,2,None,None,None)
R2=ABCD('L_w',None,1,1.5,2,1.5,-2,1)
R3=ABCD('L_t',2,None,None,2,None,None,None)
S1=ABCD('S',None,None,None,2,None,None,None)
FR=ABCD('F_R',None,1,1.3,2,-1.7,None,None)
l1=np.array([[3],[0]])
l2=np.array([[0],[0]])
l3=np.array([[-3],[0]])

M = [R1,R2]
L=[l1,l2,l3]

pic=[[] for _ in range(len(M))]
####################################

def get_y(x,p,t):
    #b=y-ax
    b=p[1]-p[0]*t
    return t*x+b
def pic_get(pic,p):
    if len(pic) == 0:
        pic=p
    else:
        if pic[0]!=p[0]:
            return
        else:
            pic[1]+=p[1]
            pic[2]=p[2]
    return pic
        
    
            
def light_pic(l,M):
    if len(M)==0:
        return l
    else:
        for i in range(len(M)):
            if i == 0 :
                x0=0
                xt=M[i].get_d()
                x=np.linspace(x0,xt,10)
                y=get_y(x,[x[0],l[0][0]],l[1])
                xf,yf=x[-1],y[-1]
                plt.plot(x,y)
                l_b=M[i].get_matrix().dot(l)
 
            else:
                x0=xt
                xt+=M[i].get_d()
                
                if M[i-1].get_t():
                    
                    x=np.linspace(x0+M[i-1].get_t(),xt,10)
                    y=get_y(x,[xf,yf],l_b[1][0])
                    xf,yf=x[-1],y[-1]
                    
                    pic[i-1] = pic_get(pic[i-1],[x[0],y[0],M[i-1].get_t()])

                else:
                    x=np.linspace(x0,xt,10)
                    y=get_y(x,[xf,yf],l_b[1][0])
                    xf,yf=x[-1],y[-1]
                    
                    pic[i-1] = pic_get(pic[i-1],[x[0],y[0],0])
                    
                plt.plot(x,y)
                    
                l_b=M[i].get_matrix().dot(l_b)

        if M[-1].get_t():
            x=np.linspace(xt+M[-1].get_t(),xt+5,10)
            y=get_y(x,[xf,yf],l_b[1][0])
            pic[-1] = pic_get(pic[-1],[x[0],y[0],M[-1].get_t()])
        else:
            x=np.linspace(xt,xt+5,10)
            y=get_y(x,[xf,yf],l_b[1][0])
            pic[-1] = pic_get(pic[-1],[x[0],y[0],0])
        plt.plot(x,y)
        
for l in L:
    light_pic(l,M)

for i in range(len(pic)):
    
    x,y,w=pic[i]

    if M[i].get_type() == 'F_R' or M[i].get_type() == 'F':
        circle = matplotlib.patches.Arc((x-(w/2),y), w, 10*len(L) ,angle=0, ls = '--', color= 'b' ,linewidth=0.5, fill=False, zorder=2)
    elif M[i].get_type() == 'S':
        circle = matplotlib.patches.Arc((x-(w/2),y), w, 10*len(L) ,angle=0, color= 'w' ,linewidth=0.1, fill=False, zorder=2) 
    elif M[i].get_type() == 'L_t':
        circle = matplotlib.patches.Arc((x-(w/2),y), w+0.1, 10*len(L) ,angle=0,linewidth=0.9, fill=False, zorder=2) 
    else:
        circle = matplotlib.patches.Arc((x-(w/2),y), w, 10*len(L) ,angle=0 ,linewidth=1, fill=False, zorder=2)
    plt.gca().add_patch(circle)

plt.xlim(-1, )
plt.ylim(-25, 25)
plt.axhline(y=0,lw=1,ls='--',color='black')
plt.show()        


    