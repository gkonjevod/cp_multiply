# cp_multiply

Code to help generate tessellation crease patterns.

The input is the data describing the creases in the folded state of a unit cell of the tessellation, and a sequence of operations that generate a translation unit.

The output is an SVG file whose lines encode the creases, with color values defining the crease sense (mountain/valley) and the opacity defining the fold angle in the folded state. Such a file can be imported by Origami Simulator.

Examples are in cp_multiply.examples, and some of them can be run using the top-level run_examples script.
