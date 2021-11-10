from cliente import Cliente
from excepciones import excepcionMenu
from excepciones import excepcionBrazo
from excepciones import excepcionRango

cliente1 = Cliente()
while True:
    try:
        menu = int(input("""
---------------Menu Principal-----------------
|                                            | 
|   1) Conectar/Desconectar con el Servidor  |
|   2) Encender/Apagar Robot                 |
|   3) Ver historial de movimientos          | 
|   4) Comandos de control                   |
|                                            |
|   0) Salir del programa                    |
----------------------------------------------
--> """))
        if menu == 0:
            print("Programa finalizado")
            cliente1.enviarDatos(menu)
            if cliente1.estado==1:
                cliente1.terminarCliente()
            break

        elif menu == 1:
            if cliente1.estado == 0:
                cliente1.iniciarCliente()
            elif cliente1.estado == 1:
                cliente1.enviarDatos(menu)
                cliente1.terminarCliente()

        elif cliente1.estado==1:
            if menu == 2:
                cliente1.enviarDatos(menu)
                info1=cliente1.recibirDatos()   #recibe la info del estado del robot
                print(info1)
            elif menu == 3:
                cliente1.enviarDatos(menu)
                cant_elementos=cliente1.recibirDatos()
                print("Registro de movimientos:")
                print("Vinculo N°:Angulo,Velocidad,Tiempo")
                k=0
                while k < int(cant_elementos):
                    ele=cliente1.recibirDatos()
                    print(ele)
                    k+=1
                    cliente1.enviarDatos("OK")

            elif menu == 4:
                cliente1.enviarDatos(menu)
                estadobrazo=cliente1.recibirDatos()
                while True:
                    menu = int(input("""
    --------------Comandos de Control-------------
    |                                            |
    |   1) Mover vinculo 1                       |
    |   2) Mover vinculo 2                       |
    |   3) Mover vinculo 3                       |
    |   4) Encender/Apagar Efector               |
    |   5) Mostrar posicion actual               |
    |   6) Volver a la posicion inicial          |
    |                                            |
    |   0) Volver al menu principal              |
    ----------------------------------------------
    --> """))       
                    if int(estadobrazo)==1:

                        if menu == 1:
                            cliente1.enviarDatos(menu)
                            while True:
                                try:                                    
                                    vi1 = input("Ingrese el angulo de rotacion (0 a 360): ")
                                    cliente1.enviarDatos(vi1)
                                    vel = input("Ingrese la velocidad (rad/s): ")
                                    cliente1.enviarDatos(vel)
                                    rangos_=int(cliente1.recibirDatos())    #CHEQUEA SI EL VALOR INGRESADO ESTA DENTRO DEL RANGO
                                    if rangos_ == 1:
                                        break
                                    elif rangos_ == 0:
                                        raise excepcionRango()
                                except excepcionRango:
                                    print("El angulo ingresado esta fuera de rango...")

                        if menu == 2:
                            cliente1.enviarDatos(menu)
                            while True:
                                try:
                                    vi2 = input("Ingrese el angulo de rotacion (-90 a 90): ")
                                    cliente1.enviarDatos(vi2)
                                    vel = input("Ingrese la velocidad (rad/s): ")
                                    cliente1.enviarDatos(vel)
                                    rangos_=int(cliente1.recibirDatos())    #CHEQUEA SI EL VALOR INGRESADO ESTA DENTRO DEL RANGO
                                    if rangos_ == 1:
                                        break
                                    elif rangos_ == 0:
                                        raise excepcionRango()
                                except excepcionRango:
                                    print("El angulo ingresado esta fuera de rango...")

                        if menu == 3:
                            cliente1.enviarDatos(menu)
                            while True:
                                try:
                                    vi3 = input("Ingrese el angulo de rotacion (-90 a 90): ")
                                    cliente1.enviarDatos(vi3)
                                    vel = input("Ingrese la velocidad (rad/s): ")  
                                    cliente1.enviarDatos(vel)
                                    rangos_=int(cliente1.recibirDatos()) #CHEQUEA SI EL VALOR INGRESADO ESTA DENTRO DEL RANGO
                                    if rangos_ == 1:
                                        break
                                    elif rangos_ == 0:
                                        raise excepcionRango()
                                except excepcionRango:
                                    print("El angulo ingresado esta fuera de rango...")  

                        elif menu==4:
                            cliente1.enviarDatos(menu)
                            efector=int(cliente1.recibirDatos())    
                            if efector==1:
                                print("El efector esta encendido")
                            elif efector==0:
                                print("El efector esta apagado")
                        
                        elif menu==5:
                            cliente1.enviarDatos(menu)
                            v123=cliente1.recibirDatos()
                            print("Los vinculos se han movido:\n") 
                            print(v123)                        
                        elif menu==6:
                            cliente1.enviarDatos(menu)
                            print("El robot se encuentra en la posicion incial")
                        elif menu==0:
                            cliente1.enviarDatos(menu)
                            break
                    elif int(estadobrazo)==0 and menu!=0:
                        print("No se pueden realiza acciones. El brazo está apagado.")
                    elif menu==0:
                        cliente1.enviarDatos(menu)
                        break
        elif cliente1.estado==0:
            print("No hay conexión con el servidor")
        else:
            raise excepcionMenu
    except ValueError:
        print("El comando ingresado no es valido")
    except excepcionMenu:
        print("El comando ingresado no es valido")
    except excepcionBrazo:
        print("El robot esta apagado, debe encenderlo primero")
    except ConnectionRefusedError:
        print("No se pudo establecer la conexion con el servidor")
