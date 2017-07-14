import argparse


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
parser.add_argument('Number1',
                    help='The first number to find the GCD.',
                    type=int)
parser.add_argument('Number2',
                    help='The second number to find the GCD.',
                    type=int)
parser.add_argument("-a", "--average",
                    help="The number of runs for averaging, greater than zero."
                         "", default=1, type=int, required=False)

args = parser.parse_args()

print(gcd(args.Number1, args.Number2))