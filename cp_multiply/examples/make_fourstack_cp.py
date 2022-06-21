#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP
from ..cp_utils import to_degrees, dihedral_angle, normal

from math import sqrt, pi, tan, atan2

t1 = 0.2 # offset for two points

fourstack_nodes = {'A': (0, 0), 
                   'B': (4, 0), 
                   'C': (8, 0), 
                   'D': (2, 2), 
                   'E': (4, 2),
                   'F': (6, 2),
                   'G': (8, 2),
                   'H': (3, 3), 
                   'I': (4, 3), 
                   'J': (4.5+t1, 3.5-t1), 
                   'K': (4.5, 3.5), 
                   'L': (0, 4),
                   'M': (2, 4),
                   'N': (3, 4),
                   'O': (5, 4), 
                   'P': (6, 4), 
                   'Q': (8, 4), 
                   'R': (3.5, 4.5), 
                   'S': (3.5-t1, 4.5+t1),
                   'T': (4, 5),
                   'U': (6, 6),
                   'V': (8, 6), 
                   'W': (4, 6), 
                   'X': (2, 6), 
                   'Y': (0, 8), 
                   'Z': (2, 8),
                   'a': (4, 8),
                   'b': (6, 8),
                   'c': (8, 8),
                   'd': (6, 0),
                   'e': (0, 6)}


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
#print('angle1 = ', angle1)
angle2 = to_degrees(dihedral_angle(normal(folded_wall_coords), 
                                   normal(folded_slanted_coords)))
#print('angle2 = ', angle2)

fourstack_edges = {'AB': 0,
                   'AD': -180, 
                   'AL': 0,
                   'BC': 0,
                   'BE': 0,
                   'CG': 0,
                   'DE': 90,
                   'DH': -180,
                   'DM': -90, 
                   'EF': 90,
                   'EH': 0,
                   'FG': 90,
                   'FI': -180,
                   'FJ': 180,
                   'FO': -180, 
                   'FP': 180,
                   'GQ': 0,
                   'HI': -180,
                   'HM': 180,
                   'HN': -180,
                   'IJ': 180,
                   'IK': -180,
                   'JK': -180, 
                   'JO': 180,
                   'KO': -180,
                   'KR': 180,
                   'LM': 90,
                   'LY': 0,
                   'MX': 90,
                   'NR': -180, 
                   'NS': 180,
                   'NX': -180,
                   'OP': 90,
                   'OT': -90 - angle2,
                   'OU': -90 - angle1,
                   'PQ': -90,
                   'PU': 180,
                   'QV': 0, 
                   'RS': -180,
                   'RT': -180,
                   'ST': 180,
                   'SX': 180,
                   'TU': -90 - angle1,
                   'TW': 90,
                   'TX': -180, 
                   'UV': 90,
                   'UW': 180,
                   'Ub': 90,
                   'Vc': 0,
                   'WX': 180,
                   'Wa': -90,
                   'Xe': 90,
                   'XZ': 90,
                   'YZ': 0,
                   'Za': 0,
                   'ab': 0,
                   'bc': 0,
                   'dF': 90}

def generate_fourstack():

    unit = GeneralCP(namednodes = fourstack_nodes, 
                     namededges = fourstack_edges)
    unit.save_cp('fourstack')


