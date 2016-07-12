"""
Figures out how much it will cost to paint a wall.
Asks user for height, width, cost of paint and how many coats.
Allows for multiple rooms.
"""

# setup, starting variables to call the loop
SQ_FT_PER_GALLON_OF_PAINT = 400
another_wall = 'y'
total_sq_ft_of_all_rooms = 0
# input

print('How much does a gallon of paint cost?')
cost_of_paint = float(input())

# while loop for further input and maths

while another_wall == 'y':
    print('What is your walls width?')
    wall_width = float(input())

    print('What is your walls height?')
    wall_height = float(input())

    print('How many coats of paint?')
    coats_of_paint = float(input())
# math, calculates surface area that needs to be covered
# & uses total_sq_ft_of_all_rooms as a running tally

    sq_ft_of_wall = wall_width * wall_height
    sq_ft_of_wall_times_coats_of_paint = sq_ft_of_wall * coats_of_paint
    total_sq_ft_of_all_rooms = total_sq_ft_of_all_rooms + sq_ft_of_wall_times_coats_of_paint

    print('Do you have another wall to paint?')
    another_wall = input("y/n ")

# transform, final math figures amount of paint needed

gallons_of_paint_needed = total_sq_ft_of_all_rooms / SQ_FT_PER_GALLON_OF_PAINT
total_cost = gallons_of_paint_needed * cost_of_paint
# used round() to round total cost to $X.xx

total_cost_rounded = round(total_cost, 2)
# output

print('You will need to purchise ' + str(gallons_of_paint_needed) + ' gallons of paint.')
print('Your total cost to paint will be, $' + str(total_cost_rounded))
