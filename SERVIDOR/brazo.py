from excepciones import excepcionRango
from servidor import Servidor
import math

servidor1=Servidor()

class Brazo:
    def __init__(self):
        self.vi1 = 0
        self.vi2 = 0
        self.vi3 = 0
        self.vel = 0
        self.rango = 0
        self.estado = 0
        self.tiempo = 0

    def encender(self):
        if self.estado == 0:
            self.estado = 1
            if servidor1.estado==1:
                servidor1.enviarDatos("El robot esta encendido")
            else:
                print("El robot esta encendido")
        elif self.estado == 1:
            self.estado = 0
            if servidor1.estado==1:
                servidor1.enviarDatos("El robot esta apagado")
            else:
                print("El robot esta apagado")

    def casa(self):
        self.vi1 = 0
        self.vi2 = 0
        self.vi3 = 0
        if servidor1.estado==0:
            print("El robot se encuentra en la posicion inicial")

    def vinculo1(self):
        while True:
            try:
                self.rango = 360
                if servidor1.estado==0:
                    self.vi1 = input("Ingrese el angulo de rotacion (0 a 360): ")
                    self.vel = input("Ingrese la velocidad (rad/s): ")
                if servidor1.estado==1:
                    self.vi1=servidor1.recibirDatos()
                    self.vel=servidor1.recibirDatos()
                vinc = int(self.vi1)
                self.tiempo = (float(vinc) * (math.pi/180))*float(self.vel)
                if int(self.vi1) < 0 or int(self.vi1) > self.rango:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("0")  ##FUERA DE RANGO (Se envia un 0 al cliente)
                    raise excepcionRango()
                else:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("1") ##DATOS CARGADOS OK (Se envia un 1 al cliente)
                    break
            except excepcionRango:
                if servidor1.estado==0:
                    print("El angulo ingresado esta fuera de rango...")

    def vinculo2(self):
        while True:
            try:
                self.rango = abs(90)
                if servidor1.estado==0:
                    self.vi2 = input("Ingrese el angulo de rotacion (-90 a 90): ")
                    self.vel = input("Ingrese la velocidad (rad/s): ")
                elif servidor1.estado==1:
                    self.vi2=servidor1.recibirDatos()
                    self.vel=servidor1.recibirDatos()
                vinc = abs(int(self.vi2))
                self.tiempo = (float(vinc) * (math.pi/180))*float(self.vel)
                if int(self.vi2) < -self.rango or int(self.vi2) > self.rango:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("0")  ##FUERA DE RANGO (Se envia un 0 al cliente)
                    raise excepcionRango()
                else:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("1") ##DATOS CARGADOS OK (Se envia un 1 al cliente)
                    break
            except excepcionRango:
                if servidor1.estado==0:
                    print("El angulo ingresado esta fuera de rango...")

    def vinculo3(self):
        while True:
            try:
                self.rango = abs(90)
                if servidor1.estado==0:
                    self.vi3 = input("Ingrese el angulo de rotacion (-90 a 90): ")
                    self.vel = input("Ingrese la velocidad (rad/s): ")
                elif servidor1.estado==1:
                    self.vi3=servidor1.recibirDatos()
                    self.vel=servidor1.recibirDatos()
                vinc = abs(int(self.vi3))
                self.tiempo = (float(vinc) * (math.pi/180))*float(self.vel)
                if int(self.vi3) < -self.rango or int(self.vi3) > self.rango:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("0")  ##FUERA DE RANGO (Se envia un 0 al cliente)
                    raise excepcionRango()
                else:
                    if servidor1.estado==1:
                        servidor1.enviarDatos("1") ##DATOS CARGADOS OK (Se envia un 1 al cliente)
                    break
            except excepcionRango:
                if servidor1.estado==0:
                    print("El angulo ingresado esta fuera de rango...")

    def info(self):
        if servidor1.estado == 0:
            print("Los vinculos se han movido:\n")
            print("Vinculo 1: ", self.vi1)
            print("Vinculo 2: ", self.vi2)
            print("Vinculo 3: ", self.vi3)
        elif servidor1.estado == 1:
            mensaje_="Vinculo 1: "+ str(self.vi1) + " Vinculo 2: " + str(self.vi2) + " Vinculo 3: "+ str(self.vi3)
            servidor1.enviarDatos(mensaje_)