#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from math import pi, sin, cos

def mult(vec, a):
    #print('In mult, a =', a, 'vec =', vec)
    return tuple(a * x for x in vec)

def reflect(p, line):
    q1, q2 = line
    x1, y1 = q1
    x2, y2 = q2
    px, py = p
    
    dx = x2 - x1
    dy = y2 - y1
    
    xsq = dx * dx
    ysq = dy * dy
    
    distsq = xsq + ysq
    a = (xsq - ysq) / distsq
    b = 2*dx*dy / distsq
    
    #x2 = round(a * (px - x1) + b * (py - y1) + x1)
    #y2 = round(b * (px - x1) - a * (py - y1) + y1)
    x2 = a * (px - x1) + b * (py - y1) + x1
    y2 = b * (px - x1) - a * (py - y1) + y1
    
    return (x2, y2)

def translate(p, vector):
    dx, dy = vector
    px, py = p
    return (px+dx, py+dy)

def glide_reflect(p, vector_and_line):
    vector, line = vector_and_line
    return reflect(translate(p, vector), line)

def scale_and_shift(p, factor_and_vector):
    factor, vector = factor_and_vector
    return translate(mult(p, factor), vector)
               
def convert_named_to_foldAngles(namednodes, namededges):
    edges_foldAngle = {}
    for e_str in namededges:
        n1 = e_str[0]
        n2 = e_str[1]
        edges_foldAngle[(namednodes[n1], namednodes[n2])] = namededges[e_str]
    return edges_foldAngle

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

def point_angle_to_line(p, deg):
    angle = deg * pi / 180
    return (p, translate(p, (cos(angle), sin(angle))))

def to_degrees(angle):
    return 180*angle/pi

# from fold_geometry

from math import atan2, sqrt
import numpy as np

def scale(v, ll):
    return tuple(ll*x for x in v)

def length(v):
    return sqrt(dot(v, v))

def vdir(p1, p2):
    return tuple(x2 - x1 for x1, x2 in zip(p1, p2))

def dot(v1, v2):
    return sum(x1 * x2 for x1, x2 in zip(v1, v2))

def unit(v, eps = 1e-6):
    #TODO: this is clearly not safe
    return scale(v, 1.0/length(v))

def normal(f):
    return unit(cross(vdir(f[0], f[1]), vdir(f[1], f[2])))

def cross(v1, v2):
    return np.array((v1[1]*v2[2] - v1[2]*v2[1], 
                     v1[2]*v2[0] - v1[0]*v2[2],
                     v1[0]*v2[1] - v1[1]*v2[0]))

def dihedral_angle(n1, n2):
    crease = cross(n1, n2)
    return atan2(dot(cross(crease, n1), n2), dot(n1, n2))




    
    
    
    
    
    
