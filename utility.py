from bitarray import bitarray
import random
import math
#Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#TODO: finish noise function
def noise(message):
    for x in range(0, len(message)):
        random_value = random.randint(0,25)
        selected_value = random.randint(0,25) 
        if(random_value == selected_value):
            message[x] = random.randint(0,1)
            print("switching ", x ," to ", random_value)
    return message

#TODO: separate hamming, finish steps
def hamming(message="hola"):
    length = len(message)
    #lista de posiciones
    arr = []
    for x in range(1, length):
        #calculamos logaritmo 2.
        res = math.log(x,2)
        #si el resultado (retornado como float), su parte decimal es 0.0 convertimos a int y agregamos a lista.
        if(math.modf(res)[0] == 0.0):
            arr.append(int(x))
    print(arr)
#TODO: finish counter function
def hamming_counter(message, list_parity):
    count = 0
    for x in range(0, len(list_parity)) :
        message[x] = 0

    

result = text_to_bits("hola tony")
hamming(result)