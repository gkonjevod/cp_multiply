#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:30:20 2023

@author: goran
"""

from itertools import chain   
 
from ..cp_lines import Pre_CP, Point, Step_Sequence


def generate_mars_joker_cp(min_step, n_steps):
    max_step = min_step + n_steps - 1
    steps_x = list(range(min_step, max_step + 1))
    steps_x.extend(list(range(max_step, min_step, -1)))
    steps_y = list(range(max_step, min_step, -1))
    steps_y.extend(list(range(min_step, max_step + 1)))
    zeros = [0] * len(steps_x)
    alt_x = list(chain(*zip(steps_x, zeros)))
    alt_y = list(chain(*zip(zeros, steps_y)))
    
    
    steps = [Point(*xy) for xy in zip(alt_x[1:], alt_y[1:])]
    start_node = Point(0,0)
    axis1 = 30
    axis2 = -30
    l1 = Pre_CP(step_sequence = Step_Sequence(start_node = start_node,
                                              axis1 = axis1,
                                              axis2 = axis2,
                                              steps = steps))

    l2 = l1.rotate(( (0, 0), -90))
    all_nodes = []
    all_edges = []
    e_a = []
    for i, n in enumerate(l1.nodes):
        l_v = l2.translate(n)
        all_nodes.extend(l_v.nodes)
        print(len(all_nodes))
        all_edges.extend(l_v.edges)
        if i == 0 or i == len(l1.nodes) - 1:
            e_a.extend([0] * (len(l2.nodes)-1))
        elif i % 2 == 1:
            e_a.extend([180] * (len(l2.nodes)-1))
        else:
            e_a.extend([-180] * (len(l2.nodes)-1))
    for i, n in enumerate(l2.nodes):
        l_h = l1.translate(n)
        all_nodes.extend(l_h.nodes)
        all_edges.extend(l_h.edges)
        if i == 0 or i == len(l2.nodes) - 1:
            e_a.extend([0] * (len(l1.nodes)-1))
        elif i % 2 == 0:
            ext = [-180, 180] * len(l2.nodes)
            e_a.extend(ext[:len(l2.nodes)-1])
        else:
            ext = [180, -180] * len(l2.nodes)
            e_a.extend(ext[:len(l2.nodes)-1])
    all_nodes = set(all_nodes)
    p = Pre_CP(nodes = all_nodes, edges = all_edges, edge_assignments = e_a)
    p.save_cp(fold_name = 'mars_joker_'+str(min_step)+'_'+str(n_steps), scale = 10)



    