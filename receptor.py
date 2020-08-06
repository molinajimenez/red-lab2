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

def detectError(arr, nr): 
    nr = int(nr)
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
            
            

            
            print("********")


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

#Tomado de: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def funcion_x():
    print("funcion x")


print("El receptor esta esperando un mensaje")
iniciar_server()


"""

st = "hola tony"
print(st)
print(' '.join(map(bin,bytearray(st,'utf8'))))

print("testeando test_to_bits")
result2 = text_to_bits("hola tony")
print(result2)

"""