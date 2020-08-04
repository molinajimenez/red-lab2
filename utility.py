from bitarray import bitarray
import random
import math
#Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#noise, it receives message, and 1/prob probability of messing certain position. it runs on each bit of the message.
def noise(message, prob=25):
    for x in range(0, len(message)):
        random_value = random.randint(0,prob)
        selected_value = random.randint(0,prob) 
        if(random_value == selected_value):
            error = random.randint(0,1)
            message = message[:x-1] + str(error) + message[x+1:]
            print("switching ", x ," to ", error)
    return message

#function that determines required parity bit
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
        #if not just add to the res answer the data..
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
  
        #concatenamos..
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n) 
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 
    return arr 
    
def detectError(arr, nr): 
    n = len(arr) 
    res = 0
  
    # Calculate parity bits again 
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 
  
        # Create a binary no by appending 
        # parity bits together. 
  
        res = res + val*(10**i) 
  
    # Convert binary to decimal 
    return int(str(res), 2) 


def hamming(message="hola", m = len("hola")):
    r_bits = calculate_rbit(m)
    arr = pos_rbit(message, r_bits)
    arr = calcParityBits(arr,r_bits)
    return arr

    
result = text_to_bits("hola tony")
arr = hamming(result, len(result))
#data transfer
print(result)
print(arr)
noise(result)