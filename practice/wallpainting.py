"""
Figures out how much it will cost to paint a wall.
Asks user for height, width and cost of paint.
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
total_cost = paint_needed * cost
# used round() to round total cost to nearest x.oo 
total_cost = round(total_cost, 2)
# output, issues with remainders and decimals look up "maths." functions
print('Your total cost to paint will be, $') + str(float(total_cost))
