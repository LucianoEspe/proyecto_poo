import time
from brazo import Brazo
from brazo import servidor1
from efector import Efector
from grafico import Grafico
from registro import Registro
from excepciones import excepcionMenu
from excepciones import excepcionBrazo


brazo1=Brazo()
efector1=Efector()
registro1=Registro()
grafico1=Grafico()

while True:
  try:
    if servidor1.estado==0:
      menu=int(input("""
  ---------------Menu Principal-----------------
  |                                            | 
  |   1) Abrir/Cerrar el servidor              |
  |   2) Encender/Apagar Robot                 |
  |   3) Encender/Apagar grabacion de registro |
  |   4) Ver historial de movimientos          |
  |   5) Ver registro grabado                  |
  |   6) Modo Automatico                       | 
  |   7) Comandos de control                   |
  |                                            |
  |   0) Salir del programa                    |
  ----------------------------------------------
  --> """))
      if menu==0:
        print("Programa finalizado")
        break
      elif menu==1:
        if servidor1.estado==0:
          servidor1.iniciarServidor()
        elif servidor1.estado==1:
          servidor1.terminarServidor()
      elif menu==2:
        brazo1.encender()
        brazo1.casa()
        if brazo1.estado==0:
          efector1.estado=0
      elif menu==3:
        registro1.iniciarRegistro()
      elif menu==4:
        print("Registro de movimientos:")
        print("Vinculo N°:Angulo,Velocidad,Tiempo")
        registro1.verHistorial()  #HISTORIAL DE MOVIMIENTOS
      elif menu==5:
        registro1.verRegistroGrabado()  #REGISTRO GRABADO (Aprendizaje)
      elif menu==6:
        if brazo1.estado==1:
          registro1.ejecutarRegistro(servidor1.estado,0)
          i=0
          for n in registro1.linea1:
            brazo1.vi1=int(registro1.linea1[i])
            brazo1.vel1=float(registro1.velocidad1[i])
            brazo1.vi2=int(registro1.linea2[i])
            brazo1.vel2=float(registro1.velocidad2[i])
            brazo1.vi3=int(registro1.linea3[i])
            brazo1.vel3=float(registro1.velocidad3[i])
            print("Ejecutando movimiento...")
            tiempo=float(registro1.tiempo1[i])+float(registro1.tiempo2[i])+float(registro1.tiempo3[i])
            time.sleep(tiempo)
            brazo1.info()
            print("El tiempo empleado fue:",tiempo,"segundos")
            i=i+1
        else:
          print("El robot esta apagado, debe encenderlo primero")
      elif menu==7:
        while True:
          menu=int(input("""
  --------------Comandos de Control-------------
  |                                            |
  |   1) Mover vinculo 1                       |
  |   2) Mover vinculo 2                       |
  |   3) Mover vinculo 3                       |
  |   4) Encender/Apagar Efector               |
  |   5) Mostrar posicion actual               |
  |   6) Volver a la posicion inicial          |
  |                                            |
  |   7) Ver robot                             |
  |   0) Volver al menu principal              |
  ----------------------------------------------
  --> """))
          if brazo1.estado==1:
            if menu==1:
              brazo1.vinculo1()
              if registro1.activo==0:
                reg="Vinculo 1: "+ str(brazo1.vi1) +","+ str(brazo1.vel) +"," + str(brazo1.tiempo)
                registro1.grabarHistorial(reg)
              if registro1.activo==1:
                registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
                reg="Vinculo 1: "+ str(brazo1.vi1) +","+ str(brazo1.vel) +"," + str(brazo1.tiempo)
                registro1.grabarRegistro(reg)
                registro1.grabarHistorial(reg)

            elif menu==2:
              brazo1.vinculo2()
              if registro1.activo==0:
                reg="Vinculo 2: "+ brazo1.vi2 +"," + brazo1.vel +"," + str(brazo1.tiempo)
                registro1.grabarHistorial(reg)
              if registro1.activo==1:
                registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
                reg="Vinculo 2: "+ brazo1.vi2 +"," + brazo1.vel +"," + str(brazo1.tiempo)
                registro1.grabarRegistro(reg)
                registro1.grabarHistorial(reg)
                
            elif menu==3:
              brazo1.vinculo3()
              if registro1.activo==0:
                reg="Vinculo 3: "+ brazo1.vi3 +"," + brazo1.vel +"," + str(brazo1.tiempo)
                registro1.grabarHistorial(reg)
              if registro1.activo==1:
                registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
                reg="Vinculo 3: "+ brazo1.vi3 +"," + brazo1.vel +"," + str(brazo1.tiempo)
                registro1.grabarRegistro(reg)
                registro1.grabarHistorial(reg)
                
            elif menu==4:
              efector1.activarEfector(servidor1.estado)  
            elif menu==5:
              brazo1.info()
            elif menu==6:
              brazo1.casa()
          if menu==7:
            grafico1.mostrarGraf()
          elif menu==0:
            break 
          elif brazo1.estado==0:
            raise excepcionBrazo
      else:
        raise excepcionMenu 
    elif servidor1.estado==1:     #--------------CONEXION Y CONTROL DESDE EL CLIENTE------------------------
      menu=int(servidor1.recibirDatos())
      if menu==0:
        print("El cliente finalizó")
        servidor1.terminarServidor()
      elif menu==1:
        print("El cliente finalizó")
        servidor1.terminarServidor()
      elif menu==2:
        brazo1.encender()
        brazo1.casa()
        if brazo1.estado==0:
          efector1.estado=0
      elif menu==3:
        cant_elementos=len(registro1.movimientosH)
        servidor1.enviarDatos(cant_elementos)
        for elementos in registro1.movimientosH:
          servidor1.enviarDatos(elementos) 
          servidor1.recibirDatos()
      elif menu==4:    
        servidor1.enviarDatos(str(brazo1.estado))
        while True:
          menu=int(servidor1.recibirDatos())
          if brazo1.estado==1:
            if menu==1:
              brazo1.vinculo1()
              registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
              reg="Vinculo 1: "+ str(brazo1.vi1) +","+ str(brazo1.vel) +"," + str(brazo1.tiempo)
              registro1.grabarHistorial(reg)
            elif menu==2:
              brazo1.vinculo2()
              registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
              reg="Vinculo 2: "+ str(brazo1.vi2) +"," + str(brazo1.vel) +"," + str(brazo1.tiempo)
              registro1.grabarHistorial(reg)
                
            elif menu==3:
              brazo1.vinculo3()
              registro1.tiempoT=registro1.tiempoT+brazo1.tiempo
              reg="Vinculo 3: "+ str(brazo1.vi3) +"," + str(brazo1.vel) +"," + str(brazo1.tiempo)
              registro1.grabarHistorial(reg)
                
            elif menu==4:
              efector1.activarEfector(servidor1.estado)  
              servidor1.enviarDatos(efector1.estado)
            elif menu==5:
              brazo1.info()
            elif menu==6:
              brazo1.casa()
              brazo1.info()
            elif menu==0:
              break   
          elif menu==0:
            break 
          elif brazo1.estado==0 and menu !=0:
            raise excepcionBrazo
      else:
        raise excepcionMenu 
  except ValueError:
    print("El comando ingresado no es valido")
  except excepcionMenu:
    print("El comando ingresado no es valido")
  except excepcionBrazo:  
      print("El robot esta apagado, debe encenderlo primero")