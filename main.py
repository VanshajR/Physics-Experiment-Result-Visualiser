import matplotlib.pyplot as plot
import numpy as np
import math

from tkinter import *
from formulas import *

m=Tk()
m.title("PHYSICS EXPERIMENT CALCULATOR")
m.geometry("1300x500")

label=Label(m,text="SELECT ONE OF THE EXPERIMENTS SHOWN BELOW TO CONTINUE",font="Arial 18 bold")
label.grid(row=0,column=5,padx=10,pady=10,sticky="N")
label.config(bg="#4FB9AF")

btnf=Button(m,text="FARADAY'S LAW",command=farawin,font="Calibri 14 bold")
btnf.grid(row=1,column=5,padx=10,pady=10)
btnf.config(bg="#4FB9AF")
 
btnm=Button(m,text="MALUS LAW",command=malus,font="Calibri 14 bold")
btnm.grid(row=1,column=6,padx=10,pady=10)
btnm.config(bg="#4FB9AF")

btns=Button(m,text="SPECIFIC ROTATION",command=sugar,font="Calibri 14 bold")
btns.grid(row=2,column=5,padx=10,pady=10)
btns.config(bg="#4FB9AF")

btng=Button(m,text="SPECTROMETER GRATING",command=grating,font="Calibri 14 bold")
btng.grid(row=2,column=6,padx=10,pady=10)
btng.config(bg="#4FB9AF")

m.config(bg="#008080",border=10)
m.mainloop()

