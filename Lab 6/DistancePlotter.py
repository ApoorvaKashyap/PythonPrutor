### DO NOT CHANGE. REQUIRED TO PLOT IN PRUTOR #################################
import math
#import prutorplotlib as pl
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
###############################################################################

g = 9.8

# YOUR CODE GOES HERE ********************************************************
vel = float(input())
rad = math.radians(float(input())) 

t = round(2 * vel * math.sin(rad) / g, 2)
h = round((vel ** 2) * (math.sin(rad) ** 2) / (2 * g), 2)
r = round((vel **2) * math.sin(2 * rad) / g, 2)

print("Time of Flight = {}\nDistance Covered = {}\nPeak Height = {}".format(t,r,h))

#Plotting the Graph
rvals = np.linspace(0, r, 100)
hvals = (rvals * math.tan(rad)) - ((0.5 * g * (rvals ** 2)) / ((vel ** 2) * (math.cos(rad) ** 2)))
plt.ylabel('Vertical Height(m)')
plt.xlabel('Horizontal Distance(m)')
plt.plot(rvals, hvals)
plt.show()

### DO NOT CHANGE. REQUIRED TO PLOT IN PRUTOR #################################
#pl.prutorsaveplot(plt, 'plot1.pdf')
###############################################################################