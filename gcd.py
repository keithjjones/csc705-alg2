import argparse
import time
import random
import math

def gcd(number1, number2):
    q = []
    r = []
    i = 0
    a = number1
    b = number2

    while True:
        q.append(a // b)
        r.append(a % b)
        a = b
        b = r[i]
        if r[i] == 0:
            return r[i-1]
        i += 1

# Main functionality starts here...

# Argument parsing
parser = argparse.ArgumentParser(description='RC4 encryption/decryption.')
parser.add_argument('Bits1',
                    help='The number of bits to generate in the first random number.',
                    type=int)
parser.add_argument('Bits2',
                    help='The number of bits to generate in the second random number.',
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

number1 = random.getrandbits(args.Bits1)
bits1 = math.log2(number1)
number2 = random.getrandbits(args.Bits2)
bits2 = math.log2(number2)

if args.verbose:
    print("Random Numbers: \n\t{0:,}\n\t\t{2} bits\n\t{1:,}\n\t\t{3} bits".format(number1, number2, bits1, bits2))

# Gather time data for averages
for a in range(0, args.average):
    starttime = time.process_time()

    gcd(number1, number2)

    endtime = time.process_time()
    totaltime = endtime - starttime
    totaltimespan += totaltime

print("Average running time for {0:,} iterations: {1:.4E}".format(args.average, totaltimespan/args.average))
