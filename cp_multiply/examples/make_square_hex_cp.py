#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

from ..general_cp import GeneralCP
from ..cp_utils import to_degrees, dihedral_angle, normal, unit_dir, mult, translate, reflect

from math import sqrt, pi, tan, atan2


square_hex_nodes = {'A': (0, 0), 
                    'B': (sqrt(2), 0), 
                    'C': unit_dir(45), 
                    'D': mult(unit_dir(60), 1.03), 
                    'E': translate(mult(unit_dir(120), 1.03), (sqrt(2), 0)),
                    'F': unit_dir(75),
                    'G': translate(unit_dir(105), (sqrt(2), 0)),
                    'H': mult(unit_dir(60), sqrt(2)), 
                    'I': mult(unit_dir(120), 1/(sqrt(2))), 
                    'J': translate(mult(unit_dir(60), 1/sqrt(2)), (sqrt(2), 0))}



square_hex_edges = {#'AB': 0,
                    #'AC': 0, 
                    'AD': 180,
                    'AF': -90,
                    #'AI': 0,
                    'BC': -180,
                    'BE': 180,
                    'BG': -90,
                    #'BJ': 0, 
                    'CD': -90,
                    'CE': -30,
                    'CH': -60,
                    'DH': 180,
                    'EG': -60,
                    'EH': 180, 
                    'FH': -90,
                    #'FI': 0,
                    'GH': -90,
                    #'GJ': 0}
                    }

def generate_square_hex():

    unit = GeneralCP(namednodes = square_hex_nodes, 
                     namededges = square_hex_edges)
    
    center = square_hex_nodes['H']
    angle = 120
    two = unit.add_rotation((center, angle))
    full_circle = two.merge(unit.add_rotation((center, 2*angle)))
    shift1 = translate(square_hex_nodes['B'], (mult(unit_dir(60), sqrt(2))))
    shift2 = mult(unit_dir(90), sqrt(3)*sqrt(2))
    shift3 = mult(unit_dir(0), sqrt(2) * 3)
    two_c = full_circle.add_translation(shift1)
    four_c = two_c.add_translation(shift2)
    eight_c = four_c.add_translation(shift3)
    #eight_c.save_cp('square_hex_8', scale = 80)
    sixteen_c = eight_c.add_translation( mult(unit_dir(90), 2* sqrt(3) * sqrt(2)))
    #sixteen_c.save_cp('square_hex_16', scale = 80)
    thirtytwo_c = sixteen_c.add_translation( mult(unit_dir(0), 6 * sqrt(2)))
    sixtyfour_c = thirtytwo_c.add_translation( mult(unit_dir(90), 4 * sqrt(3) * sqrt(2)))
    #sixtyfour_c.save_cp('square_hex_64', scale = 80)
    one28_c = sixtyfour_c.add_translation( mult(unit_dir(0), 12 * sqrt(2)))
    two56_c = one28_c.add_translation( mult(unit_dir(90), 8 * sqrt(3) * sqrt(2)))
    two56_c.save_cp('square_hex_256', scale = 160)
