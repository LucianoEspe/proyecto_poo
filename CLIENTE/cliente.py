import socket

class Cliente:
    def __init__(self):
        self.estado=0
        self.mi_socket=0

    def iniciarCliente(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('localhost', 8000))
        self.estado=1
        print("Conexion realizada")

    def enviarDatos(self,mensaje):
        self.mi_socket.send(str(mensaje).encode())
    
    def recibirDatos(self):
        ordenes = self.mi_socket.recv(1024).decode()
        return(ordenes)

    def terminarCliente(self):
        print("Conexion finalizada")
        self.mi_socket.close()
        self.estado=0
    
