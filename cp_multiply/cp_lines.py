#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:30:20 2023

@author: goran
"""

from collections import namedtuple
from dataclasses import dataclass
import drawsvg as draw

from cp_multiply.cp_utils import unit_dir, mult
from cp_multiply.cp_utils import translate, rotate


Point = namedtuple('Point', ['x', 'y'])
Step = namedtuple('Step', ['x', 'y'])

@dataclass
class Step_Sequence(object):
    start_node: Point
    axis1: float # angle of first axis
    axis2: float # angle of second axis
    steps: list[Step]

class Pre_CP(object):
# this should be related to GeneralCP,
# but that one probably needs some overhaul,
# so I'll keep this simple for now
    def __init__(self,
                 nodes = None,
                 edges = None,
                 step_sequence = None,
                 edge_assignments = None):
        if step_sequence:
            if nodes or edges:
                print('Step sequence given; overwriting nodes and edges')
            self.edges = []
            node0 = step_sequence.start_node
            self.nodes = [(node0.x, node0.y)]
            print('Start node:', self.nodes[0])

            for step in step_sequence.steps:
                lastnode = self.nodes[-1]
                print('Adding another step:', step)
                step_in_xy = translate(mult(unit_dir(step_sequence.axis1), step.x),
                                       mult(unit_dir(step_sequence.axis2), step.y))
                print('  the step in (x, y) is ', step_in_xy)
                newnode = translate(lastnode, step_in_xy)
                print('  and the next node is ', newnode)
                self.nodes.append(newnode)
                self.edges.append((lastnode, newnode))
        else:
            self.nodes = nodes.copy()
            self.edges = edges.copy()
            
        if edge_assignments:
            self.edge_assignments = edge_assignments
            self.edges_assigned = True
        else:
            self.edges_assigned = False
            
        self.maxx = max([n[0] for n in self.nodes])
        self.minx = min([n[0] for n in self.nodes])
        self.maxy = max([n[1] for n in self.nodes])
        self.miny = min([n[1] for n in self.nodes])
        
    
    def copy(self):
        return Pre_CP(nodes = self.nodes, edges = self.edges)
    
    def map_symmetry(self, symmetry_type, data):
        r_nodes = [symmetry_type(n, data) for n in self.nodes]
        r_edges = [(symmetry_type(e[0], data), 
                    symmetry_type(e[1], data)) for e in self.edges]
        return Pre_CP(nodes = r_nodes, edges = r_edges)
    
    def rotate(self, center_and_angle):
        return self.map_symmetry(rotate, center_and_angle)
    
    def translate(self, vector):
        return self.map_symmetry(translate, vector)
    
    def merge(self, other):
        return Pre_CP(nodes = list(set(self.nodes + other.nodes)),
                      edges = list(set(self.edges + other.edges)))
        
    def add_symmetry_mapped(self, symmetry_type, data):
        return self.merge(self.map_symmetry(symmetry_type, data))
        
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
        for i, e in enumerate(edges):
            n1, n2 = e
            if self.edges_assigned:
                fold_angle = self.edge_assignments[i]
            else:
                fold_angle = 0 #self.edges_foldAngle[e]
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
        d.save_svg(filename)
    


    