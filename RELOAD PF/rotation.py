import x80,udp
def mov(robot, faceD,queue,camino_Recorrido,condicion_hilo,lista_obstaculos_mandar,hacer_loop):

    destiny = faceD #establece la nueva posicion o donde se va dirigir

    face = robot.face# en donde esta ahora mismo
    #print("faceR = ", face)

    #print("faceD = ", destiny)
    rid = robot.id
    #dependidon de la cara actual del robot
    print(" ")
    print("Rid Robot")
    print(rid)
    # ----------------- 0 -------------------#
    if face == 0:
        #se detiene
        #el centro
        x80.stop(rid)
        condicion=False
        face=robot.face
        print(" CONDICIONALCITO")
        print((condicion, face))
        return (condicion, face)

    # ----------------- 1 -------------------#
    if face == 1:
        if destiny == 1:
            #print("0º")
            #print("Forward Corto")


            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano  1")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1(   "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        if destiny == 2:
            #print("45º derecha")
            puerto=x80.turn45(rid, 0)
            #print("Forward Largo")
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1(   "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            #print("cara del robot = ", robot.face)
        if destiny == 3:
            #print("90º derecha")
            puerto=x80.turn90(rid, 0)
            #print("Forward Corto")


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:
            #print("90º derecha")
            #print(" 45º derecha")
            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)
            #print("Forward Largo")

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:
            #print("90º derecha")
            #print("90 derecha")
            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)
            #print("Forward Corto")


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1(   "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 <18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:
            #print("90º IZQUIERDA")
            #print("45º IZQUIERDA")
            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)
            #print("Forward Largo")
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)


        if destiny == 7:
            #print("90º IZQUIERDA")
            puerto=x80.turn90(rid, 1)
           #print("Forward Corto")


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI2<18or sensoresI0<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            #print("45º IZQUIERDA")
            puerto=x80.turn45(rid, 1)
            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0< 18 or sensoresI2<18:
                    condicion=True


                    robot.face =face
                    print("HOLA PIBE VALDERAMAAA")
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    # print("Forward Largo")
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion,robot.face)

            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)










   # print("cara del robot afuera = ", robot.face)

    # ----------------- 2 -------------------#
    if face == 2:
        if destiny == 1:
            ##print("45º IZQUIERDA")
            puerto=x80.turn45(rid, 1)
            #print("Forward Corto")


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:
            ##print("0º")
            ##print("Forward Largo")

            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0 <18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny

                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            puerto=x80.turn45(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)

                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)

                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1( "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        if destiny == 7:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            puerto=x80.turn90(rid, 1)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        # ----------------- 3 -------------------#
    if face == 3:
        if destiny == 1:

            puerto=x80.turn90(rid, 1)


            if rid == 0:
                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)

                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:

            puerto=x80.turn45(rid, 1)



            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0< 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    robot.face = destiny
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:


            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0 , sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            puerto=x80.turn90(rid, 0)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        if destiny == 6:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)

                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0< 22 or sensoresI2<22:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:

                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:

                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:

                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        # ----------------- 4 -------------------#
    if face == 4:
        if destiny == 1:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:

            puerto=x80.turn90(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.fac1e = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0 < 18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            puerto=x80.turn45(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        # ----------------- 5 -------------------#
    if face == 5:
        if destiny == 1:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1( "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0< 18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1,sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)


                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            puerto=x80.turn90(rid, 1)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0< 18  or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:

            puerto=x80.turn90(rid, 0)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        # ----------------- 6 -------------------#
    if face == 6:
        if destiny == 1:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)

            if rid == 0:
                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            puerto=x80.turn90(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1( "192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)

                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:

            puerto=x80.turn45(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

        # ----------------- 7 -------------------#
    if face == 7:
        if destiny == 1:

            puerto=x80.turn90(rid, 0)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)



            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            puerto=x80.turn90(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            puerto=x80.turn45(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0 <18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:



            puerto = x80.forward2(rid, 0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18:
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:

            puerto=x80.turn45(rid, 0)


            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)

    # ----------------- 8 -------------------#
    if face == 8:
        if destiny == 1:

            puerto=x80.turn45(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 2:


            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 3:

            x80.turn90(rid, 0)
            puerto=x80.turn45(rid, 0)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                print(sensoresI1)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 4:

            x80.turn90(rid, 0)
            puerto=x80.turn90(rid, 0)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 5:

            x80.turn90(rid, 1)
            puerto=x80.turn45(rid, 1)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 6:

            puerto=x80.turn90(rid, 1)

            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3,sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 7:

            puerto=x80.turn45(rid, 1)

            if rid == 0:
                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forward2(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
        if destiny == 8:
            puerto = x80.forward2(rid,0.01)
            print("H ola hermano")

            print(puerto)
            if rid == 0:

                sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1<35 or sensoresI0<18 or sensoresI2<18:
                    condicion=True

                    print("HOLA Falcao")
                    robot.face=face
                    return (condicion,robot.face)
                if sensoresI1>35:
                    condicion=False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)
            if rid == 1:
                sensoresI0, sensoresI1, sensoresI2,sensoresI3,sensoresI4,sensoresI5, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                sensores = (sensoresI0, sensoresI1, sensoresI2, sensoresI3, sensoresI4, sensoresI5)
                x=camino_Recorrido, sensores, condicion_hilo,lista_obstaculos_mandar
                print("condicion hilo",condicion_hilo)
                queue.put(x)
                if sensoresI1 < 35 or sensoresI0<18 or sensoresI2<18 :
                    condicion = True

                    print("HOLA Falcao")
                    robot.face = face
                    return (condicion, robot.face)
                if sensoresI1 > 35:
                    condicion = False
                    puerto=x80.forwardL(rid, 1)
                    robot.face = destiny
                    if hacer_loop==True:
                        while True:
                            sensoresI0, sensoresI1, sensoresI2, _, _, _, _, x1_robot_1, x2_robot_1, x3_robot_1, x4_robot_1 = udp.leer_ultrasonido_robot_1("192.168.0.100", puerto, rid)
                            if sensoresI1<5:
                                break
                    return (condicion, robot.face)