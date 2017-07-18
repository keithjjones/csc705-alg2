import argparse
import time
import random
import math


def gcd(number1, number2):
    if number1 >= number2:
        a = number1
        b = number2
    else:
        b = number1
        a = number2

    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

# Main functionality starts here...

# Argument parsing
parser = argparse.ArgumentParser(description='RC4 encryption/decryption.')
parser.add_argument('Number1',
                    help='The first number.',
                    type=int)
parser.add_argument('Number2',
                    help='The second number.',
                    type=int)
parser.add_argument("-a", "--average",
                    help="The number of runs for averaging, greater than zero."
                         "", default=1, type=int, required=False)
parser.add_argument("-v", "--verbose",
                    help="Turn on output of more data."
                         "", action='store_true', required=False)

args = parser.parse_args()

# Create running time counter...
totaltimespan = 0

number1 = args.Number1
bits1 = math.log2(number1)
number2 = args.Number2
bits2 = math.log2(number2)

if args.verbose:
    print("Random Numbers: \n\t{0:,}\n\t\t{2} bits\n\t{1:,}\n\t\t{3} bits".format(number1, number2, bits1, bits2))

# Gather time data for averages
for a in range(0, args.average):
    starttime = time.process_time()

    g = gcd(number1, number2)

    endtime = time.process_time()
    totaltime = endtime - starttime
    totaltimespan += totaltime

print("Average running time for {0:,} iterations: {1:.4E}".format(args.average, totaltimespan/args.average))
print(g)