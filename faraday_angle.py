import matplotlib.pyplot as plt
import math
import numpy as np
from tkinter import *
print("FARADAY'S LAW(CONSTANT ANGLE)")
n=int(input("Enter number of readings:"))
emf_list=[]
time_list=[]
dist_list=[]
a=int(input("Enter the constant angle taken:"))
a2=(a/2)*(math.pi/180)
print()
print("Enter the readings of time below:-")
for i in range(0,n):
    print("Enter",i+1,"th reading of time:")
    t=float(input())
    time_list.append(t)
print()
print("Enter the readings of distance below:-")
for i in range(0,n):
    print("Enter",i+1,"th reading of distance:")
    d=float(input())
    dist_list.append(d)
print()
print("Enter the readings of peak emf below:-")
for i in range(0,n):
    print("Enter",i+1,"th reading of peak emf:")
    e=float(input())
    emf_list.append(e)

print()
vel_list=[]
for i in range(0,n):
    v=((4*math.pi)/time_list[i])*(dist_list[i])*math.sin(a2)
    vel_list.append(v)

win=Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("RESULTS")
Label(win,text="Velocities in order:-",font="Bahnschrift 20 bold").pack()
text=Text(win,width=80,height=15, font="Calibri 15 bold")
text.pack()
for i in vel_list:
    text.insert(END,str(i)+'\n')
win.mainloop()



xpoints = np.array(vel_list)
ypoints = np.array(emf_list)

plt.plot(xpoints, ypoints)
plt.show()

