import argparse
import math
from ultiFunc import calculate_inver_units 

parser = argparse.ArgumentParser(description="Input a number to get it's inverticle unit", prog="ProgramName")
parser.add_argument('-u', '--unit', dest='unit', action='store', type=int, nargs='+',help='a list of number for calculating entropy', required=True)
args  = parser.parse_args()
unit = args.unit[0]

print(f'Number of invertible unit found in {unit} is {calculate_inver_units(unit)}')