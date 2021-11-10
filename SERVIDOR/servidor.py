import socket

class Servidor:
    def __init__(self):
        self.conexion = 0
        self.estado = 0
        self.dato=0
    def iniciarServidor(self):
        
        direccionServidor = "localhost"
        puertoServidor = 8000
        mi_socket = socket.socket()
        mi_socket.bind((direccionServidor, puertoServidor))
        mi_socket.listen(5)
        print("Esperando conexion...")
        self.conexion, addr = mi_socket.accept()
        print("Nueva conexion establecida")
        print(addr)
        print("---El robot está siendo controlado por el Cliente---")
        self.estado = 1
    def terminarServidor(self):
        self.estado=0
        self.conexion.close()
    def recibirDatos(self):
        ordenes = self.conexion.recv(1024).decode()
        return(ordenes)
    def enviarDatos(self,mensaje):
        self.conexion.send(str(mensaje).encode())