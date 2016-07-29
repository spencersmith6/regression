import matplotlib.pylab as plt
import numpy as np
from minimize import *

def heatmap(X,Y,f, trace):
    b1 = np.arange(-60, -14, 1)
    b2 = np.arange(5, 26, 1)
    map = np.zeros((len(b1), len(b2)))
    for x in range(len(b1)):
        for y in range(len(b2)):
            map[x,y]= f([b1[x],b2[y]])

    plt.imshow(map, origin='lower', extent=[min(b1), max(b1), min(b2), max(b2)], vmax=abs(map).max(), vmin=-abs(map).max())
    tracex=[]
    tracey=[]
    for i in range(len(trace)):
        addx = trace[i][0]
        addy = trace[i][1]
        tracex = np.append(tracex, addx)
        tracey = np.append(tracey, addy)
    plt.plot(tracex, tracey, 'ko', markersize = 1)



## TESTING ##


test = [-45, 7]
test2 = [ -19, 20]

Bfin, steps, trace = minimum(Cost, test, 50, .00001, .000000000001)
Bfin2, steps2, trace2 = minimum(Cost, test2, 50, .00001, .000000000001)

print Bfin, Bfin2

heatmap(HOURLY_WAGE, MURDERS, Cost, trace)
heatmap(HOURLY_WAGE, MURDERS, Cost, trace2)

plt.text(-59,23,"Steps= %1.0f" %steps)
plt.text(test[0]+1, test[1]+1, "Start (Run one)")
plt.text(Bfin[0]+1, Bfin[1]+1, "Stop [$%1.3f,\\ %1.3f$]" %(Bfin[0], Bfin[1]))
plt.plot(test[0], test[1], "go")
plt.plot(Bfin[0], Bfin[1], "ro")

plt.text(-59,21,"Steps (Run Two)= %1.0f" %steps2)
plt.text(test2[0]+1, test2[1]+1, "Start (Run Two)")
plt.text(Bfin2[0]+1, Bfin2[1]+3, "Run Two [$%1.3f,\\ %1.3f$]" %(Bfin2[0], Bfin2[1]))
plt.plot(test2[0], test2[1], "go")
plt.plot(Bfin2[0], Bfin2[1], "ro")

plt.show()