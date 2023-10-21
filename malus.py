import math
import matplotlib.pyplot as plt
import numpy as np
print("***************************MALUS LAW***************************")
n=int(input("Enter the number of readings:"))
clist=[]
alist=[]
coslist=[]
for i in range(0,n):
    print("Enter the",i+1,"th reading of current(CURRENT IS THE INTENSITY):")
    c=float(input())
    clist.append(c)
print()

for i in range(0,n):
    print("Enter the",i+1,"th reading of angle:")
    t=int(input())
    alist.append(t)
print()

for i in alist:
    a=(i/2)*(math.pi/180)
    cos=(math.cos(a))**2
    coslist.append(cos)

xpoints = np.array(coslist)
ypoints = np.array(clist)

plt.plot(xpoints, ypoints)
plt.show()

