"""
Figures out how much it will cost to paint a wall.
Asks user for height, width, cost of paint and how many coats.
"""

# setup
PAINT_AREA = 400

# input
print('How much does a gallon of paint cost?')
cost = float(input())

print('What is your walls width?')
wall_width = float(input())

print('What is your walls height?')
wall_height = float(input())

print('How many coats of paint?')
coats = float(input())
# transform, here is where maths happens. remember order of operations
surface_area = wall_width * wall_height
# print(surface_area)
paint_needed = surface_area / PAINT_AREA
# print(paint_needed)
paint_needed = coats * paint_needed
# formats paint_needed to .00 adds up and slices the remainder off
paint_needed = float('%.0f' % (paint_needed + .5))
# print('Paint needed') + (paint_needed)
total_cost = paint_needed * cost
# used round() to round total cost to x.oo, not needed when using format 
# total_cost = round(total_cost, 2)
# output
print('You will need to purchise ') + str(paint_needed) + ('gallons of paint.')
print('Your total cost to will be, $') + str(float(total_cost))
