import argparse
import random
import time


# The key
K = "This is my key!"
Kbytearray = bytearray()
Kbytearray.extend(map(ord, K))


# The RC4 algorithm function
def rc4(inputbytearray, keybytearray):
    '''
    This returns the RC4 encryption/decryption of a byte array with the key array
    :param inputbytearray: The byte array of the input to be encrypted/decrypted
    :param keybytearray: The key (< 256 bytes) for the encryption
    :return: A byte array of the results
    '''
    outputbytearray = bytearray()

    # The state vector
    S = []

    # The replicated key vector
    T = []

    #
    # Initialization
    #
    for i in range(0, 256):
        S.append(i)
        T.append(keybytearray[i % len(keybytearray)])

    #
    # Initial permutation of S
    #
    j = 0
    for i in range(0, 256):
        j = (j + S[i] + T[i]) % 256
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp

    #
    # Stream generation
    #
    i = 0
    j = 0
    for p in range(0, len(inputbytearray)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp
        t = (S[i] + S[j]) % 256
        k = S[t]
        outputbytearray.append(k ^ inputbytearray[p])

    return outputbytearray

# Main functionality starts here...

# Argument parsing
parser = argparse.ArgumentParser(description='RC4 encryption/decryption.')
parser.add_argument('Size',
                    help='The size, in bytes, of random data to encrypt/decrypt.',
                    type=int)
parser.add_argument("-s", "--seed",
                    help="The seed value to the random function to simulate a malware file."
                         "", default=0, type=int, required=False)
parser.add_argument("-a", "--average",
                    help="The number of runs for averaging, greater than zero."
                         "", default=1, type=int, required=False)

args = parser.parse_args()

# Random seed for reproducibility
random.seed(args.seed)

# Random Data
plainbytes = [random.randint(0, 255) for i in range(0, args.Size)]
# plaintext = "This is my plaintext!"
# plainbytes = bytearray()
# plainbytes.extend(map(ord, plaintext))

# Create running time counter...
totaltimespan = 0

# Gather time data for averages
for a in range(0, args.average):
    starttime = time.process_time()

    cipherbytes = rc4(plainbytes, Kbytearray)

    endtime = time.process_time()
    totaltime = endtime - starttime
    totaltimespan += totaltime

print("Average running time for {0:,} iterations: {1:.4E}".format(args.average, totaltimespan/args.average))

# Check correctness
cipherbytes = rc4(plainbytes, Kbytearray)
plainbytes2 = rc4(cipherbytes, Kbytearray)

correctness = True
for i in range(0, len(plainbytes2)):
    if plainbytes[i] != plainbytes2[i]:
        print("{0} {1} {2}".format(i, plainbytes[i], plainbytes2[i]))
        correctness = False
        break

if correctness is True:
    print("Algorithm is correct!")
else:
    print("Algorithm is NOT correct!")

# print("".join(map(chr, cipher)))