# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:32:42 2022

@author: hua_yee
"""
import numpy as np
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

'''
數據
'''
#ref
h=6.626*10**-34
c=3*10**8
kB=1.38*10**-23
N=1000
#U
class Data:
    
    def __init__(self,lamda,T):
        self.T=T
        self.lamda_pi=lamda
    
    def u(self):
        U=[]
        for lamda in self.lamda_pi:
            e=np.exp((h*c)/(lamda*kB*self.T),dtype=np.longdouble)
            U.append(((8*np.pi*h*c)/lamda**5)*(1/(e-1)))

 
        return np.array([self.lamda_pi,U])
#lambda
def lamda_pi(l):
    lamda=[]
    for i in range(N):
        lamda.append((100+((i/N)*l))*10**-9)
    return lamda


'''
繪圖
'''
#plot
f = Figure(figsize=(4, 4))
a = f.add_subplot(111)
x = 0
y = 0
a.plot(x, y)

def plot(T,l):
    a.clear()
    lamda=lamda_pi(l)
    for t in T:
        data=Data(lamda,t).u()
        x=data[0]
        y=data[1]
        a.plot(x,y,label=t)
    a.set_xlabel("λ(nm)")
    a.set_ylabel("u")
    fmt = lambda x, pos: "{:.0f}".format(x*(10**9), pos)
    a.xaxis.set_major_formatter(plt.ticker.FuncFormatter(fmt))
    fmt2 = lambda y, pos: "{:.1f}".format(y/(10**5), pos)
    a.yaxis.set_major_formatter(plt.ticker.FuncFormatter(fmt2))
    a.legend(title="Temperature(K)",loc="upper right")
    canvas.draw()

'''
#視窗設定
'''
root = tk.Tk()
w=800  #width
r=500  #height
x=500  #與視窗左上x的距離
y=200  #與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))
root.resizable(0, 0)
root.title("Test")
root.configure(bg="white")

#canvas
canvas = FigureCanvasTkAgg(f, master=root)

canvas.draw()

canvas.get_tk_widget().place(x=300,y=0,height=400,width=500)

#input
L=tk.Label(root,text="Temperature(K):",bg="white",fg="black",font=("Times", 18))
L.place(x=90,y=10)
L1=tk.Label(root,text="Input:",fg="black",font=("Times", 12))
L1.place(x=80,y=50,width=50)
E1=tk.Entry(root)
L1_check=tk.Label(root,text="",bg="white",fg="red",font=("Times", 15))
def key_event(event):
    #L1_check.place_forget()
    T=[]
    for ent in all_line:
        try:
            t=float(ent[1].get().strip())
            if t==0:
                #L1_check.configure(text = "check your intput")
                #L1_check.place(x=50,y=10)
                return
            T.append(t)
            #L1_check.configure(text = "T="+str(t))
        except ValueError:
            continue
            #L1_check.configure(text = "check your intput")
            #L1_check.place(x=50,y=10)
    if len(T)>0:
        l=scale_h.get()
        plot(T,l)
E1.bind("<KeyRelease>",key_event)
E1.place(x=130,y=50)


#add new line
all_line=[[L1,E1]]
def add_line():
    line=len(all_line)
    if line >=8:
        return
    L_new=tk.Label(root,text="Input"+str(line+1)+":",fg="black",font=("Times", 12))
    L_new.place(x=80,y=50+(40*line),width=50)
    E_new =tk.Entry(root)
    E_new.bind("<KeyRelease>",key_event)
    E_new.place(x=130,y=50+(40*line))
    all_line.append([L_new,E_new])
button1 = tk.Button(master=root, text="Add", command=add_line)              
button1.place(x=110,y=360)

#sacle
scale_h=tk.Scale(root,from_=500, to=10000,resolution=500,length=250,orient="horizontal",bg="white")
scale_h.set(2500)
scale_h.place(x=430,y=400)
scale_h.bind("<ButtonRelease-1>",key_event)
#Clear    
def remove_line():
    for i in range(1,len(all_line)):
        all_line[i][0].destroy()
        all_line[i][1].destroy()
    del all_line[1:]
    E1.delete(0, tk.END)
    a.clear()
    canvas.draw()
button_rm = tk.Button(master=root, text="Clear", command=remove_line)
button_rm.place(x=160,y=360)    

    

    

    
def _quit():
    root.quit() # 結束主循環
    root.destroy() # 銷燬窗口
button = tk.Button(master=root, text="End", command=_quit)                
button.place(x=220,y=360)

root.mainloop()


