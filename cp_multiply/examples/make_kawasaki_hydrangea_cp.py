#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP

kawasaki_cell_nodes = {'A': (1,1), 
                       'B': (0,2), 
                       'C': (2,2), 
                       'D': (1,3), 
                       'E': (2,4),
                       'F': (3,5),
                       'G': (1,5),
                       'H': (2,6),
                       'I': (0,6),
                       'J': (0,3),
                       'K': (0,5)}

kawasaki_cell_edges = {'AB': 180, 
                       'BC': -180,
                       'BD': -180,
                       'CD': 180,
                       'CE': -180,
                       'DG': 180,
                       'DJ': 180,
                       'EF': 180,
                       'EG': -180,
                       'EH': -180,
                       'GH': 180,
                       'GK': 180,
                       'HI': -180}


def generate_kawasaki_hydrangea():
    l1 = ((0, 0), (1, 1))
    l2 = ((8, 0), (7, 1))

    min_cell = GeneralCP(namednodes = kawasaki_cell_nodes, 
                         namededges = kawasaki_cell_edges)
    double_cell = min_cell.add_reflection(l1)
    #double_cell.save_cp('kawasaki_1')
    quad_cell = double_cell.add_reflection(l2)
    #quad_cell.save_cp('kawasaki_2')

    v1 = (8, 0)
    v2 = (0, 8)
    mult1 = quad_cell.add_translation(v1)
    mult2 = mult1.add_translation(v2)

    v3 = (16, 0)
    v4 = (0, 16)
    mult3 = mult2.add_translation(v3).add_translation(v4)
    mult3.save_cp('kawasaki_hydrangea_4x4')
    
    v5 = (32, 0)
    v6 = (0, 32)
    mult4 = mult3.add_translation(v5).add_translation(v6)
    mult4.save_cp('kawasaki_hydrangea_8x8')

def generate_kawasaki_nonhydrangea():
    '''This generates a different variation
    by reflecting on axis-aligned lines instead of
    on diagonals    
    '''
    l1 = ((0, 0), (1, 1))
    l2 = ((8, 0), (7, 1))

    min_cell = GeneralCP(namednodes = kawasaki_cell_nodes, 
                         namededges = kawasaki_cell_edges)
    quad_cell = min_cell.add_reflection(l1).add_reflection(l2)

    l3 = ( (8, 0), (8, 1) )
    l4 = ( (0, 8), (1, 8) )
    mult1 = quad_cell.add_reflection(l3).add_reflection(l4)
    
    l5 = ( (16, 0), (16, 1) )
    l6 = ( (0, 16), (1, 16) )
    mult2 = mult1.add_reflection(l5).add_reflection(l6)
    mult2.save_cp('kawasaki_nonhydrangea_4x4')

    l7 = ( (32, 0), (32, 1) )
    l8 = ( (0, 32), (1, 32) )
    mult3 = mult2.add_reflection(l7).add_reflection(l8)
    mult3.save_cp('kawasaki_nonhydrangea_8x8')

