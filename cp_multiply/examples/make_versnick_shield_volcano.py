#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP

# Shield Volcano by Paula Versnick, Imagiro 77 (2006)

volcano_cell_nodes = {'A': (2, 14), 
                      'B': (4, 12), 
                      'C': (4, 16), 
                      'D': (6, 10), 
                      'E': (8, 12),
                      'F': (8, 16),
                      'G': (10, 6),
                      'H': (11, 5),
                      'I': (12, 6),
                      'J': (12, 8),
                      'K': (12, 12),
                      'L': (12, 16),
                      'M': (13, 3),
                      'N': (13.5, 2.5),
                      'O': (14, 3),
                      'P': (14, 4),
                      'Q': (14, 6),
                      'R': (14, 10),
                      'S': (14.5, 1.5),
                      'T': (15, 1),
                      'U': (15, 2),
                      'V': (15, 3),
                      'W': (15, 5),
                      'X': (16, 1),
                      'Y': (16, 2),
                      'Z': (16, 5),
                      'a': (16, 6),
                      'b': (16, 10),
                      'c': (16, 12),
                      'd': (0, 16),
                      'e': (16, 16)}

m = -180
v = 180
b = 200

volcano_cell_edges = {'AC': m,
                      'BF': v,
                      'DE': v,
                      'EF': v,
                      'EK': m,
                      'EJ': v,
                      'FK': v,
                      'GJ': m,
                      'HI': v,
                      'IJ': v,
                      'IQ': m,
                      'IP': v,
                      'JK': m,
                      'JQ': m,
                      'JR': m,
                      'KL': m,
                      'KR': v,
                      'Kc': m,
                      'MP': m,
                      'NO': v,
                      'OP': v,
                      'OU': v,
                      'OV': m,
                      'PQ': m,
                      'PV': m,
                      'PW': m,
                      'QR': v,
                      'QW': v,
                      'Qa': m,
                      'Rb': v,
                      'SU': v,
                      'TU': m,
                      'TX': m,
                      'TY': v,
                      'UY': v,
                      'VW': v,
                      'VY': m,
                      'WZ': v,
                      'dC': 'B',
                      'CF': 'B',
                      'FL': 'B',
                      'Le': 'B'}


def generate_volcano(use_color = True):
    l1 = ((0, 16), (16, 0))
    l2 = ((0, 0), (16, 0))
    l3 = ((16, 0), (16, 16))

    min_cell = GeneralCP(namednodes = volcano_cell_nodes, 
                         namededges = volcano_cell_edges)
    full_cp = min_cell.add_reflection(l1).add_reflection(l2).add_reflection(l3)
    full_cp.save_cp('versnick_shield_volcano', use_color = use_color)
    
