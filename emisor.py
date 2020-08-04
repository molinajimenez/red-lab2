import socket

HEADERSIZE = 2020
FORMAT = "utf-8"

emisor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
emisor.connect((socket.gethostname(), 1234))


def enviar_mensaje(msg):
    mensaje = msg.encode(FORMAT)
    msg_length = len(mensaje)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE - len(send_length))
    emisor.send(send_length)
    emisor.send(mensaje)


while True:
    de_usuario = input("Ingresa mensaje: ")
    enviar_mensaje(de_usuario)