"""Convert an amount in gallons to liters"""

# 1. setup
LPG = 3.785

# 2. input
print('How many gallons?')
gallons = float(input())

# 3. transform
liters = gallons * LPG

# 4. output
print(liters)
