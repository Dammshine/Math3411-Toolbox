import argparse
import math
from ultiFunc import find_mod 

parser = argparse.ArgumentParser(description="Input a base, a power and a mod", prog="ProgramName")
parser.add_argument('-b', '--base', dest='base', action='store', type=int, nargs='+',help='base', required=True)
parser.add_argument('-p', '--power', dest='pow', action='store', type=int, nargs='+',help='power', required=True)
parser.add_argument('-m', '--mod', dest='mod', action='store', type=int, nargs='+',help='mod', required=True)
args  = parser.parse_args()
base = args.base[0]
pow = args.pow[0]
mod = args.mod[0]

print(f'Answer to query {base} ^ {pow} mod {mod} = {find_mod(base, pow, mod)}')

