#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

import drawSvg as draw

from cp_multiply.cp_utils import mult, convert_named_to_foldAngles, scale_and_shift
from cp_multiply.cp_utils import reflect, translate, glide_reflect, merge_two_dicts
from cp_multiply.cp_utils import rotate



class GeneralCP(object):
    def __init__(self, 
                 namednodes = None, 
                 namededges = None,
                 edges_foldAngle = None):
        '''
        This implements the basic functionality needed to keep track
        of a crease pattern with known edge fold angles. Basic symmetries
        and operations to combine existing patterns are also implemented here.

        When hand-coding the definition of a CP, even in small instances, 
        it is more convenient to name the nodes and use them to define creases,
        and so, if namednodes and namededges are given, 
        a helper function is used to convert to the standard representation in
        edges_foldAngle.
        
        Otherwise, edges_foldAngle must be given.
        '''

        fold_angle_map = {'V': 180, 'M': -180, 'B': 0, 'F': 0, 'U': 0}
        if namednodes and namededges:
            edges_foldAngle = convert_named_to_foldAngles(namednodes, namededges)
        else:
            assert edges_foldAngle, "Specify either namednodes and namededges, or edges_foldAngle"
        self.edges = list(edges_foldAngle.keys())
        self.nodes = [e[0] for e in self.edges] + [e[1] for e in self.edges]
        self.edges_foldAngle = {}
        self.edges_assignment = {}
        for e in self.edges:
            foldAngle = edges_foldAngle[e]
            if isinstance(foldAngle, str):
                self.edges_assignment[e] = foldAngle
                self.edges_foldAngle[e] = fold_angle_map[foldAngle]
            elif isinstance(foldAngle, int) or isinstance(foldAngle, float):
                self.edges_foldAngle[e] = foldAngle
                if edges_foldAngle[e] > 0:
                    self.edges_assignment[e] = 'V'
                elif edges_foldAngle[e] < 0:
                    self.edges_assignment[e] = 'M'
            else:
                assert 1 == 0, 'Bad input: fold angle'+ str(foldAngle) + ' for edge ' + str(e)

        self.maxx = max([n[0] for n in self.nodes])
        self.minx = min([n[0] for n in self.nodes])
        self.maxy = max([n[1] for n in self.nodes])
        self.miny = min([n[1] for n in self.nodes])
        

    def copy(self):
        return GeneralCP(edges_foldAngle = self.edges_foldAngle)
                
    def map_symmetry(self, symmetry_type, data):
        r_nodes = {n: symmetry_type(n, data) for n in self.nodes}
        r_edges = {e: (r_nodes[e[0]], r_nodes[e[1]]) for e in self.edges}
        r_edges_foldAngle = {r_edges[e]: self.edges_foldAngle[e] for e in self.edges}
        mapped = GeneralCP(edges_foldAngle = r_edges_foldAngle)
        return mapped
        
    def reflect(self, line):
        return self.map_symmetry(reflect, line)

    def translate(self, vector):
        return self.map_symmetry(translate, vector)

    def glide_reflect(self, vector_and_line):
        return self.map_symmetry(glide_reflect, vector_and_line)
    
    def scale(self, alpha):
        return self.map_symmetry(mult, alpha)
    
    def scale_and_shift(self, factor_and_vector):
        alpha, vector = factor_and_vector
        #print('In scale_and_shift; factor =', alpha, 'vector =', vector)
        scaled = self.scale(alpha)
        return scaled.translate(vector)

    def rotate(self, center_and_angle):
        return self.map_symmetry(rotate, center_and_angle)

    def merge(self, other):
        return GeneralCP(edges_foldAngle = merge_two_dicts(self.edges_foldAngle, other.edges_foldAngle))

    def map_by_name(self, map_name, data):
        mapping = getattr(self, map_name)
        return mapping(data)

    def add_symmetry_mapped(self, symmetry_type, data):
        return self.merge(self.map_symmetry(symmetry_type, data))

    def add_mapped_by_name(self, map_name, data):
        mapping = getattr(self, map_name)
        return self.merge(mapping(data))

    def add_reflection(self, line):
        return self.add_symmetry_mapped(reflect, line)
    
    def add_translation(self, vector):
        return self.add_symmetry_mapped(translate, vector)
    
    def add_glide_reflection(self, vector_and_line):
        return self.add_symmetry_mapped(glide_reflect, vector_and_line)

    def add_scale_and_shift(self, factor_and_vector):
        return self.add_symmetry_mapped(scale_and_shift, factor_and_vector)
    
    def add_rotation(self, center_and_angle):
        return self.add_symmetry_mapped(rotate, center_and_angle)
    
    def make_grid(self, grid_size = (2, 2), overlap_frac = 0):
        n, m = grid_size

        width = self.maxx - self.minx
        height = self.maxy - self.miny
        x_vec = (width * (1 - overlap_frac), 0)
        y_vec = (0, height * (1 - overlap_frac))

        row = self.copy()
        for i in range(1, n):
            row = row.merge(self.translate(mult(x_vec, i)))
        grid = row.copy()
        for i in range(1, m):
            grid = grid.merge(row.translate(mult(y_vec, i)))
        return grid
    
    def add_edges_from_list(self, the_list):
        for n1, n2, angle in the_list:        
            self.edges.append((n1, n2))
            self.edges_foldAngle[(n1, n2)] = angle
            if angle > 0:
                self.edges_assignment[(n1, n2)] = 'V'
            elif angle < 0:
                self.edges_assignment[(n1, n2)] = 'M'
            else:
                self.edges_assignment[(n1, n2)] = 'F'
                              
    def make_svg_cp(self, 
                    fold_name = 'some_fold',
                    scale = 20,
                    stroke_width = 2,
                    use_color = True):
        maxx = scale * self.maxx
        minx = scale * self.minx
        maxy = scale * self.maxy
        miny = scale * self.miny
        dx = (maxx - minx)
        dy = (maxy - miny)
        d = draw.Drawing(dx, dy, origin = (minx, miny))
        
        print('Drawing the crease pattern')
        print('Scale = ', scale)
        edges = self.edges
        for e in edges:
            n1, n2 = e
            fold_angle = self.edges_foldAngle[e]
            color = 'black'
            opacity = 1
            stroke_dasharray = ""
            if fold_angle > 0:
                if use_color:
                    color = 'blue'
                else:
                    stroke_dasharray = "4 4"
            elif fold_angle < 0:
                if use_color:
                    color = 'red'
                else:
                    stroke_dasharray = ""
            else: # fold_angle == 0
                if use_color:
                    color = 'black'
                else:
                    stroke_dasharray = ""
            if fold_angle != 0:
                opacity = abs(fold_angle / 180)
            n1x, n1y = (e[0][0] * scale, e[0][1] * scale)
            n2x, n2y = (e[1][0] * scale, e[1][1] * scale)
            d.append(draw.Lines(n1x, n1y, n2x, n2y, close = False,
                                stroke = color, stroke_width = stroke_width,
                                stroke_opacity = opacity,
                                stroke_dasharray = stroke_dasharray))
        return d

    def save_cp(self, fold_name = 'some_fold',
                scale = 20,
                stroke_width = 2,
                use_color = True):
        d = self.make_svg_cp(fold_name = fold_name,
                             scale = scale,
                             stroke_width = stroke_width,
                             use_color = use_color)
        filename = fold_name + '.svg'
        d.saveSvg(filename)
            


