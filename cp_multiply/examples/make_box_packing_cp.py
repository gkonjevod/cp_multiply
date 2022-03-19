#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP
from ..cp_utils import to_degrees, dihedral_angle, normal

from math import sqrt, pi, tan, atan2

# calculate the non-integer coordinate
twentytwoandhalf = 22.5 * pi / 180
CD = 2*sqrt(2) * tan (twentytwoandhalf)
C_x = 4 - CD / sqrt(2)

box_packing_cell_nodes = {'A': (2, 0), 
                       'B': (4, 0), 
                       'C': (2, 2), 
                       'D': (4, 2), 
                       'E': (4, 3),
                       'F': (3.5, 3.5),
                       'G': (0, 0)}


angle1 = to_degrees(atan2(sqrt(2)/2, 2))
folded_wall_coords = [ (2, 2, 0),
                       (2, 1, 2), 
                       (2, 2, 2)]
folded_top_coords = [ (2, 1, 2),
                      (2, 2, 2),
                      (1, 2, 2)]

folded_slanted_coords = [(1, 2, 2),
                         (2, 2, 0),
                         (2, 1, 2)]

angle1_check = to_degrees(dihedral_angle(normal(folded_top_coords), 
                                         normal(folded_slanted_coords)))
print('angle1 = ', angle1)
angle2 = to_degrees(dihedral_angle(normal(folded_wall_coords), 
                                   normal(folded_slanted_coords)))
print('angle2 = ', angle2)

box_packing_cell_edges = {'AC': -90, 
                          'BD': 180,
                          'CD': -180,
                          'CE': 90 + angle1,
                          'DE': -180,
                          'EF': 90 + angle2,
                          'BG': 0}

def generate_box_packing():
    l1 = ((0, 0), (2, 2))
    l2 = ((4, 0), (4, 1))
    l3 = ((0, 4), (1, 4))
    #l4 = ((0, 8), (1, 8))

    min_cell = GeneralCP(namednodes = box_packing_cell_nodes, 
                         namededges = box_packing_cell_edges)
    #min_cell.save_cp('test0')
    c1 = min_cell.add_reflection(l1).add_reflection(l2).add_reflection(l3)#.add_reflection(l4)
    c1.save_cp('box_packing_cell')

    grid = c1.make_grid(grid_size = (5, 5), overlap_frac = 0.25)
    grid.save_cp('box_packing_5x5')

    # l5 = ((16, 0), (16, 1))
    # l6 = ((0, 16), (1, 16))
    # c2 = c1.add_reflection(l5).add_reflection(l6)
    # c2.save_cp('box_grid_cell_2x2')
    
    # l7 = ((32, 0), (32, 1))
    # l8 = ((0, 32), (1, 32))
    # c3 = c2.add_reflection(l7).add_reflection(l8)
    # c3.save_cp('box_grid_cell_4x4')

    # l9 = ((64, 0), (64, 1))
    # l10 = ((0, 64), (1, 64))
    # c4 = c3.add_reflection(l9).add_reflection(l10)
    # c4.save_cp('box_grid_cell_8x8')

    # l11 = ((128, 0), (128, 1))
    # l12 = ((0, 128), (1, 128))
    # c5 = c4.add_reflection(l11).add_reflection(l12)
    # c5.save_cp('box_grid_cell_16x16')

