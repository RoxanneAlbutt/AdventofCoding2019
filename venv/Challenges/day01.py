# --- Day 1: The Tyranny of the Rocket Equation ---
# 28 Feb 2021

import fileinput
import math
import sys
from pathlib import Path

inputfilename = Path(__file__).stem + "_input.txt"

def calc_fuel(mass):
    total_fuel = 0

    while True:
        fuel = math.floor(mass/3) - 2

        if fuel <= 0:
            break

        total_fuel += fuel
        mass = fuel
    return total_fuel

def sum_fuel(input):
    return(sum(calc_fuel(int(line)) for line in input))

print(sum_fuel(fileinput.input(inputfilename)))

