import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    
    Full_cost = meal_cost + meal_cost * (tip_percent/100) + meal_cost * tax_percent/100)
    
    print Full_cost
    return Full_cost

meal_cost = float(raw_input())

tip_percent = int(raw_input())

tax_percent = int(raw_input())
    
solve(meal_cost, tip_percent, tax_percent)
