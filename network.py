import socket

def iniciar_servidor():
    host = '0.0.0.0'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reutilizar el puerto
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor esperando conexión...")
    conn, addr = server_socket.accept()
    conn.setblocking(False)  # Configura la conexión para modo no bloqueante
    print(f"Conexión establecida desde {addr}")
    return conn

def conectar_a_servidor():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print("Conectado al servidor.")
    except socket.error as e:
        print(f"Error conectando al servidor: {e}")
    return client_socket

def enviar_mensaje(conn, mensaje):
    conn.sendall(mensaje.encode())

def recibir_mensaje(conn):
    try:
        return conn.recv(1024).decode()
    except BlockingIOError:
        return None
