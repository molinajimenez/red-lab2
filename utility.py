from bitarray import bitarray
import random

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

    rand = random.randint(0, len(arr_txt)-1)

    if(arr_txt[rand] == '0'):
        arr_txt[rand] = '1'
    else:
        arr_txt[rand] = '0'
    
    return "".join(arr_txt)
    

