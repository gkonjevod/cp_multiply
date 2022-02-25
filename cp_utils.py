#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

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
    
    x2 = round(a * (px - x1) + b * (py - y1) + x1)
    y2 = round(b * (px - x1) - a * (py - y1) + y1)

    return (x2, y2)

def translate(p, vector):
    dx, dy = vector
    px, py = p
    return (px+dx, py+dy)

def glide_reflect(p, vector_and_line):
    vector, line = vector_and_line
    return reflect(translace(p, vector), line)
               
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

