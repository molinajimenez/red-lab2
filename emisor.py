import socket

from utility import noise

HEADERSIZE = 2020
FORMAT = "utf-8"

emisor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# El emisor/cliente llama a connect () para establecer una conexión con el servidor e three way handshake
emisor.connect((socket.gethostname(), 1234))

#Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def enviar_mensaje(msg):
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