import socket
import threading

HEADERSIZE = 2020
FORMAT = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))

def conexion_cliente(conn, addr):
    print(f"CONEXION CON CLIENTE: {addr}")

    conectado = True
    while conectado:
        msg_length = conn.recv(HEADERSIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == "adios":
                conectado = False

            print(msg)


    conn.close()

#funcion para iniciar el servidor/receptor
def iniciar_server():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=conexion_cliente, args=(conn, addr))
        thread.start()

print("El receptor esta esperando un mensaje")
iniciar_server()