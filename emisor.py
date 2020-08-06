import socket

from utility import *
HEADERSIZE = 2020
FORMAT = "utf-8"
KEY = "1001"
emisor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# El emisor/cliente llama a connect () para establecer una conexión con el servidor e three way handshake
emisor.connect((socket.gethostname(), 1234))

#Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def encodeData(data, key): 
   
    l_key = len(key) 
   
    # Appends n-1 zeroes at end of data 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    # Append remainder in the original data 
    codeword = data + remainder 
    return codeword     

def enviar_mensaje(msg):
    #ans = encodeData(msg,KEY) 
    mensaje = msg.encode(FORMAT)
    msg_length = len(mensaje)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE - len(send_length))
    emisor.send(send_length)
    emisor.send(mensaje)


while True:
    #alter_noise = noise(text_to_bits("hola tony"))
    enviar_mensaje(text_to_bits("hola tony"))
    enviar_mensaje("adios")