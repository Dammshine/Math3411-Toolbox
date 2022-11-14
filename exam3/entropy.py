import argparse
import math
from ultiFunc import calculate_entropy 

parser = argparse.ArgumentParser(description='Input list of probability for calculation entropy', prog="ProgramName")
parser.add_argument('-p', '--prob', dest='prob', action='append', type=float, nargs='+',help='a list of number for calculating entropy', required=True)
parser.add_argument('-r', '--radix', dest='radix', action='store', type=int, nargs='+',help='radix for the entropy', required=True)

args  = parser.parse_args()
probs = args.prob[0]
radix = args.radix[0]


print(f'Entropy for probability {probs} in radix {radix} is {calculate_entropy(probs, radix)}')

