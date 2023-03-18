from cp_multiply.examples.make_box_grid_cp import generate_box_grid
from cp_multiply.examples.make_kawasaki_hydrangea_cp import generate_kawasaki_hydrangea, generate_kawasaki_nonhydrangea
from cp_multiply.examples.make_versnick_shield_volcano import generate_volcano
from cp_multiply.examples.make_box_flower_cp import generate_box_flower_tessellation, generate_box_flower_cp
from cp_multiply.examples.make_box_packing_cp import generate_box_packing
from cp_multiply.examples.make_fourstack_cp import generate_fourstack
#from cp_multiply.examples.make_cube_tessellation_siggy_cp import generate_cube_stairs
from cp_multiply.examples.make_helena_verill_fractal_cp import generate_verill_fractal
from cp_multiply.examples.make_square_hex_cp import generate_square_hex
from cp_multiply.examples.make_hex_rearrangements_cp import generate_hex_rearrangements
from cp_multiply.examples.make_mars_joker import generate_mars_joker_cp

generate_mars_joker_cp(4, 9)

#generate_box_grid()
#generate_kawasaki_hydrangea()
#generate_kawasaki_nonhydrangea()
#generate_volcano(use_color = False)

#generate_box_flower_tessellation((1, 1))
#box_flower = generate_box_flower_cp().make_grid((5, 4))
#box_flower.save_cp('boxflower_tess_5_4')

#generate_box_packing()
#generate_fourstack()
#generate_cube_stairs()

#generate_verill_fractal()
#print('done with fractal')
#generate_square_hex()

#generate_hex_rearrangements()
