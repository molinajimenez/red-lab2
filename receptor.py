import socket
import threading

# size del header, es la longitud del contenido que va a enviar el emisor/cliente
HEADERSIZE = 2020
FORMAT = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# direccion
HOST = socket.gethostname()

# puerto donde se va a oir
PORT = 1234

# el bind() se utiliza para asociar el socket con una interfaz de red específica y un número de puerto:
server.bind((HOST, PORT))


def conexion_cliente(conn, addr):
    print(f"CONEXION CON CLIENTE: {addr}")

    # mientras que connection sea verdadero, se va a estar en el  while
    # se va a salir de loop si se envia la palabra adios para ir a close() para cerrar el socket
    connection = True
    while connection:

        # conn.rev(HEADERSIZE) se utiliza para recibir cierta cantidad de bytes del cliente
        # en este caso, queremos recibir la cantidad puesta en HEADERSIZE.
        msg_length = conn.recv(HEADERSIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == "adios":
                connection = False

            print(msg)


    conn.close()

#funcion para iniciar el servidor/receptor
def iniciar_server():
    # se oye/busca la conexion del cliente
    server.listen()

    while True:
        # se acepta el .connect() del emison/cliente donde se obtiene 
        # addr guarda la direccion y puerto de donde vino la conexion 
        # conn es el objeto que se utilzará para enviar mensajes de vuelta al cliente
        conn, addr = server.accept()
        # socket
        print("conn es: ", conn)
        # se crea un thread para cada nuevo cliente conectado con el servidor para tener más de uno
        # ejecutará la función conexion_cliente con los argumentos conn y addr
        thread = threading.Thread(target=conexion_cliente, args=(conn, addr))
        thread.start()

print("El receptor esta esperando un mensaje")
iniciar_server()