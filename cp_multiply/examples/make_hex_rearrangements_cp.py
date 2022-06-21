#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP
from ..cp_utils import to_degrees, dihedral_angle, normal, unit_dir, mult, translate, reflect

from math import sqrt, pi, tan, atan2


nodes_hex_grid = {'A': (-3, 0), 
                  'B': (4, 0), 
                  'D': (3, 0),
                  'E': (3, 1),
                  'F': (1, 3),
                  'G': (4, 1),
                  'H': (6, 1),
                  'I': (2, 3),
                  'J': (-3, 3),
                  'K': (-3, 4),
                  'L': (1, 4),
                  'M': (6, 0),
                  'N': (7, 0),
                  'O': (2, 4),
                  'Q': (4, 3),
                  'R': (5, 3),
                  'S': (4, 4),
                  'T': (7, 1),
                  'U': (5, 4),
                  'W': (-3, 1),
                  'X': (4, 2),
                  'Y': (3, -6),
                  'Z': (-2 + 1/3, 5 + 1/3),
                  'a': (34, -20),
                  'b': (14, -34),
                  'c': (20, 14),
                  'd': (32, -36)}

h1 = unit_dir(-30)
h2 = unit_dir(30)

nodes_cart_grid = {n: translate(mult(h1, p[0]), mult(h2, p[1])) for (n, p) in nodes_hex_grid.items()}

m = -180
v = 180

edges = {'AN': m,
         'BG': m,
         'DE': v,
         'EF': m,
         'EF': m,
         'FL': v,
         'GI': v,
         'HQ': v,
         'IO': m,
         'JR': v,
         'KU': m,
         'MH': m,
         'NT': v,
         'QS': m,
         'RT': m,
         'RU': v,
         'TW': v}

def generate_hex_rearrangements():

    unit = GeneralCP(namednodes = nodes_cart_grid, 
                     namededges = edges)
    unit.save_cp('hex_rearr_unit')
    
    
    rot3c = nodes_cart_grid['Z']
    rot6c = nodes_cart_grid['Y']

    triangle = unit.add_rotation((rot3c, 120)).merge(unit.add_rotation((rot3c, 240)))
    triangle.save_cp('hex_rearr_triangle')

    angle_list = [60, 120, 180, 240, 300]
    hexagon = triangle
    for angle in angle_list:
        hexagon = hexagon.merge(triangle.rotate((rot6c, angle)))
    hexagon.save_cp('hex_rearr_hexagon')

    shift1 = nodes_cart_grid['a']
    shift3 = nodes_cart_grid['b']
    shift5 = nodes_cart_grid['c']
    shift4 = nodes_cart_grid['d']
    shift6 = mult(shift5, 2)
    shift7 = translate(shift4, shift6)

    map2_list = [('translate', shift3),
                 ('translate', shift5),
                 ('translate', shift4),
                 ('translate', shift6)
    ]
    full = hexagon
    for i in map2_list:
        full = full.add_mapped_by_name(i[0], i[1])
    full.save_cp('hex_rearr_full_4by4')
