from bitarray import bitarray
import random
import math
# Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def bits_to_bitarray(text):
    return bitarray(text)

# noise, it receives message, and 1/prob probability of messing certain position. it runs on each bit of the message.


def noise(text):
    arr_txt = list(text)

    rand = random.randint(0, len(arr_txt))

    if(arr_txt[rand] == '0'):
        arr_txt[rand] = '1'
    else:
        arr_txt[rand] = '0'
    
    return bitarray("".join(arr_txt))
    


# function that determines required parity bit


def calculate_rbit(length):
    for i in range(length):
        if(2**i >= length + i + 1):
            return i


def pos_rbit(data, redundancy):
    j = 0
    k = 1
    length = len(data)
    res = ''
    for i in range(1, length + redundancy+1):
        # if the counter is at a 2 power position. add a 0 as parity bit.
        if(i == 2**j):
            res = res + '0'
            j += 1
        # if not just add to the res answer the data..
        else:
            res = res + data[-1 * k]
            k += 1

    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # 1 en posicion significativa
            # position then Bitwise OR the array value
            # to find parity bit value.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j array esta al reves

        # concatenamos..
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr




def hamming(message="hola", m=len("hola")):
    arr_answer = []
    r_bits = calculate_rbit(m)
    arr = pos_rbit(message, r_bits)
    arr = calcParityBits(arr, r_bits)

    arr_answer.append(arr)
    arr_answer.append(r_bits)
    return arr_answer


result = text_to_bits("hola tony")
nois = noise(result)
print("", result)
print("", nois)
arr = hamming(result, len(result))
