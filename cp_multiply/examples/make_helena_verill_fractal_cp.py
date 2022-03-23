#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

# design by Helena Verill, 2021-22
# reference: https://mathamaze.co.uk/origami/fractal

from ..general_cp import GeneralCP
from ..cp_utils import to_degrees, dihedral_angle, normal, translate

from math import sqrt, pi, tan, atan2



cube_nodes = {'A': (0, 0), 
              'B': (1, 0), 
              'C': (2, 0), 
              'D': (0, 1), 
              'E': (1, 1),
              'F': (2, 1),
              'G': (3, 1),
              'H': (4, 1), 
              'I': (1, 2), 
              'J': (3, 2), 
              'K': (0, 3), 
              'L': (4, 3),
              'M': (0, 5),
              'N': (2, 5),
              'O': (4, 5)} 


cube_edges = {#'AB': 0,
              #'BC': 0,
              'AM': 90,
              'BI': -90,
              'CF': 90,
              'DE': 90,
              'EF': -90,
              #'FH': 0,
              'FI': 180, 
              'FJ': 180,
              'GJ': -90,
              'HO': 90,
              'IJ': -90,
              'IK': -180,
              'JL': -180, 
              'KL': 90,
              'KN': -180,
              'LN': -180,
              'MN': 0,
              'NO': 90}

def generate_verill_fractal():

    unit = GeneralCP(namednodes = cube_nodes, 
                     namededges = cube_edges)
    unit.save_cp('verill_fractal_unit')
    
    map_list = [('scale_and_shift', (1, (4, 2))),
                ('scale_and_shift', (0.5, (0, -2.5))),
                ('scale_and_shift', (0.5, (2, -1.5))),
                ('scale_and_shift', (0.5, (4, -0.5))),
                ('scale_and_shift', (0.5, (6, 0.5)))]
    for j in range(8):
        map_list.append( ('scale_and_shift', (0.25, (j, -2.5-1.25 + 0.5 * j))) )
    
    for j in range(16):
        map_list.append( ('scale_and_shift', (0.125, (j/2, -2.5-1.25-0.5*1.25 + 0.25 * j))))
    
    final_cp = unit
    for i in map_list:
        final_cp = final_cp.merge(unit.map_by_name(i[0], i[1]))
    
    add_list = []
    for j in range(64):
        n1 = (j/8 + 0.125, -2.5-1.25-0.5*1.25)
        n2 = (j/8 + 0.125, -2.5-1.25-0.5*1.25 + ((j) // 2) * 0.125 )
        sign = ((j % 2) - 0.5) * 2
        add_list.append( (n1, n2, sign * 180))
        # print('Adding ', n1, n2, sign * 180)     
        add_list.append( (n1, translate(n1, (-0.125, 0)), 0))
    final_cp.add_edges_from_list(add_list)
        
    final_cp.save_cp('verill_fractal_final', scale = 80)
    
    