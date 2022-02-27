#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:38:25 2022

@author: goran
"""

import drawSvg as draw

from cp_multiply.cp_utils import convert_named_to_foldAngles
from cp_multiply.cp_utils import reflect, translate, glide_reflect, merge_two_dicts


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
            elif isinstance(foldAngle, int):
                self.edges_foldAngle[e] = foldAngle
                if edges_foldAngle[e] > 0:
                    self.edges_assignment[e] = 'V'
                elif edges_foldAngle[e] < 0:
                    self.edges_assignment[e] = 'M'
            else:
                assert 1 == 0, 'Bad input: fold angle'+ str(foldAngle) + ' for edge ' + str(e)
        
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

    def merge(self, other):
        return GeneralCP(edges_foldAngle = merge_two_dicts(self.edges_foldAngle, other.edges_foldAngle))

    def add_symmetry_mapped(self, symmetry_type, data):
        return self.merge(self.map_symmetry(symmetry_type, data))

    def add_reflection(self, line):
        return self.add_symmetry_mapped(reflect, line)
    
    def add_translation(self, vector):
        return self.add_symmetry_mapped(translate, vector)
    
    def add_glide_reflection(self, vector_and_line):
        return self.add_symmetry_mapped(glide_reflect, vector_and_line)


    def make_svg_cp(self, 
                    fold_name = 'some_fold',
                    scale = 20,
                    stroke_width = 2,
                    use_color = True):
        maxx = scale * max([n[0] for n in self.nodes])
        minx = scale * min([n[0] for n in self.nodes])
        maxy = scale * max([n[1] for n in self.nodes])
        miny = scale * min([n[1] for n in self.nodes])
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
        

