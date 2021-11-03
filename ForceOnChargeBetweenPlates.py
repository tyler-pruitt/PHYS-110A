#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 03:17:17 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

def Fx(x, a, iterations):
    """
    Calculates the force on the charge q for 
    a given number of iterations for the two inifinite summations
    Note: in unites of q**2 / (16 * np.pi * epsilon_0)
    """
    sum = 0
    
    for i in range(iterations+1):
        sum -= 1 / (a * i + x)**2
    
    for j in range(1, iterations+1):
        sum += 1 / (a * j - x)**2
    
    return sum

aInput = float(input("Enter a: "))
iterationsInput = int(input("Enter the number of iterations: "))

minX = float(input("Enter minimum x: "))
maxX = float(input("Enter maximum x: "))

numPoints = int(input("Enter the number of x values to be tested between these values: "))
xInput = np.linspace(minX, maxX, numPoints)

FxOutput = np.empty((numPoints,), float)

for i in range(len(xInput)):
    FxOutput[i] = Fx(xInput[i], aInput, iterationsInput)

title = "Force on charge q. " + str(iterationsInput) + " iterations. a: " + str(aInput) + "."
plt.figure(1)
plt.plot(xInput, FxOutput, "r.")
plt.xlabel("x")
plt.ylabel("Fx")
plt.title(title)


