
import rotation
import x80
import udp
from threading import Thread



print("  ")
def movement(queue,rob, rx, ry,dictionario_de_celdas_de_tareas,lista_obstaculos_mandar,camino_Recorrido):
    print("Entro al movement")
    camino_Recorrido=[]
    print("RX,RY",rx,ry)
    print(dictionario_de_celdas_de_tareas)
    if lista_obstaculos_mandar==None:
        print("ENTRO CONDICION IF")
        lista_obstaculos_mandar=None
    else:
        print("ENTRO AL ELSE")

        lista_obstaculos_mandar=lista_obstaculos_mandar
    faceD = rob.face
    length = len(rx)
    print(length)
    lista_de_tares=dictionario_de_celdas_de_tareas
    print(" ")
    print("Lista tareas MOVE",dictionario_de_celdas_de_tareas)
    print(lista_de_tares)
    rid=rob.id
    camino_Recorrido.append((rob.x,rob.y))


    for i in range(length):
        #lista = [(1, 2), (3, 4), (5, 6), (7, 6), (4, 5)]
        #x = (lista, 1, 1, False)
        #queue.put(x)
        #aqui tenemos que mandarle a rotation el camino que lleva recorrido
        print("ROB.FACE",rob.face)
        print("entro AL FO MOVEMENT")
        if (rx[i], ry[i]) in dictionario_de_celdas_de_tareas:
            print("ENTRO AQUI")
            # cuando sea el mismo que la tarea
            hacer_loop = True
            if i == length - 1:
                hacer_loop=False
        else:
            hacer_loop = False
        tuplito=(rx[i],ry[i])
        camino_Recorrido.append(tuplito)
        ruta_temporal=[]
        #si tuplito es igual a uno de los caminos entoncves
        #hacemos lo de abajo
        #si esta en un de las metas que se detenga por tantos segundos
        #hago un while en donde le digo que no puede continuar(hasta que un sensor sea menor de 5
        #podemos usar el la funcion udp en donde llamaremos  la funcion stop y la de adelante un poquito
        #leemos el puerto indefinidamenteee hasta que se pueda salir del while
        #despues se mira si hay un obstaculo lo que hace usualmente
        print(tuplito)
        print("Valor que toma I : " , i)
        print("LA CARA ES " , faceD)
        print("Vlaor de Rx " , rx[i])
        print("Valor de Ry " , ry[i])
        faceD = whatFace(rob, rx[i], ry[i], faceD)#devuleme la cara a que cara moverme

        #print("-------------------------- MOVIMIENTO = ", i)
        print(" ")
        print(" before rot = ", faceD)
        if i == length - 1:
            condicion_hilo=True
        else:
            condicion_hilo=False
        print("camino recorrido",camino_Recorrido)
        condicion,face_robotcito =rotation.mov(rob, faceD,queue,camino_Recorrido,condicion_hilo,lista_obstaculos_mandar,hacer_loop)
        print(condicion)
        print(faceD)
        print("     ")
        print(" cara despues del obstaculo ")
        print(face_robotcito)

        # la empanada
        if i == length - 1:
            print("ENTRO ESTE CASO PARTICULAR")
            #lista_de_tares.pop(0)
            print("lista de tareas")
            print(lista_de_tares)
            print(rx[i],ry[i])

            if rid==0:
                print("PAPI Entraste")
                rid = rob.id

                rob.x = rx[i]  # nueva posicion del robot
                rob.y = ry[i]
                x80.stop(rid)
                print((False,rob,lista_de_tares,False))
                return (False,rob,lista_de_tares,False)
            elif rid==1:
                rid = rob.id
                x80.stop(rid)
                print((False,rob,lista_de_tares,False))
                return (False,rob,lista_de_tares,False)

        if condicion==True:
            camino_Recorrido.pop(-1)
            #
            print("Entraste Bebe")

            if i==0:
                # R1.put(rob)
                rob.face=faceD
                donde_encontro_obstaculo = (rx[i], ry[i])
                print("Lista de tareas Mov2",lista_de_tares)
                lista_de_tares.insert(0, (rob.x, rob.y))
                print("donde encontro obs mov2",donde_encontro_obstaculo)
                x=condicion,rob,lista_de_tares,donde_encontro_obstaculo

                if rob.id == 0:
                    return x
                elif rob.id == 1:
                    return x
                break
            else:
                #R1.put(rob)
                rob.face = faceD
                lista_de_tares.pop(0)
                lista_de_tares.insert(0,(rob.x,rob.y))
                donde_encontro_obstaculo=(rx[i],ry[i])


                if rid == 0:
                    print(condicion,rob,lista_de_tares,donde_encontro_obstaculo)
                    #posiblemente hacer un pop de la ultima posicion en lista de tareas
                    return (condicion,rob,lista_de_tares,donde_encontro_obstaculo)

                elif rid == 1:
                    print(condicion, rob, lista_de_tares, donde_encontro_obstaculo)
                    return (condicion,rob,lista_de_tares,donde_encontro_obstaculo)


                break
        else:

            if tuplito in lista_de_tares:
                print("HOLA BEBE")
                indice = lista_de_tares.index(tuplito)
                lista_de_tares.pop(indice)





        rob.x = rx[i]  # nueva posicion del robot
        rob.y = ry[i]
        #if condicion==True:
            #break
            #algo.put(detenerse al queue)
        #si detecta obstaculo que se salga
        #y que agrege algo para pasarlo al proceso padreee
        #para que recalcule la ruta
        #if condicion==True:
          #  break

        #break SI DETECTA OBSTACULO  en una posicion devuelva esa POsicion de ese OBSTACULO
        # y que recalcule la ruta con los nuevos obstaculoss
        #decirle que ry[i],rx[i],hay un obstaculo
        #y darle la nueva posicion inicial al posicion actual del robot para actualizar los 4 Cuadros que son los objetivos
        #usando el A *



        #dato_hex = leer_ultrasonido("192.168.0.100", 56338)

        #sensorH,sensorI,sensorJ,sensorK,sensorL,sensorM= sacar_datos_ultrasonido(dato_hex)


        #la posicion vieja del robot










    #print("final face of R = ", rob.x, rob.y)


def whatFace(rob, sigX, sigY, faceD):
    #recibe X,Y
    #sacamos las cordenas actuales del robot
    #y le decimos que cara #para decirle que movimiento tiene que hacer
    acX = rob.x
    acY = rob.y
    if (acX == sigX) and (acX == acY):
        #mismo lugar
        faceD = 0

    if (acX== sigX) and (sigY > acY):
        #AL FRENTE
        faceD = 1

    if (sigX<acX) and (sigY>acY):
        #derecha adelante
        faceD = 2

    if (sigX<acX) and (acY == sigY):
        #derecha
        #punto referencia robot mirando alante
        faceD = 3

    if (sigY<acY) and (sigX<acX):
        #atrax derecha
        faceD = 4


    if (acX == sigX) and (sigY < acY):
        #atrax
        faceD = 5

    if (sigY<acY) and (sigX>acX):
        #atrax izquierda
        faceD = 6

    if (sigX>acX) and (acY==sigY):
        #IZQuierda referencia robot mirando alante
        faceD = 7

    if (sigX>acX) and (sigY>acY):
        faceD = 8
        #diagonal izquierda referencia robot mirando alante
    #print("faceD calc = ", faceD)
    return faceD




