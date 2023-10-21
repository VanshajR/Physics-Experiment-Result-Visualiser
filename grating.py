import math
from tkinter import *
m=float(input("Enter the number of lines in grating PER INCH: "))
order=["Zero Order","Violet","Indigo","Blue","Green","Yellow/Orange","Red"]
sc1=[]
sc2=[]
print("Enter the readings taken on scale 1:-")
for i in range(0,7):
    print("Enter reading for the ",order[i]," fringe:")
    t1=float(input())
    sc1.append(t1)
print()
print("Enter the readings taken on scale 2:-")
for i in range(0,7):
    print("Enter reading for the ",order[i]," fringe:")
    t2=float(input())
    sc2.append(t2)
print()
sum1=0
sum2=0
a1=[]
a2=[]
for i in range(0,6):
    sum1+=(sc1[i+1]-sc1[0])
    a1.append(sum1)
    sum1=0
    sum2+=(sc2[i+1]-sc2[0])
    a2.append(sum2)
    sum2=0
avg=0
tavg=[]
for i in range(0,6):
    avg=(a1[i]+a2[i])/2
    tavg.append(avg)
lines=m/0.0254
wave=[]
for i in range(1,7):
    ang=(tavg[i-1])*(math.pi/180)
    w=(math.sin(ang))/(lines*i)
    wave.append(w)
win=Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("RESULTS")
Label(win,text="Wavelengths in the order V I B G Y/O R:-",font="Bahnschrift 20 bold").pack()
text=Text(win,width=80,height=15, font="Calibri 15 bold")
text.pack()
for i in wave:
    text.insert(END,str(i)+'\n')
win.mainloop()


