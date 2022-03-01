#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP

from math import sqrt, pi, tan

# calculate the non-integer coordinate
twentytwoandhalf = 22.5 * pi / 180
CD = 2*sqrt(2) * tan (twentytwoandhalf)
C_x = 4 - CD / sqrt(2)

box_grid_cell_nodes = {'A': (0,2), 
                       'B': (2,2), 
                       'C': (C_x,C_x), 
                       'D': (4,4), 
                       'E': (2,6),
                       'F': (0,6)}

box_grid_cell_edges = {'AB': 90, 
                       'BC': -180,
                       'BE': 135,
                       'CD': 180,
                       'CE': -180,
                       'EF': -90}

def generate_box_grid():
    l1 = ((0, 8), (1, 7))
    l2 = ((0, 0), (1, 1))
    l3 = ((8, 0), (8, 1))
    l4 = ((0, 8), (1, 8))

    min_cell = GeneralCP(namednodes = box_grid_cell_nodes, 
                         namededges = box_grid_cell_edges)
    #min_cell.save_cp('test0')
    c1 = min_cell.add_reflection(l1).add_reflection(l2).add_reflection(l3).add_reflection(l4)
    c1.save_cp('box_grid_cell')

    l5 = ((16, 0), (16, 1))
    l6 = ((0, 16), (1, 16))
    c2 = c1.add_reflection(l5).add_reflection(l6)
    c2.save_cp('box_grid_cell_2x2')
    
    l7 = ((32, 0), (32, 1))
    l8 = ((0, 32), (1, 32))
    c3 = c2.add_reflection(l7).add_reflection(l8)
    c3.save_cp('box_grid_cell_4x4')

    l9 = ((64, 0), (64, 1))
    l10 = ((0, 64), (1, 64))
    c4 = c3.add_reflection(l9).add_reflection(l10)
    c4.save_cp('box_grid_cell_8x8')

    l11 = ((128, 0), (128, 1))
    l12 = ((0, 128), (1, 128))
    c5 = c4.add_reflection(l11).add_reflection(l12)
    c5.save_cp('box_grid_cell_16x16')

