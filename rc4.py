# The plaintext
# plaintext = "This is my plaintext!"
# plainbytearray = bytearray()
# plainbytearray.extend(map(ord, plaintext))

# The key
#K = "This is my key!"


def rc4(inputbytearray, keybytearray):
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
        outputbytearray[p] = k ^ inputbytearray[p]

    return outputbytearray

