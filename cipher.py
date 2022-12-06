import math
import numpy as np


def shift_cipher(text, shift, alphabets):

    def shift_alphabets(alphabets):
        return alphabets[shift:] + alphabets[:shift]

    shifted_alphabets = tuple(map(shift_alphabets, alphabets))
    final_alphabets = ''.join(alphabets)
    final_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabets, final_shifted_alphabets)
    return text.translate(table)


def tricipherenc(pt):
    mx = []
    n = int(0)
    while len(pt) > n * n:
        n = n + 1

    # padding
    pt = pt + ((n * n) - len(pt)) * '&'
    ct = ""
    mx = []

    # buat matriks segitiga
    ptidx = 0
    for i in range(0, n):
        temp = []
        for j in range(0, (2 * n) - 1):
            if j >= math.ceil(((2 * n) - 1) / 2) - i - 1 and j <= math.ceil(
                    ((2 * n) - 1) / 2) + i - 1:
                temp.append(pt[ptidx])
                ptidx += 1
            else:
                temp.append('\0')
        mx.append(temp)

    # enkripsi
    for i in range(0, (2 * n) - 1):
        for j in range(0, n):
            if mx[j][i] != '\0':
                ct += mx[j][i]
    return ct


def tricipherdec(ct):
    mx = []
    n = int(math.sqrt(len(ct)))
    ctidx = 0
    for i in range(0, (2 * n) - 1):
        temp = []
        for j in range(0, n):
            idx = j
            if i > ((2 * n) - 1) / 2:
                idx = j + n - (2 * (i % n)) - 2
            if idx >= n - (i % n) - 1:
                temp.append(ct[ctidx])
                ctidx += 1
            else:
                temp.append('\0')
        mx.append(temp)

    transpmx = np.transpose(mx)

    pt = ''
    for i in range(0, n):
        for j in range(0, (2 * n) - 1):
            if transpmx[i][j] not in ['\0', '&']:
                pt += transpmx[i][j]

    return pt