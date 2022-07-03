# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:40:14 2022

@author: hua_yee

n1*sin(x) = n2*sin(y)
sin(z) = n2/n1 n1>n2
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# cal
def cal():
    a.clear()
    n1=float(entry_n1.get().strip())
    n2=float(entry_n2.get().strip())
    th1=float(scale_h.get())
    if -1 <= (n1*np.sin(np.deg2rad(th1)))/n2 <= 1:
        th2=np.degrees(np.arcsin((n1*np.sin(np.deg2rad(th1)))/n2))
    else: 
        th2=None
    line=[]
    

    for i in range(0,11):
        line.append(-1*(i*np.tan(np.deg2rad(th1))))
    if th2 != None :
        
        line2=[]
        for i in range(0,-11,-1):
            line2.append(-1*(i*np.tan(np.deg2rad(th2))))
    else:
        line2=[-i for i in line]        
    #plot
    
    a.axhline(y=0,color="black", linewidth=2)
    a.axvline(x=0,color="black", linewidth=0.5,linestyle="dashed")
    a.plot(line,np.arange(0,11))
    if th2 != None :
        a.plot(line2, np.arange(0,-11,-1))
        a.text(-3, -11, 'θ2 = '+str(round(th2, 2)),fontsize=18)
    else:
        a.plot(line2, np.arange(0,11))
    a.set_xlim([-20,20])
    a.set_ylim([-10,10])
    a.text(-3, 11, 'θ1 = '+str(th1),fontsize=18)
    a.axis('off')
    canvas.draw()


#tk
root = tk.Tk()
w=500  #width
r=500  #height
x=500  #與視窗左上x的距離
y=200  #與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))
root.resizable(0, 0)
root.title("Test")
root.configure(bg="white")


#canvas
fig, a = plt.subplots(figsize = (5,4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=-100,y=100,height=400,width=700)


#set n
def key_event(event):
    cal()
    
lable_n1=tk.Label(root,text="n1 = ",bg="white",fg="black",font=("Times", 18))
lable_n1.place(x=0,y=140)
entry_n1=tk.Entry(root,font=("Times", 18),width=5)
entry_n1.place(x=50,y=140)
entry_n1.insert(1, "1")
entry_n1.bind("<KeyRelease>",key_event)
lable_n2=tk.Label(root,text="n2 = ",bg="white",fg="black",font=("Times", 18))
lable_n2.place(x=0,y=305)
entry_n2=tk.Entry(root,font=("Times", 18),width=5)
entry_n2.insert(1, "1.52")
entry_n2.place(x=50,y=305)
entry_n2.bind("<KeyRelease>",key_event)
#set th1
scale_h=tk.Scale(root,from_=90, to=-90,resolution=5,length=500,orient="horizontal",bg="white")
scale_h.set(0.0)
scale_h.place(x=5,y=50)
scale_h.bind("<ButtonRelease-1>",key_event)

cal()
root.mainloop()
