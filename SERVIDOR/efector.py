
class Efector:
  def __init__(self):
    self.estado=0


  def activarEfector(self,estadoservidor1):
    if self.estado == 0:
      self.estado=1
      if estadoservidor1==0:
        print("El efector esta encendido")
    elif self.estado == 1:
      self.estado=0
      if estadoservidor1==0:
        print("El efector esta apagado")