"""
Figures out how much it will cost to paint a wall.
Asks user for height, width, cost of paint and how many coats.
Allows for multiple rooms.
"""

# setup, starting varibles to call the loop
PAINT_AREA = 400
another_wall = 'y'
total_area_of_all_rooms = 0
# input
print('How much does a gallon of paint cost?')
cost = float(input())

# while loop for further input and maths
while another_wall == 'y':
    print('What is your walls width?')
    wall_width = float(input())

    print('What is your walls height?')
    wall_height = float(input())

    print('How many coats of paint?')
    coats = float(input())
# math, calculates surface area that needs to be covered
# & uses total_area as a running tally
    surface_area = wall_width * wall_height
    surface_area_plus_coats = surface_area * coats
    total_area_of_all_rooms = total_area_of_all_rooms + surface_area_plus_coats

    print('Do you have another wall to paint?')
    another_wall = input("y/n ")

# transform, final math figures amount of paint needed
paint_needed = total_area_of_all_rooms / PAINT_AREA
# print('Paint needed') + (paint_needed)
total_cost = paint_needed * cost
# used round() to round total cost to x.oo
total_cost_rounded = round(total_cost, 2)
# output
print('You will need to purchise ' + str(paint_needed) + ' gallons of paint.')
print('Your total cost to will be, $' + str(float(total_cost_rounded)))
