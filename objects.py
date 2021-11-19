#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:13:49 2021

@author: tylerpruitt
"""

import numpy as np

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.r = np.sqrt(self.x**2 + self.y**2)
        
        if self.x == 0.0:
            self.phi = np.pi / 2
        else:
            self.phi = np.arctan(self.y / self.x)
    
    def __repr__(self):
        return "Point(x = " + str(self.x) + ",y = " + str(self.y) + ")"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def distance(self, other):
        d = np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return d
    
    def xDistance(self, other):
        d = self.x - other.x
        return d
    
    def yDistance(self, other):
        d = self.y - other.y
        return d

class Wire(Point):
    def __init__(self, x, y, current):
        super().__init__(x, y)
        self.current = current
    
    def __repr__(self):
        return "Wire(x = " + str(self.x) + ",y = " + str(self.y) + ",current = " + str(self.current) + ")"

class Vector(Point):
    def __init__(self, x, y, xComp, yComp):
        self.x = x
        self.y = y
        
        self.xComp = xComp
        self.yComp = yComp
        
        self.r = np.sqrt(self.x**2 + self.y**2)
        
        if self.x == 0.0:
            self.phi = np.pi / 2
        else:
            self.phi = np.arctan(self.y / self.x)
        
        self.rComp = np.sqrt(self.xComp**2 + self.yComp**2)
        
        if self.xComp == 0.0:
            self.phiComp = np.pi / 2
        else:
            self.phiComp = np.arctan(self.yComp / self.xComp)
        
    def __repr__(self):
        return "Vector(x = " + str(self.x) + ",y = " + str(self.y) + ",Vx = " + str(self.xComp) + ",Vy = " + str(self.yComp) + ")"
    
    def __add__(self, other):
        return Vector(self.x, self.y, self.xComp + other.xComp, self.yComp + other.yComp)
    
    def __sub__(self, other):
        return Vector(self.x, self.y, self.xComp - other.xComp, self.yComp - other.yComp)


        