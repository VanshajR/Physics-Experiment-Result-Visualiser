import math
# import os
from subprocess import call

from tkinter import *
def dist():
    call(["python", "faraday_dist.py"])
def ang():
    call(["python", "faraday_angle.py"])
def farawin():
    f=Tk()
    f.geometry("500x500")
    f.title("Faraday's Law Experiment")
    b1=Button(f,text="Constant Distance",command=dist)
    b1.pack()
    b2=Button(f,text="Constant Angle",command=ang)
    b2.pack()

def malus():
    call(["python", "malus.py"])
def sugar():
    call(["python", "sugar.py"])
def grating():
    call(["python", "grating.py"])

    