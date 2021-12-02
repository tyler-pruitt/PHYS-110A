#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:08:01 2020
@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

from objects import Point
from objects import Wire
from objects import Vector

# Here we define the magnetic field
def Mf(currentWire, point):
    """
    Given the current wire and the point, calculates the magnetic field 
    from the current wire at the specified point.
    
    Returns:
        Vector, whose components are the components of the magnetic field
    """
    
    dist = currentWire.distance(point)
    
    rx, ry = point - currentWire
    
    try:
        phi = np.arctan(ry / rx)
    except:
        if rx == 0:
            if ry > 0:
                phi = np.pi / 2
            elif ry < 0:
                phi = - np.pi / 2
    
    
    I = currentWire.current
    
    # Take units to be mu_0 = 1
    mu_0 = 1
    
    Mfx = I * mu_0 * (-np.sin(phi)) / (2 * np.pi * dist)
    
    Mfy = I * mu_0 * (np.cos(phi)) / (2 * np.pi * dist)
    
    if rx < 0:
        Mfx *= -1
        Mfy *= -1
    
    return Vector(point.x, point.y, Mfx, Mfy)

def input_wire():
    while True:
     try:
      curr = float(input("input the current: "))
      xpos = float(input("input the x position: "))
      ypos = float(input("input the y position: "))
      
      return curr, xpos, ypos
     except:
       print("They need to be floats")


while True:
    try:
     n_wires=int(input("input the number of magnetic wires: "))
     
     if n_wires < 1:
        raise
     break
    except:
     print("Needs to be an integer bigger than 0")

startXGrid = float(input("Enter min x (Xmin) value to plot for vector plot: "))
stopXGrid = float(input("Enter max x (Xmax) value to plot for vector plot: "))

startYGrid = float(input("Enter min y (Ymin) value to plot for vector plot: "))
stopYGrid = float(input("Enter max y (Ymax) value to plot for vector plot: "))

Y, X = np.mgrid[startYGrid:stopYGrid:40j,startXGrid:stopXGrid:40j]

testPoints = np.zeros((len(X), len(Y)), dtype=Point)
BField = np.zeros((len(X), len(Y)), dtype=Vector)

for i in range(len(X)):
    for j in range(len(Y)):
        testPoints[i,j] = Point(X[0,i], Y[j,0])
        BField[i,j] = Vector(X[0,i], Y[j,0], 0, 0)


current_wires = []

for i in range(n_wires):
    print("For wire number %d, " % (i+1))
    
    current, x, y = input_wire()
    current_wires += [Wire(x, y, current)]
    
    for j in range(len(X)):
        for k in range(len(Y)):
            BField[j,k] += Mf(current_wires[-1], testPoints[j,k])


U, V = 0 * X, 0 * Y

for i in range(len(X)):
    for j in range(len(Y)):
        U[j,i] += BField[i,j].xComp
        V[j,i] += BField[i,j].yComp

plt.streamplot(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stream Plot of Magnetic Field')
plt.savefig('streamplot.png')
plt.show()

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.3, Y=1.1, U=5,label='Quiver key, length = 3', labelpos='E')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Magnetic field')

for i in range(n_wires):
    if current_wires[i].current > 0:
        color = 'ro'
    else:
        color = 'bx'
    if (current_wires[i].x >= startXGrid and current_wires[i].x <= stopXGrid) and (current_wires[i].y >= startYGrid and current_wires[i].y <= stopYGrid):
        ax.plot(current_wires[i].x, current_wires[i].y, color)

plt.savefig('quiverplot.png')
plt.show()

print('Positive current is represented by a red . and negative current is represented by a blue X.')

