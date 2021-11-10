
class Registro:
  def __init__(self):
    self.movimientos=[]
    self.movimientosH=[]
    self.activo=0
    self.tiempoT=0
    self.f=0
    self.linea1=[]
    self.velocidad1=[]
    self.tiempo1=[]
    self.linea2=[]
    self.velocidad2=[]
    self.tiempo2=[]
    self.linea3=[]
    self.velocidad3=[]
    self.tiempo3=[]
    self.nombrearchivo=''

  def iniciarRegistro(self):
    if self.activo == 0:
        self.activo=1
        self.movimientos.clear()
        self.f = open("datos.txt","w")
        print("Grabacion iniciada")
    elif self.activo == 1:
        self.activo=0
        tiempoTotal="Tiempo total: " + str(self.tiempoT)
        self.movimientos.append(tiempoTotal)
        for movs in self.movimientos:
          self.f.write("\n"+movs)
        self.f.close()
        print("Grabacion finalizada")
  
  def grabarRegistro(self,par):
    self.movimientos.append(par)

  def grabarHistorial(self,par):
    self.movimientosH.append(par)
    
  def verRegistroGrabado(self):
    print("Registro guardado: ")
    with open("datos.txt",'r') as f:
      for lineas in f:
        print(lineas)

  def verHistorial(self):   
    for elementos in self.movimientosH:
      print(elementos)

  def ejecutarRegistro(self,estado,nombre):
    self.linea1.clear()
    self.velocidad1.clear()
    self.tiempo1.clear()
    self.linea2.clear()
    self.velocidad2.clear()
    self.tiempo2.clear()
    self.linea3.clear()
    self.velocidad3.clear()
    self.tiempo3.clear()
    if estado==0:
      print("Modo automatico activado")
      self.archivo=input("Nombre del archivo de registro: ")
    elif estado==1:
      self.archivo=nombre
    with open(self.archivo, 'r') as f:
        for lineas in f:
          lineas=lineas.replace(" ","").replace("\n","")
          linea= lineas.split(":")
          for n in linea:
            if 'Vinculo1' in n:
              mov1=lineas.split(":")[1:]
              mov1[0]=mov1[0].split(",")[0]
              self.linea1.append(mov1[0])
              dat1=lineas.split(",")[1:]
              self.velocidad1.append(dat1[0])
              self.tiempo1.append(dat1[1])
            elif 'Vinculo2' in n:
              mov2=lineas.split(":")[1:]
              mov2[0]=mov2[0].split(",")[0]
              self.linea2.append(mov2[0])
              dat2=lineas.split(",")[1:]
              self.velocidad2.append(dat2[0])
              self.tiempo2.append(dat2[1])
            elif 'Vinculo3' in n:
              mov3=lineas.split(":")[1:]
              mov3[0]=mov1[0].split(",")[0]
              self.linea3.append(mov3[0])
              dat3=lineas.split(",")[1:]
              self.velocidad3.append(dat3[0])
              self.tiempo3.append(dat3[1])
    