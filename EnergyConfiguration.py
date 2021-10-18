#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 03:32:15 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

class Point(object):
    def __init__(self, radius, degree):
        # radius >= 0
        self.radius = radius
        # degree must be in radians
        self.degree = degree
        
        self.x = radius * np.cos(degree)
        self.y = radius * np.sin(degree)
    
    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def ComputeEnergy(N, radius, isPointAtCenter):
    work = 0
    points = []
    degree = 0
    
    if N == 1 or N == 0:
        return 0
    
    if isPointAtCenter:
        degreeChange = 2 * np.pi / (N - 1)
    else:
        degreeChange = 2 * np.pi / N
        
    for i in range(N):
        # Insert a new points and establish center for configurations with centers
        if isPointAtCenter and i == 0:
            points += [Point(0, 0)]
        else:
            points += [Point(radius, degree)]
        
        # Update degree for next point
        degree += degreeChange
        
        # For new points sum up distances to other points
        for j in range(len(points) - 1):
            work += (1 / points[i].distance(points[j]))
    
    work *= N / 2
    plotCircle(points, radius, work)
    
    return work

def plotCircle(data, r, energy):
    x, y = [], []
    n = len(data)
    
    if data[0].x == 0:
        label = "N = " + str(n) + " points WITH center: " + str(energy)
    else:
        label = "N = " + str(n) + " points WITHOUT center: " + str(energy)
    
    for i in range(n):
        x += [data[i].x]
        y += [data[i].y]
    
    plt.figure()
    plt.plot(x, y, "r.")
    plt.xlim(left=(-1.1 * r), right=(1.1 * r))
    plt.ylim(bottom=(-1.1 * r), top=(1.1 * r))
    plt.title(label)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

n = int(input("Enter N: "))
r = float(input("Enter radius: "))
print("")

for i in range(1, n+1):
    for j in range(2):
        if j == 0:
            print("N = " + str(i) + " WITHOUT center point: " + str(ComputeEnergy(i, r, False)))
        else:
            print("N = " + str(i) + " WITH center point: " + str(ComputeEnergy(i, r, True)))

