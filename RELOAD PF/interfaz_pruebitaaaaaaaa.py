# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intefaz2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from itertools import permutations

from PyQt5 import QtCore, QtGui, QtWidgets
from cell import Cell
from PyQt5.QtCore import pyqtSignal
from priorityqueque import PriorityQueue
from movement import movement
from robot import robot
from multiprocessing import Process,Queue,Manager,Lock
import multiprocessing.managers as m
import time
import time
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
condicional_borrar=False
grid=[]
cordenadas_lineas=[]
cordenadas_lineas2=[]
cordenadas_obs_encontrados=[]
cordenadas_obs_encontrados2=[]
tareas_organizadas_pintar_robotX80=[]
tareas_organizadas_pintar_robotX80Pro=[]
pintar=False

def caminillo_sin_pintar_ruta(end, start, came_from, condicion):
    current = end
    path = []
    path.append(current)
    while True:
        # correntito
        # previos
        previos = current
        # print(current.x)
        # print(current.y)
        # print(came_from)
        current = came_from[current]

        path.append(current)
        # print(current)
        if (current == start):
            x = path
            x.reverse()
            if condicion == False:
                x.pop(-1)

            # print(x)
            return x
def cojer_mejor_rutas_para_robot_caso_repetido( tareas, largo):
    print("ESTO ES YA PARA SACAR UN MEJOR OBSTACULO")
    if largo == 6:
        costo_temportal = 999
        A = [1, 2, 3,4,5]
        x = permutations(A, 5)
        # i=3
        for i in x:
            a, b, c,d,e = i
            print("ENTRO AL 4")
            # print(i)
            came_from1, cost_so_far1, success, has_been_next, end1, start1 = a_star(tareas[0], tareas[a])
            came_from2, cost_so_far2, success, has_been_next, end2, start2 = a_star(tareas[a], tareas[b])
            came_from3, cost_so_far3, success, has_been_next, end3, start3 = a_star(tareas[b], tareas[c])
            came_from4, cost_so_far4, success, has_been_next, end4, start4 = a_star(tareas[c], tareas[d])
            came_from5, cost_so_far5, success, has_been_next, end5, start5 = a_star(tareas[d], tareas[e])

            costo1 = sacar_costo_total(end1, start1, came_from1, False)
            costo2 = sacar_costo_total(end2, start2, came_from2, False)
            costo3 = sacar_costo_total(end3, start3, came_from3, False)
            costo4 = sacar_costo_total(end4, start4, came_from4, False)
            costo5 = sacar_costo_total(end5, start5, came_from5, False)
            print("")

            costo_ruta_combinacion = costo1 + costo2 + costo3+costo4+costo5
            print("")
            print(i)
            print("")
            print("costo de esta ruta")
            print(costo_ruta_combinacion)
            # print("Costo Ruta Combinacion")
            # print(costo_ruta_combinacion)
            if costo_ruta_combinacion < costo_temportal:
                costo_temportal = costo_ruta_combinacion
                print("")
                print("Costo Temporal")
                print(costo_temportal)
                print("Mejor ruta")
                print(" ")
                print(i)
                ruta_encontrada = i
                end_mejor_1 = end1
                end_mejor_2 = end2
                end_mejor_3 = end3
                end_mejor_4 = end4
                end_mejor_5 = end5

                #
                star_mejor_1 = start1
                star_mejor_2 = start2
                star_mejor_3 = start3
                star_mejor_4 = start4
                star_mejor_5 = start5
                #
                mejor_came_from_1 = came_from1
                mejor_came_from_2 = came_from2
                mejor_came_from_3 = came_from3
                mejor_came_from_4 = came_from4
                mejor_came_from_5 = came_from5
        ruta = []
        p5 = caminillo_sin_pintar_ruta(end_mejor_5, star_mejor_5, mejor_came_from_5, False)
        p4 = caminillo_sin_pintar_ruta(end_mejor_4, star_mejor_4, mejor_came_from_4, False)
        p3 = caminillo_sin_pintar_ruta(end_mejor_3, star_mejor_3, mejor_came_from_3, True)
        p2 = caminillo_sin_pintar_ruta(end_mejor_2, star_mejor_2, mejor_came_from_2, False)
        p1 = caminillo_sin_pintar_ruta(end_mejor_1, star_mejor_1, mejor_came_from_1, False)

        ruta.append(p1)
        ruta.append(p2)
        ruta.append(p3)
        ruta.append(p4)
        ruta.append(p5)
        return (ruta_encontrada, costo_temportal, ruta)
    elif largo == 5:
        costo_temportal = 999
        A = [1, 2, 3,4]
        x = permutations(A, 4)
        # i=3
        for i in x:
            a, b, c,d = i
            print("ENTRO AL 4")
            # print(i)
            came_from1, cost_so_far1, success, has_been_next, end1, start1 = a_star(tareas[0], tareas[a])
            came_from2, cost_so_far2, success, has_been_next, end2, start2 = a_star(tareas[a], tareas[b])
            came_from3, cost_so_far3, success, has_been_next, end3, start3 = a_star(tareas[b], tareas[c])
            came_from4, cost_so_far4, success, has_been_next, end4, start4 = a_star(tareas[c], tareas[d])
            costo1 = sacar_costo_total(end1, start1, came_from1, False)
            costo2 = sacar_costo_total(end2, start2, came_from2, False)
            costo3 = sacar_costo_total(end3, start3, came_from3, False)
            costo4 = sacar_costo_total(end4, start4, came_from4, False)
            print("")

            costo_ruta_combinacion = costo1 + costo2 + costo3+costo4
            print("")
            print(i)
            print("")
            print("costo de esta ruta")
            print(costo_ruta_combinacion)
            # print("Costo Ruta Combinacion")
            # print(costo_ruta_combinacion)
            if costo_ruta_combinacion < costo_temportal:
                costo_temportal = costo_ruta_combinacion
                print("")
                print("Costo Temporal")
                print(costo_temportal)
                print("Mejor ruta")
                print(" ")
                print(i)
                ruta_encontrada = i
                end_mejor_1 = end1
                end_mejor_2 = end2
                end_mejor_3 = end3
                end_mejor_4 = end4

                #
                star_mejor_1 = start1
                star_mejor_2 = start2
                star_mejor_3 = start3
                star_mejor_4 = start4
                #
                mejor_came_from_1 = came_from1
                mejor_came_from_2 = came_from2
                mejor_came_from_3 = came_from3
                mejor_came_from_4 = came_from4
        ruta = []
        p4 = caminillo_sin_pintar_ruta(end_mejor_4, star_mejor_4, mejor_came_from_4, False)
        p3 = caminillo_sin_pintar_ruta(end_mejor_3, star_mejor_3, mejor_came_from_3, True)
        p2 = caminillo_sin_pintar_ruta(end_mejor_2, star_mejor_2, mejor_came_from_2, False)
        p1 = caminillo_sin_pintar_ruta(end_mejor_1, star_mejor_1, mejor_came_from_1, False)

        ruta.append(p1)
        ruta.append(p2)
        ruta.append(p3)
        ruta.append(p4)

        return (ruta_encontrada, costo_temportal, ruta)
    elif largo == 4:
        costo_temportal = 999
        A = [1, 2, 3]
        x = permutations(A, 3)
        # i=3
        for i in x:
            a, b, c = i
            print("ENTRO AL 4")
            # print(i)
            came_from1, cost_so_far1, success, has_been_next, end1, start1 = a_star(tareas[0], tareas[a])
            came_from2, cost_so_far2, success, has_been_next, end2, start2 = a_star(tareas[a], tareas[b])
            came_from3, cost_so_far3, success, has_been_next, end3, start3 = a_star(tareas[b], tareas[c])
            costo1 = sacar_costo_total(end1, start1, came_from1, False)
            costo2 = sacar_costo_total(end2, start2, came_from2, False)
            costo3 = sacar_costo_total(end3, start3, came_from3, False)
            print("")

            costo_ruta_combinacion = costo1 + costo2 + costo3
            print("")
            print(i)
            print("")
            print("costo de esta ruta")
            print(costo_ruta_combinacion)
            # print("Costo Ruta Combinacion")
            # print(costo_ruta_combinacion)
            if costo_ruta_combinacion < costo_temportal:
                costo_temportal = costo_ruta_combinacion
                print("")
                print("Costo Temporal")
                print(costo_temportal)
                print("Mejor ruta")
                print(" ")
                print(i)
                ruta_encontrada = i
                end_mejor_1 = end1
                end_mejor_2 = end2
                end_mejor_3 = end3
                #
                star_mejor_1 = start1
                star_mejor_2 = start2
                star_mejor_3 = start3
                #
                mejor_came_from_1 = came_from1
                mejor_came_from_2 = came_from2
                mejor_came_from_3 = came_from3
        ruta = []
        p3 = caminillo_sin_pintar_ruta(end_mejor_3, star_mejor_3, mejor_came_from_3, True)
        p2 = caminillo_sin_pintar_ruta(end_mejor_2, star_mejor_2, mejor_came_from_2, False)
        p1 = caminillo_sin_pintar_ruta(end_mejor_1, star_mejor_1, mejor_came_from_1, False)

        ruta.append(p1)
        ruta.append(p2)
        ruta.append(p3)

        return (ruta_encontrada, costo_temportal, ruta)
    elif largo == 3:
        costo_temportal = 999
        A = [2, 3]
        x = permutations(A, largo - 1)
        print("tareas",tareas)
        for z in tareas:
            print((z.x,z.y))



        for i in x:
            a, b = i
            print("ENTRO ")
            print(i)
            came_from1, cost_so_far1, success, has_been_next, end1, start1 = a_star(tareas[0], tareas[a - 1])
            came_from2, cost_so_far2, success, has_been_next, end2, start2 = a_star(tareas[a - 1], tareas[b - 1])
            #print("camefrom1",came_from1)
            #print("camefrom2",came_from2)

            costo1 = sacar_costo_total(end1, start1, came_from1, False)
            costo2 = sacar_costo_total(end2, start2, came_from2, False)

            print("")
            print("Costo 1")
            print(costo1)
            print("")
            print("Costo 2")
            print(costo2)

            costo_ruta_combinacion = costo1 + costo2
            print("")
            print(i)
            print("")
            print("costo de esta ruta")
            print(costo_ruta_combinacion)
            # print("Costo Ruta Combinacion")
            # print(costo_ruta_combinacion)
            if costo_ruta_combinacion < costo_temportal:
                costo_temportal = costo_ruta_combinacion
                print("")
                print("Costo Temporal")
                print(costo_temportal)
                print("Mejor ruta")
                print(" ")
                print(i)
                ruta_encontrada = i
                end_mejor_1 = end1
                end_mejor_2 = end2

                #
                star_mejor_1 = start1
                star_mejor_2 = start2

                #
                mejor_came_from_1 = came_from1
                mejor_came_from_2 = came_from2
        ruta = []

        p2 = caminillo_sin_pintar_ruta(end_mejor_2, star_mejor_2, mejor_came_from_2, True)
        p1 = caminillo_sin_pintar_ruta(end_mejor_1, star_mejor_1, mejor_came_from_1, False)

        ruta.append(p1)
        ruta.append(p2)

        return (ruta_encontrada, costo_temportal, ruta)



    elif largo == 2:

        print("eNtraste al largo ==2")

        print(tareas)
        print(tareas[0].x, tareas[0].y)
        print(tareas[1].x, tareas[1].y)
        came_from1, cost_so_far1, success, has_been_next, end1, start1 = a_star(tareas[0], tareas[1])
        print(end1)
        print("Dicionario")
        # print(came_from1)
        print(success)

        costo1 = sacar_costo_total(end1, start1, came_from1, False)

        print("")
        print("Costo 1")
        print(costo1)

        end_mejor_1 = end1

        #
        star_mejor_1 = start1

        #
        mejor_came_from_1 = came_from1

        ruta = []
        ruta_encontrada = []
        p1 = caminillo_sin_pintar_ruta(end_mejor_1, star_mejor_1, mejor_came_from_1, True)

        ruta.append(p1)

        return (ruta_encontrada, costo1, ruta)




    elif largo == 1:

        pass
def sacar_costo_total( end, start, came_from, condicion):
    current = end
    print("CUrrent", current.x, current.y)
    path = []
    path.append(current)
    while True:
        # print(current)
        # print(came_from)

        current = came_from[current]
        print("PEDAZO")

        path.append(current)
        # print(current)
        if (current == start):
            x = path
            x.reverse()
            if condicion == False:
                x.pop(-1)
            return len(x)
def heuristic2( tile1, tile2):
    """
    Manhattan distance between two tiles.
    :param tile1: Tile
    :param tile2: Tile
    :return: int distance
    """
    (x1, y1) = (tile1.x, tile1.y)
    (x2, y2) = (tile2.x, tile2.y)
    return abs(x1 - x2) + abs(y1 - y2)
def a_star( start, end):
    # we NEED  START ,END RECTANGLE
    """
    A* Pathfinding algorithm. Takes a start tile and end tile, and uses
    their neighbour list to traverse.
    Uses the heapq queue in queues.py.
    :param start: Tile
    :param end: Tile
    :return: came_from, dictionary with all tiles as key, and where we came from (parent tile) as value.
             cost_so_far, dictionary with tiles as key, and their cost so far as value.
             success, True or False. If the algorithm found the end tile or not.
             has_been_next, list over tiles that has been considered as the next tile.
    """

    # saquemos los puntos
    start = start
    end = end
    end.wall=False

    caminito = []
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    has_been_next = []
    success = False
    while not frontier.empty():
        current = frontier.pop()
        # print("Current",current.x,current.y)
        # caminito.append(current)
        # print("ESTE ES EL CAMINITO")
        #    print(len(caminito))
        # print(current)

        # current.visit() pone lo del color

        if current == end:
            print("A* Pathfinder, successful.")
            success = True
            break

        for next_tile in current.neighbours:


    
                new_cost = cost_so_far[current] + next_tile.weight
                if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                    cost_so_far[next_tile] = new_cost
                    priority = new_cost + heuristic2(end, next_tile)
                    frontier.put(next_tile, priority)
                    came_from[next_tile] = current

    # print(cost_so_far)
    return came_from, cost_so_far, success, has_been_next, end, start
def sacar_datos_para_el_robot_2_parte(cordenadas_cuadros_1):
    print("POR LO MENOS AQUI")
    path_robot1, path_robot2,robotX80Tareas,robotX80ProTareas = sacar_datos_para_el_robot_1_parte(cordenadas_cuadros_1)
    print("POR LO MENOS AQUI 2")
    celditas_x_robot1 = []
    celditas_y_robot1 = []
    celditas_x_robot2 = []
    celditas_y_robot2 = []
    print("ROBOX80TAREAS DATOS1",robotX80Tareas)
    print("ROBOX80TAREASPro DATOS1",robotX80ProTareas)
    celdas_robot1 = []
    celdas_robot2 = []
    print(" ")
    print("los paths")
    print(path_robot1)
    print(path_robot2)
    cordenadas=[]
    cordenadas2=[]

    for path_cortados_pruebas in path_robot1:

        for idx, celda in enumerate(path_cortados_pruebas):
            print("entro alemnos")
            celditas_x_robot1.append(celda.y)

            celditas_y_robot1.append(celda.x)
            cordenadas.append((celda.y,celda.x))
            celdas_robot1.append(celda)

    for path_cortados_pruebas in path_robot2:

        for idx, celda in enumerate(path_cortados_pruebas):
            celditas_x_robot2.append(celda.y)
            celditas_y_robot2.append(celda.x)
            cordenadas2.append((celda.y, celda.x))
            celdas_robot2.append(celda)

    lista_celdidas_robot_1 = []
    lista_celdidas_robot_2 = []
    print("CELDITAS_x",celditas_x_robot1)
    print("CELDITAS_y", celditas_y_robot1)







    i = 0
    for idx, z in enumerate(celditas_x_robot1):
        x = celditas_x_robot1[idx]
        y = celditas_y_robot1[idx]

        lista_celdidas_robot_1.append((x, y))

        i += 1
    i = 0
    for idx, z in enumerate(celditas_x_robot2):
        x = celditas_x_robot2[idx]
        y = celditas_y_robot2[idx]

        lista_celdidas_robot_2.append((x,y))

        i += 1
    print("lista celditas1",lista_celdidas_robot_1)
    print("lista celditas2", lista_celdidas_robot_2)
    print("los muevo suave")

    return celditas_x_robot1, celditas_y_robot1, robotX80Tareas, celditas_x_robot2, celditas_y_robot2, robotX80ProTareas,cordenadas,cordenadas2


def sacar_datos_para_el_robot_1_parte(cordenadas_cuadros_1):
    #global pintar
    # print("Entraste")

    print(" ")
    print("robot_1 START")
    # print(R1)
    print(" ")
    print(" ")
    print("robot_2 START")
    # print(R2)
    print(" ")


    camino_organizado_robotX80 = []
    camino_organizado_robotX80Pro = []
    robotX80Tareas=[]
    robotX80ProTareas = []
    punto_inicial_robotstandart=None
    punto_inicial_robotPro=None
    # para Robot 1
    print("hello")
    print(cordenadas_cuadros_1)
    i=0
    #Asignaos
    # for x  in cordenadas_cuadros_1["start"]:
    #     if i==0:
    #         camino_organizado_robotX80.append(x)
    #         punto_inicial_X80=x
    #
    #
    #     if i==1:
    #         camino_organizado_robotX80Pro.append(x)
    #         punto_inicial_X80Pro=x
    #         break
    #     i+=1
    #
    # for x in cordenadas_cuadros_1["start"]:
    #     if x is not  punto_inicial_X80Pro and x is not punto_inicial_X80:
    #         # ahora vamos a comprar las heuristica de cada punto partida con X
    #         distancia_x80Pro = heuristic2(punto_inicial_X80Pro,x)
    #         distancia_x80 = heuristic2( punto_inicial_X80,x)
    #         print("Celda", x)
    #         print("Distancia x80", distancia_x80)
    #         print("Distancia X80 Pro", distancia_x80Pro)
    #         if distancia_x80 < distancia_x80Pro:
    #             camino_organizado_robotX80.append(x)
    #             robotX80Tareas.append((x.y,x.x))
    #         elif distancia_x80Pro < distancia_x80:
    #             camino_organizado_robotX80Pro.append(x)
    #             robotX80ProTareas.append((x.y,x.x))
    #         elif distancia_x80Pro == distancia_x80:
    #             camino_organizado_robotX80Pro.append(x)
    #             robotX80ProTareas.append((x.y,x.x))
    #
    # if len(camino_organizado_robotX80Pro) == 0 and len(camino_organizado_robotX80) > 1:
    #     camino_organizado_robotX80Pro.append(camino_organizado_robotX80.pop(0))
    #     robotX80ProTareas.append(robotX80Tareas.pop(0))
    #
    # if len(camino_organizado_robotX80)==0 and len(camino_organizado_robotX80Pro)>1:
    #     camino_organizado_robotX80.append(camino_organizado_robotX80Pro.pop(0))
    #     robotX80Tareas.append(robotX80ProTareas.pop(0))




    for x in cordenadas_cuadros_1["start"]:
        if x.y<=4:
            camino_organizado_robotX80.append(x)
        if x.y>4:

            camino_organizado_robotX80Pro.append(x)
    #
    #
    print("camino_organizado_robotX80",camino_organizado_robotX80)
    print("camino_organizado_robotX80Pro",camino_organizado_robotX80)
    #
    #
    for x in cordenadas_cuadros_1["start"]:
        if x.y<=4:
            robotX80Tareas.append((x.y, x.x))
        if x.y>4:
            robotX80ProTareas.append((x.y,x.x))



    print("Resultados2")
    print("robotX80Tareas",robotX80Tareas)
    print(" ")
    print("robotX80ProTareas",robotX80ProTareas)










    mejor_ruta1, costo_mejor_ruta1, ruta1 = cojer_mejor_rutas_para_robot_caso_repetido(camino_organizado_robotX80,len(camino_organizado_robotX80))
    mejor_ruta2, costo_mejor_ruta2, ruta2 = cojer_mejor_rutas_para_robot_caso_repetido(camino_organizado_robotX80Pro,len(camino_organizado_robotX80Pro))
    print("aqui paso")
    return ruta1, ruta2,robotX80Tareas,robotX80ProTareas

class WorkerThread(QtCore.QObject):

    signalExample = QtCore.pyqtSignal(tuple)


    def __init__(self,robot_x80_x , robot_x80_y ,robot_x80_tareas,RoboX80meta,robot_x80_pro_x , robot_x80_pro_y ,robot_x80_pro_tareas,RoboX80Prometa,robot_x80,robot_x80_pro):
        super().__init__()
        #self.grid=Grid_compartida
        self.job_input = None
        self.queue_robot1=Queue()
        self.queue_robot2 = Queue()
        self.i=0
        self.robot_x80_x=robot_x80_x
        self.robot_x80_y=robot_x80_y
        self.robot_x80_tareas=robot_x80_tareas
        self.robotX80meta=RoboX80meta
        self.robot_x80_pro_x=robot_x80_pro_x
        self.robot_x80_pro_y=robot_x80_pro_y
        self.robot_x80_pro_tareas=robot_x80_pro_tareas
        self.RoboX80Prometa=RoboX80Prometa
        self.robot_x80=robot_x80
        self.robot_x80_pro=robot_x80_pro
        self.dicionario_grid={}



    def crear_Grid_temporal_para_el_proceso(self):
        global grid

        for col in range(16):
            for row in range(16):
                cell=grid[col][row]

                self.dicionario_grid[(cell.x,cell.y)]=[cell.x,cell.y,cell.weight,cell.start,cell.wall,cell.end]

        return self.dicionario_grid
    @QtCore.pyqtSlot()
    def run(self):
        dicionario_grid=self.crear_Grid_temporal_para_el_proceso()
        print("paso aqui")
        print("dicionario_grid",dicionario_grid)


        p1 = Process(target=proceso_llegar_meta, args=(self.robot_x80_x,self.robot_x80_y,self.queue_robot1,self.robot_x80_tareas,self.robot_x80,self.robotX80meta,dicionario_grid) )#ACTUALIZARA LOS SLIDERS DE ROBOTX80

        p1.start()


        while True:
            #print("ENTRO AL WHILE")

            msg = self.queue_robot1.get()#aqui actualizo el thread
            #msg2 = self.queue_robot2.get()  # aqui actualizo el thread
            #print("msg",msg)
            time.sleep(0.2)
            self.signalExample.emit(msg)#manda la senal al proceso principal
            #self.signalExample2.emit(msg2)  # manda la senal al proceso principal
            #self.thread.wait
            if msg[2]==True :
                print("Entro al Break")
                break

                #si llego a la meta se sale
                 #break
class WorkerThread2(QtCore.QObject):


    signalExample2 = QtCore.pyqtSignal(tuple)

    def __init__(self,robot_x80_x , robot_x80_y ,robot_x80_tareas,RoboX80meta,robot_x80_pro_x , robot_x80_pro_y ,robot_x80_pro_tareas,RoboX80Prometa,robot_x80,robot_x80_pro):
        super().__init__()
        #self.grid=Grid_compartida
        self.job_input = None
        self.queue_robot1=Queue()
        self.queue_robot2 = Queue()
        self.i=0
        self.robot_x80_x=robot_x80_x
        self.robot_x80_y=robot_x80_y
        self.robot_x80_tareas=robot_x80_tareas
        self.robotX80meta=RoboX80meta
        self.robot_x80_pro_x=robot_x80_pro_x
        self.robot_x80_pro_y=robot_x80_pro_y
        self.robot_x80_pro_tareas=robot_x80_pro_tareas
        self.RoboX80Prometa=RoboX80Prometa
        self.robot_x80=robot_x80
        self.robot_x80_pro=robot_x80_pro
        self.dicionario_grid={}



    def crear_Grid_temporal_para_el_proceso(self):
        global grid

        for col in range(16):
            for row in range(16):
                cell=grid[col][row]

                self.dicionario_grid[(cell.x,cell.y)]=[cell.x,cell.y,cell.weight,cell.start,cell.wall,cell.end]

        return self.dicionario_grid
    @QtCore.pyqtSlot()
    def run(self):
        dicionario_grid=self.crear_Grid_temporal_para_el_proceso()
        print("paso aqui")
        print("dicionario_grid",dicionario_grid)



        p2 = Process(target=proceso_llegar_meta, args=(self.robot_x80_pro_x, self.robot_x80_pro_y, self.queue_robot2, self.robot_x80_pro_tareas, self.robot_x80_pro, self.RoboX80Prometa,dicionario_grid))  # ACTUALIZARA LOS SLIDERS DE ROBOTX80

        p2.start()

        while True:
            #print("ENTRO AL WHILE")


            msg2 = self.queue_robot2.get()  # aqui actualizo el thread
            #print("msg",msg)
            time.sleep(0.2)#manda la senal al proceso principal
            self.signalExample2.emit(msg2)  # manda la senal al proceso principal
            #self.thread.wait
            if  msg2[2]==True:
                print("Entro al Break")
                break

                #si llego a la meta se sale
                 #break


#son las funciones a llamar

def movimiento_robot(queue,robot_x80, robot_x80_x, robot_x80_y,robot_x80_tareas,lista_obstaculos_mandar,camino_Recorrido):
    condicion, rob, lista_de_tareas, donde_encontro_obstaculo = movement(queue,robot_x80, robot_x80_x, robot_x80_y,robot_x80_tareas,lista_obstaculos_mandar,camino_Recorrido)
    return (condicion, rob, lista_de_tareas, donde_encontro_obstaculo)



def proceso_llegar_meta(robot_x80_x,robot_x80_y,queue,robot_x80_tareas,robot_x80,robotX80meta,dicionario_grid):

    #ya llegan la primera ejecuion de A*
    #print("entro al proceso llegar")
    #print("robot_x80_X",robot_x80.x)
    #print("robot_x80_Y", robot_x80.y)
    #print("robot_x80 face",robot_x80.face)
    #print("hello llegaste aqui")
    #print("META ROBOT",robotX80meta)
    lista_obstaculos_mandar=[]
    lista_obstaculos_mandar.append((None,None))
    camino_Recorrido=[]
    condicion, rob, lista_de_tares, donde_encontro_obstaculo = movimiento_robot(queue,robot_x80, robot_x80_x, robot_x80_y,robot_x80_tareas,lista_obstaculos_mandar,camino_Recorrido=None)
    #anadimos el obstaculo donde se encontro si encontro claro esta
    #print("dicicionario grid",dicionario_grid)
    #print("LO QUE DEBO VER")
    #print("LISTA De Tareas", lista_de_tares)
    #print("donde encontro obstaculo", donde_encontro_obstaculo)
    #print("ROBOTX80 META",robotX80meta)
    if donde_encontro_obstaculo!=False:
        #print("ENTRO AQUI PAPITO LINDO")
        lista_obstaculos_mandar.pop(0)
        lista_obstaculos_mandar.append(donde_encontro_obstaculo)
    # condicion, rob, lista_de_tares, donde_encontro_obstaculo=list(x)
    # si el man detecta que Llego hasta el Final no entra EN el while
    # lo Contrario entrara


    #
    robot_x80=rob
    #print("rob.x",robot_x80.x)
    #print("rob.y", robot_x80.y)
    #print("robot.face",robot_x80.face)
    grid=[]
    #ya creamos el grid temporal
    for column in range(16):
        line = []
        for row in range(16):
            line.append(Cell(column, row, 40, True))

        grid.append(line)
    #print(len(grid))
    #metemos los datos del grid que se envio al proceso
    for k,v in dicionario_grid.items():
        x,y=k
        #print("value",v)

        grid[y][x].start=v[3]
        grid[y][x].weight=v[2]
        grid[y][x].wall =v[4]
        grid[y][x].end=v[5]
    #ahora le ponmos los vecinos
        for column in range(16):
            for row in range(16):
                grid[column][row].neigh(grid)

    #print("esta condicion robotX80meta != lista_de_tares[0]",robotX80meta != lista_de_tares[0])

    while robotX80meta != lista_de_tares[0]:
        #print("se repitio")
        celdas_x1 = []
        celdas_y1 = []

        # print(objecto_referencia_compartido_entre_procesos_Grid)
        # print(objecto_referencia_compartido_entre_procesos_Grid.geter())



        if condicion == True:

            #print("SE RECIBIO OBSTACULO HAGAMOS TODO DE NUEVO")
            #print(len(lista_de_tares))
            lista_celdas_tareas_obstaculo = []
            # cojer_mejor_rutas_para_robot_caso_repetido(items[0][2])
            x_X, y_Y = donde_encontro_obstaculo  # es donde se encontro el obstaculo
            #print("DONde encontro obstaculo",donde_encontro_obstaculo)
            #print(x_X, y_Y)
            # le agregamos pesso al obstaculo
            grid[y_Y][x_X].weight+=20
            grid[y_Y][x_X].wall= True


            for z in lista_de_tares:
                x, y = z
                #print("lista de tareas XD")
                #print(x, y)
                lista_celdas_tareas_obstaculo.append(grid[y][x])  # anadimos las celdas para mandarlas
            #print(" ")
            #print("lista_celdas_tareas_obstaculo",lista_celdas_tareas_obstaculo)
            #print("Lista de OBs")
            #print("len(lista_de_tares)",len(lista_de_tares))

                #print(celdas.x, celdas.y)
                #print(" ")

            ruta_encontrada, costo_temportal, ruta = cojer_mejor_rutas_para_robot_caso_repetido(lista_celdas_tareas_obstaculo, len(lista_de_tares))
            #print(costo_temportal)
            #print(ruta_encontrada)
            #print(ruta)

            celditas_x_robot1 = []
            celditas_y_robot1 = []


            #print(" ")
            #print("los paths")
            #print(ruta)


            for path_cortados_pruebas in ruta:

                for celda in  (path_cortados_pruebas):
                    #print("entro alemnos")
                    celditas_x_robot1.append(celda.y)#las rx A*
                    celditas_y_robot1.append(celda.x)#las ry A*

            celditas_x_robot1.pop(0)  # las rx A*
            celditas_y_robot1.pop(0)  # las ry A*


            #print("celditas_x_robot1",celditas_x_robot1)
            #print("celditas_y_robot1",celditas_y_robot1)
            condicion, robo1, lista_de_tares, donde_encontro_obstaculo = movimiento_robot(queue,robot_x80, celditas_x_robot1, celditas_y_robot1,lista_de_tares,lista_obstaculos_mandar,camino_Recorrido)
            #x80_robot1, celditas_x_robot1, celditas_y_robot1, tareas
            robot_x80 = robo1
            # items = [Cola_Robot1.get_nowait() for _ in range(Cola_Robot1.qsize())]
            #print("ESTO ES JUSTO DESPUES DEL PROCESO")
            #print(condicion, robot_x80, lista_de_tares, donde_encontro_obstaculo)
            #print(robot_x80)
            #print(robot_x80.x)
            #print(robot_x80.y)
            #print(robot_x80.face)
            if donde_encontro_obstaculo != False:
                lista_obstaculos_mandar.append(donde_encontro_obstaculo)
            #print("LLEGO HASTA LA META SATISFACTORIAMENTE del robot 1")
    print("se completo el proceso satifactoria mente")


class framesito(QtWidgets.QFrame):

    def __init__(self,selfcito):

        self.x=0
        self.y=0
        self.y_presionado=0
        self.x_presionado=0
        self.ruta=[]
        self.cordenadas_cuadros2 = []
        self.cordenadas_obs=[]
        self.posiciones_robot1={}
        self.posiciones_robot2={}
        self.cordenadas_cuadros1=[]
        self.obs = {}
        self.obs['obs']=[]
        self.cond=False
        self.posiciones_robot1["start"] = []
        self.posiciones_robot2["start"] = []

        super(framesito, self).__init__(selfcito)
        self.setMouseTracking(True)
        self.setGeometry(QtCore.QRect(0, 0, 655, 655))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("CellGrid")
        self.append_Cells()
        self.establecer_neigh(16,16)
        self.qp= QtGui.QPainter(self)





    def enterEvent(self, event):
        pass
    def mouseMoveEvent(self, e):
        global condicional_borrar


        #print("esto es lo que vale",condicional_borrar)
        self.cond=condicional_borrar

        x = e.x()
        y = e.y()
        x = (x//40)
        y = (y//40)
        self.x=x
        self.y=y
        X = 10 + (x + 1 - 1) * 40

        Y = 10 + (y + 1 - 1) * 40
        #print(X,Y)
        #print("esto es COND",self.cond)
        if self.cond:
            self.update()

    def paintEvent(self, e):




        self.qp.begin(self)
        self.drawRectangles(self.qp)


        #print("hello")
        #si se pone resetear los cuadros
        if self.cond:#se borra las metas pero no los obstaculos
            self.resetear_todo_las_celdas()
        else:
            self.draw_obs_robots()

            self.draw_cuadros_robot1()
            #self.draw_cuadros_robot2()
            self.dibujar_lineas()
            self.dibujar_lineas2()
            self.draw_obs_robots_encontraods()
            self.draw_obs_robots_encontraods2()


        #miramos si undimos el shortcut



        self.qp.end()
    def resetear_todo_las_celdas(self):
        global grid,cordenadas_lineas,cordenadas_lineas2,cordenadas_obs_encontrados2,cordenadas_obs_encontrados
        cordenadas_lineas=[]
        cordenadas_lineas2=[]
        for col in range(16):
            for row in range(16):
                cell=grid[col][row]
                if cell.wall:
                    cell.weight=10
                else:
                    cell.weight=1
                #cell.weight=1
                cell.start = False
                cell.wall = False
                cell.end = False
        self.cordenadas_cuadros1=[]
        self.cordenadas_cuadros2=[]
        #los obstaculos no se borran quedan fijos
        self.posiciones_robot1['start']=[]
        self.posiciones_robot2['start'] = []
        cordenadas_obs_encontrados2=[]
        cordenadas_obs_encontrados=[]
        self.update()

    def dibujar_lineas(self):
        global cordenadas_lineas


        #self.drawLine(200, 200, 250, 250)
        for index,value in  enumerate(cordenadas_lineas):
            #print("VALUE",value)
            #print("INDEX",index)
            #print("Largo cordenadas_lineas",len(cordenadas_lineas))

            pen = QPen(Qt.black , 1, Qt.SolidLine)
            self.qp.setPen(pen)
            x,y=value
            #print("AQUI ESTUVO")
            #print(index)
            X=10+(x+1-1)*40
            X+=20

            Y=10+(y+1-1)*40
            Y+=20
            #print("INDEX", index)
           # print("  ")
            #print("X",X)
            #print("Y",Y)
            #print("")


            if index <= len(cordenadas_lineas):
                if index == len(cordenadas_lineas)-1:
                    #print("Entro al if 2")
                    #print("xtemporal,ytemporal",x_temporal,y_temporal)
                    #print(" X,Y",X,Y)
                    self.qp.drawLine(x_temporal, y_temporal, X, Y)


                if index>0:
                   # print("Entro al if 1")
                    #self.qp.drawLine(x1,y1,x2,y2)
                    self.qp.drawLine(x_temporal, y_temporal, X, Y)

            x_temporal=10+(x+1-1)*40
            x_temporal+=20
            y_temporal=10+(y+1-1)*40
            y_temporal+=20
            #print(" ")
            #print("x_Temporal",x_temporal)
            #print("y_temporal",y_temporal)
            #print(" ")
    def dibujar_lineas2(self):
        global cordenadas_lineas2


        #self.drawLine(200, 200, 250, 250)
        for index,value in  enumerate(cordenadas_lineas2):
            #print("VALUE",value)
            #print("INDEX",index)
            #print("Largo cordenadas_lineas",len(cordenadas_lineas))

            pen = QPen(Qt.black , 1, Qt.SolidLine)
            self.qp.setPen(pen)
            x,y=value
            #print("AQUI ESTUVO")
            #print(index)
            X=10+(x+1-1)*40
            X+=20

            Y=10+(y+1-1)*40
            Y+=20
            #print("INDEX", index)
           # print("  ")
            #print("X",X)
            #print("Y",Y)
            #print("")


            if index <= len(cordenadas_lineas2):
                if index == len(cordenadas_lineas2)-1:
                    #print("Entro al if 2")
                    #print("xtemporal,ytemporal",x_temporal,y_temporal)
                    #print(" X,Y",X,Y)
                    self.qp.drawLine(x_temporal, y_temporal, X, Y)


                if index>0:
                   # print("Entro al if 1")
                    #self.qp.drawLine(x1,y1,x2,y2)
                    self.qp.drawLine(x_temporal, y_temporal, X, Y)

            x_temporal=10+(x+1-1)*40
            x_temporal+=20
            y_temporal=10+(y+1-1)*40
            y_temporal+=20
            #print(" ")
            #print("x_Temporal",x_temporal)
            #print("y_temporal",y_temporal)
            #print(" ")

    def draw_cuadros_robot1(self):
        for x,y in self.cordenadas_cuadros1:
            #print("cuadros robot1")
            #print((x,y))
            if x<=4:
                self.qp.setBrush(QtGui.QColor(255, 80, 0, 160))
                X=10+(x+1-1)*40
                Y=10+(y+1-1)*40
                self.qp.drawRect(X, Y , 40, 40)
            elif x>4:
                self.qp.setBrush(QtGui.QColor(50, 80, 0, 160))
                X = 10 + (x + 1 - 1) * 40
                Y = 10 + (y + 1 - 1) * 40
                self.qp.drawRect(X, Y, 40, 40)




        # for x,y in self.cordenadas_cuadros1:
        #     #print("cuadros robot1")
        #     #print((x,y))
        #     self.qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        #     X=10+(x+1-1)*40
        #     Y=10+(y+1-1)*40
        #     self.qp.drawRect(X, Y , 40, 40)
    # def draw_cuadros_robot2(self):
    #
    #     for x,y in self.cordenadas_cuadros2:
    #         #print("cuadros robot2")
    #         #print((x,y))
    #         self.qp.setBrush(QtGui.QColor(50, 80, 0, 160))
    #         X=10+(x+1-1)*40
    #         Y=10+(y+1-1)*40
    #         self.qp.drawRect(X, Y , 40, 40)
    def draw_obs_robots(self):
        global grid
        for x,y in self.cordenadas_obs:
            #print("cuadros robot2")
            #print((x,y))

            self.qp.setBrush(QtGui.QColor(0, 0, 0, 160))
            X=10+(x+1-1)*40
            Y=10+(y+1-1)*40
            self.qp.drawRect(X, Y , 40, 40)

    def draw_obs_robots_encontraods(self):
        global cordenadas_obs_encontrados,grid
        if (None,None) in cordenadas_obs_encontrados:
            pass
        else:
            for x,y in cordenadas_obs_encontrados:
                #print("cuadros robot2")
                #print((x,y))
                grid[y][x].weight = 10
                #grid[y][x].wall=True
                self.qp.setBrush(QtGui.QColor(0, 0, 0, 160))
                X=10+(x+1-1)*40
                Y=10+(y+1-1)*40
                self.qp.drawRect(X, Y , 40, 40)
    def draw_obs_robots_encontraods2(self):
        global cordenadas_obs_encontrados2,grid
        if (None,None) in cordenadas_obs_encontrados2:
            pass
        else:
            for x,y in cordenadas_obs_encontrados2:
                grid[y][x].weight=10
                #print("cuadros robot2")
                #print((x,y))

                self.qp.setBrush(QtGui.QColor(0, 0, 0, 160))
                X=10+(x+1-1)*40
                Y=10+(y+1-1)*40
                self.qp.drawRect(X, Y , 40, 40)
    # CUADRICULA:

    def drawRectangles(self, qp):

        for col in range(10, 640, 40):
            for row in range(10, 640, 40):
                qp.drawRect(col, row, 40, 40)
            #print("valor de COL", col)


    def append_Cells(self):
        global grid

        for column in range(16):
            line = []

            for row in range(16):
                # print("col " + str(column))
                # print("row " + str(row))
                line.append(Cell( column, row, 40, True))

            grid.append(line)
        print(len(grid))


    def establecer_neigh(self,columnnumberr,rownumber):
        global grid
        # add neighbors

        for column in range(columnnumberr):
            for row in range(rownumber):
                grid[column][row].neigh(grid)


    def mousePressEvent(self, event: QtGui.QMouseEvent):
        global grid

        self.x_presionado=self.x
        self.y_presionado=self.y
        if self.x_presionado < 16 and self.y_presionado < 16:

            cell = grid[self.y_presionado][self.x_presionado]



            if event.button() == QtCore.Qt.LeftButton:
                cell.start = not cell.start


                if cell.start==False:#que se dibuje
                    if (self.x_presionado,self.y_presionado) in self.cordenadas_cuadros1:
                        #osea si ya esta el cuadro pintado y undo denuevo en ese espacio deberia borrarse
                        index=self.cordenadas_cuadros1.index((self.x_presionado,self.y_presionado))
                        self.cordenadas_cuadros1.pop(index)

                        #self.posiciones_robot1={ k:( None if cell is v else v) for (k,v) in self.posiciones_robot1.items() }
                        #print(self.posiciones_robot1)

                        for g in self.posiciones_robot1.values():
                            print(g)
                            v=g

                        print("este el valor DE V",v)
                        if cell in v:
                            index=v.index(cell)
                            v.pop(index)
                        self.posiciones_robot1["start"]=v
                        print(self.posiciones_robot1)



                        #tambien tenemos que borrarlos del dicionario

                elif cell.start==True and (self.x_presionado,self.y_presionado) not in self.cordenadas_cuadros2:#osea que todavia no es una start osea el cuadro esta en blanco
                    print("Esto es el Click IZQUIERDO",self.x,self.y)


                    self.posiciones_robot1['start'].append(cell)
                    cordenada=(self.x_presionado,self.y_presionado)
                    self.cordenadas_cuadros1.append(cordenada)
                    print(self.posiciones_robot1)
                self.update()




            # elif event.button() == QtCore.Qt.RightButton:
            #     cell.start = not cell.start
            #
            #
            #
            #
            #     if cell.start==False:#que se dibuje
            #         if (self.x_presionado,self.y_presionado) in self.cordenadas_cuadros2:
            #             #osea si ya esta el cuadro pintado y undo denuevo en ese espacio deberia borrarse
            #             index=self.cordenadas_cuadros2.index((self.x_presionado,self.y_presionado))
            #             self.cordenadas_cuadros2.pop(index)
            #
            #             for g in self.posiciones_robot2.values():
            #                 print(g)
            #                 v=g
            #
            #             print("este el valor DE V",v)
            #             if cell in v:
            #                 index=v.index(cell)
            #                 v.pop(index)
            #             self.posiciones_robot2["start"]=v
            #             print(self.posiciones_robot2)
            #
            #     elif cell.start==True and (self.x_presionado,self.y_presionado) not in self.cordenadas_cuadros1 :#osea que todavia no es una start osea el cuadro esta en blanco
            #         print("Esto es el Click IZQUIERDO",self.x,self.y)
            #
            #         self.posiciones_robot2['start'].append(cell)
            #         cordenada=(self.x_presionado,self.y_presionado)
            #         self.cordenadas_cuadros2.append(cordenada)
            #         print(self.posiciones_robot2)
            #     self.update()

            elif event.button() == QtCore.Qt.RightButton:

                cell.wall = not cell.wall

                if cell.wall==False:#que se dibuje
                    if (self.x_presionado,self.y_presionado) in self.cordenadas_obs:
                        #osea si ya esta el cuadro pintado y undo denuevo en ese espacio deberia borrarse
                        index=self.cordenadas_obs.index((self.x_presionado,self.y_presionado))
                        self.cordenadas_obs.pop(index)

                        #self.posiciones_robot1={ k:( None if cell is v else v) for (k,v) in self.posiciones_robot1.items() }
                        #print(self.posiciones_robot1)

                        for g in self.obs.values():
                            print(g)
                            v=g

                        print("este el valor DE V",v)
                        if cell in v:
                            index=v.index(cell)
                            v.pop(index)
                        self.obs["obs"]=v
                        print(self.obs)
                        #le cambio el peso si se cambia a que no es obstaculo
                        cell.weight=1
                        cell.wall=False


                        #tambien tenemos que borrarlos del dicionario

                elif cell.wall==True and (self.x_presionado,self.y_presionado) not in self.cordenadas_cuadros1 and (self.x_presionado,self.y_presionado) not in self.cordenadas_cuadros2 :#osea que todavia no es una start osea el cuadro esta en blanco
                    print("Esto es el Click IZQUIERDO",self.x,self.y)


                    self.obs['obs'].append(cell)
                    cordenada=(self.x_presionado,self.y_presionado)
                    self.cordenadas_obs.append(cordenada)
                    print(self.obs)
                    cell.weight+=10

                self.update()


                print("Esto es el Click MITAD", self.x, self.y)






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setGeometry(0,0,1400,1400)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(100, 670, 121, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Run.setIcon(icon1)
        self.Run.setObjectName("Run")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(240, 670, 91, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete.setIcon(icon2)
        self.Delete.setObjectName("Delete")
        #GRIDCITO

        #self.CellGrid = QtWidgets.QFrame(self.centralwidget)
        #self.CellGrid.setGeometry(QtCore.QRect(10, 10, 401, 351))
        #self.CellGrid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.CellGrid.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.CellGrid.setObjectName("CellGrid")

        self.CellGrid=framesito(self.centralwidget)
        self.CellGrid.setObjectName("CellGrid")
        self.cordenadas_cuadros_1=self.CellGrid.cordenadas_cuadros1
        self.cordenadas_cuadros_2 = self.CellGrid.cordenadas_cuadros2
        self.posiciones_robot1=self.CellGrid.posiciones_robot1
        self.posiciones_robot2 = self.CellGrid.posiciones_robot2


        #self.Run.pressed.connect()

        # conectar a boton run
        self.Run.pressed.connect(self.moverlos_suave)


        #establecemos un timer para que se ejecute la funcion cada 0.4 segundos

        #self.timer.setInterval(milliseconds)
        #self.timer.timeout.connect(self.read_data)


        self.X80Group = QtWidgets.QGroupBox(self.centralwidget)
        self.X80Group.setGeometry(QtCore.QRect(660, 400, 641, 331))
        self.X80Group.setObjectName("X80Group")
        self.label_8 = QtWidgets.QLabel(self.X80Group)
        self.label_8.setGeometry(QtCore.QRect(40, 20, 161, 151))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Nx80.jpg"))
        self.label_8.setObjectName("label_8")
        self.lcdX80 = QtWidgets.QLCDNumber(self.X80Group)
        self.lcdX80.setGeometry(QtCore.QRect(280, 90, 64, 23))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.lcdX80.setFont(font)
        self.lcdX80.setStyleSheet("background-color:green")
        self.lcdX80.setObjectName("lcdX80")
        self.label_10 = QtWidgets.QLabel(self.X80Group)
        self.label_10.setGeometry(QtCore.QRect(250, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.X80Group)
        self.label_9.setGeometry(QtCore.QRect(260, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.camera_sensorsX80_Group = QtWidgets.QGroupBox(self.X80Group)
        self.camera_sensorsX80_Group.setGeometry(QtCore.QRect(380, 50, 231, 171))
        self.camera_sensorsX80_Group.setObjectName("camera_sensorsX80_Group")
        self.groupBox_5 = QtWidgets.QGroupBox(self.camera_sensorsX80_Group)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 211, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.cameraX80On = QtWidgets.QPushButton(self.groupBox_5)
        self.cameraX80On.setGeometry(QtCore.QRect(0, 30, 91, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraX80On.setIcon(icon3)
        self.cameraX80On.setObjectName("cameraX80On")
        self.cameraX80Off = QtWidgets.QPushButton(self.groupBox_5)
        self.cameraX80Off.setGeometry(QtCore.QRect(100, 30, 91, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("OFF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraX80Off.setIcon(icon4)
        self.cameraX80Off.setObjectName("cameraX80Off")
        self.groupBox_4 = QtWidgets.QGroupBox(self.camera_sensorsX80_Group)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 211, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.sensorX80On = QtWidgets.QPushButton(self.groupBox_4)
        self.sensorX80On.setGeometry(QtCore.QRect(0, 30, 91, 23))
        self.sensorX80On.setIcon(icon3)
        self.sensorX80On.setObjectName("sensorX80On")
        self.sensorX80Off = QtWidgets.QPushButton(self.groupBox_4)
        self.sensorX80Off.setGeometry(QtCore.QRect(100, 30, 91, 23))
        self.sensorX80Off.setIcon(icon4)
        self.sensorX80Off.setObjectName("sensorX80Off")
        self.sensorsX80_Group = QtWidgets.QGroupBox(self.X80Group)
        self.sensorsX80_Group.setGeometry(QtCore.QRect(10, 230, 609, 80))
        self.sensorsX80_Group.setObjectName("sensorsX80_Group")
        self.Ux80_1 = QtWidgets.QSlider(self.sensorsX80_Group)
        self.Ux80_1.setGeometry(QtCore.QRect(20, 50, 160, 22))
        self.Ux80_1.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80_1.setObjectName("Ux80_1")
        self.Ux80_1.setMaximum(255)
        self.Ux80_1.setMinimum(0)
        self.Ux80_1.setTickInterval(50)

        self.labelslrobotx80_1 = QtWidgets.QLabel(self.sensorsX80_Group)
        self.labelslrobotx80_1.setGeometry(QtCore.QRect(190, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80_1.setFont(font)
        self.labelslrobotx80_1.setObjectName("labelslrobotx80_1")
        self.Ux80_2 = QtWidgets.QSlider(self.sensorsX80_Group)
        self.Ux80_2.setGeometry(QtCore.QRect(220, 50, 160, 22))
        self.Ux80_2.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80_2.setObjectName("Ux80_2")
        self.Ux80_2.setMaximum(255)
        self.Ux80_2.setMinimum(0)
        self.Ux80_2.setTickInterval(50)

        self.labelslrobotx80_2 = QtWidgets.QLabel(self.sensorsX80_Group)
        self.labelslrobotx80_2.setGeometry(QtCore.QRect(384, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80_2.setFont(font)
        self.labelslrobotx80_2.setObjectName("labelslrobotx80_2")
        self.label = QtWidgets.QLabel(self.sensorsX80_Group)
        self.label.setGeometry(QtCore.QRect(250, 30, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.sensorsX80_Group)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Ux80_3 = QtWidgets.QSlider(self.sensorsX80_Group)
        self.Ux80_3.setGeometry(QtCore.QRect(410, 50, 160, 22))
        self.Ux80_3.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80_3.setObjectName("Ux80_3")
        self.Ux80_3.setMaximum(255)
        self.Ux80_3.setMinimum(0)
        self.Ux80_3.setTickInterval(50)

        self.labelslrobotx80_3 = QtWidgets.QLabel(self.sensorsX80_Group)
        self.labelslrobotx80_3.setGeometry(QtCore.QRect(570, 50, 23, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80_3.setFont(font)
        self.labelslrobotx80_3.setObjectName("labelslrobotx80_3")
        self.label_4 = QtWidgets.QLabel(self.sensorsX80_Group)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.X80PROGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.X80PROGroup.setGeometry(QtCore.QRect(660, 0, 661, 401))
        self.X80PROGroup.setObjectName("X80PROGroup")

        self.label_7 = QtWidgets.QLabel(self.X80PROGroup)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 231, 221))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Nx80pro.jpg"))
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.label_23 = QtWidgets.QLabel(self.X80PROGroup)
        self.label_23.setGeometry(QtCore.QRect(210, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.X80PROGroup)
        self.label_24.setGeometry(QtCore.QRect(200, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lcdX80pro = QtWidgets.QLCDNumber(self.X80PROGroup)
        self.lcdX80pro.setGeometry(QtCore.QRect(250, 150, 64, 23))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        self.lcdX80pro.setFont(font)
        self.lcdX80pro.setStyleSheet("background-color:orange")
        self.lcdX80pro.setObjectName("lcdX80pro")
        self.sensorsX80PRO_Group = QtWidgets.QGroupBox(self.X80PROGroup)
        self.sensorsX80PRO_Group.setGeometry(QtCore.QRect(10, 220, 621, 151))
        self.sensorsX80PRO_Group.setObjectName("sensorsX80PRO_Group")
        self.label_16 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_16.setGeometry(QtCore.QRect(60, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.Ux80pro_1 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_1.setGeometry(QtCore.QRect(20, 50, 160, 22))
        self.Ux80pro_1.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_1.setObjectName("Ux80pro_1")
        self.Ux80pro_1.setMaximum(255)
        self.Ux80pro_1.setMinimum(0)
        self.Ux80pro_1.setTickInterval(50)

        self.labelslrobotx80pro_1 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_1.setGeometry(QtCore.QRect(190, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_1.setFont(font)
        self.labelslrobotx80pro_1.setObjectName("labelslrobotx80pro_1")
        self.label_2 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Ux80pro_2 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_2.setGeometry(QtCore.QRect(220, 50, 160, 22))
        self.Ux80pro_2.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_2.setObjectName("Ux80pro_2")
        self.Ux80pro_2.setMaximum(255)
        self.Ux80pro_2.setMinimum(0)
        self.Ux80pro_2.setTickInterval(50)

        self.label_6 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_6.setGeometry(QtCore.QRect(440, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Ux80pro_3 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_3.setGeometry(QtCore.QRect(420, 50, 160, 22))
        self.Ux80pro_3.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_3.setObjectName("Ux80pro_3")
        self.Ux80pro_3.setMaximum(255)
        self.Ux80pro_3.setMinimum(0)
        self.Ux80pro_3.setTickInterval(50)

        self.labelslrobotx80pro_2 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_2.setGeometry(QtCore.QRect(380, 50, 40, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_2.setFont(font)
        self.labelslrobotx80pro_2.setObjectName("labelslrobotx80pro_2")
        self.labelslrobotx80pro_3 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_3.setGeometry(QtCore.QRect(590, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_3.setFont(font)
        self.labelslrobotx80pro_3.setObjectName("labelslrobotx80pro_3")
        self.label_19 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_19.setGeometry(QtCore.QRect(50, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.Ux80pro_4 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_4.setGeometry(QtCore.QRect(20, 120, 160, 22))
        self.Ux80pro_4.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_4.setObjectName("Ux80pro_4")
        self.Ux80pro_4.setMaximum(255)
        self.Ux80pro_4.setMinimum(0)
        self.Ux80pro_4.setTickInterval(50)

        self.labelslrobotx80pro_4 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_4.setGeometry(QtCore.QRect(190, 120, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_4.setFont(font)
        self.labelslrobotx80pro_4.setObjectName("labelslrobotx80pro_4")
        self.label_3 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Ux80pro_5 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_5.setGeometry(QtCore.QRect(220, 120, 160, 22))
        self.Ux80pro_5.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_5.setObjectName("Ux80pro_5")
        self.Ux80pro_5.setMaximum(255)
        self.Ux80pro_5.setMinimum(0)
        self.Ux80pro_5.setTickInterval(50)

        self.labelslrobotx80pro_5 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_5.setGeometry(QtCore.QRect(390, 120, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_5.setFont(font)
        self.labelslrobotx80pro_5.setObjectName("labelslrobotx80pro_5")
        self.label_18 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.label_18.setGeometry(QtCore.QRect(440, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.Ux80pro_6 = QtWidgets.QSlider(self.sensorsX80PRO_Group)
        self.Ux80pro_6.setGeometry(QtCore.QRect(420, 120, 160, 22))
        self.Ux80pro_6.setOrientation(QtCore.Qt.Horizontal)
        self.Ux80pro_6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Ux80pro_6.setObjectName("Ux80pro_6")
        self.Ux80pro_6.setMaximum(255)
        self.Ux80pro_6.setMinimum(0)
        self.Ux80pro_6.setTickInterval(50)

        self.labelslrobotx80pro_6 = QtWidgets.QLabel(self.sensorsX80PRO_Group)
        self.labelslrobotx80pro_6.setGeometry(QtCore.QRect(590, 120, 46, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelslrobotx80pro_6.setFont(font)
        self.labelslrobotx80pro_6.setObjectName("labelslrobotx80pro_6")
        self.groupBox = QtWidgets.QGroupBox(self.X80PROGroup)
        self.groupBox.setGeometry(QtCore.QRect(360, 90, 271, 131))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 231, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.sensorX80proOn = QtWidgets.QPushButton(self.groupBox_2)
        self.sensorX80proOn.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.sensorX80proOn.setIcon(icon3)
        self.sensorX80proOn.setObjectName("sensorX80proOn")
        self.sensorX80proOff = QtWidgets.QPushButton(self.groupBox_2)
        self.sensorX80proOff.setGeometry(QtCore.QRect(120, 20, 91, 23))
        self.sensorX80proOff.setIcon(icon4)
        self.sensorX80proOff.setObjectName("sensorX80proOff")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 70, 231, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cameraX80proOn = QtWidgets.QPushButton(self.groupBox_3)
        self.cameraX80proOn.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.cameraX80proOn.setIcon(icon3)
        self.cameraX80proOn.setObjectName("cameraX80proOn")
        self.cameraX80proOff = QtWidgets.QPushButton(self.groupBox_3)
        self.cameraX80proOff.setGeometry(QtCore.QRect(110, 20, 91, 23))
        self.cameraX80proOff.setIcon(icon4)
        self.cameraX80proOff.setObjectName("cameraX80proOff")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 700, 411, 250))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_38 = QtWidgets.QLabel(self.groupBox_6)
        self.label_38.setGeometry(QtCore.QRect(300, 110, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.imagenMouse = QtWidgets.QLabel(self.groupBox_6)
        self.imagenMouse.setGeometry(QtCore.QRect(30, 110, 101, 141))
        self.imagenMouse.setText("")
        self.imagenMouse.setPixmap(QtGui.QPixmap("mouse_n.png"))
        self.imagenMouse.setScaledContents(True)
        self.imagenMouse.setObjectName("imagenMouse")
        self.label_28 = QtWidgets.QLabel(self.groupBox_6)
        self.label_28.setGeometry(QtCore.QRect(54, 67, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)

        self.label_30 = QtWidgets.QLabel(self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(174, 157, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.label_33 = QtWidgets.QLabel(self.groupBox_6)
        self.label_33.setGeometry(QtCore.QRect(294, 157, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_29 = QtWidgets.QLabel(self.groupBox_6)
        self.label_29.setGeometry(QtCore.QRect(174, 117, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1522, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Reset = QtWidgets.QAction(MainWindow)
        self.Reset.setObjectName("Reset")
        self.actionsas = QtWidgets.QAction(MainWindow)
        self.actionsas.setObjectName("actionsas")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.menuFile.addAction(self.Reset)
        self.menuFile.addAction(self.Exit)
        self.menubar.addAction(self.menuFile.menuAction())


        self.Reset.triggered.connect(self.clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def clicked(self):
        global condicional_borrar
        condicional_borrar=not condicional_borrar
        print(condicional_borrar)











    #esta es la funcion que se ejecutara en otro thread y recibira los datos del proceso y mandara a la thread principal los datos mediante una senal y se actualizara







    def moverlos_suave(self):

        #print("Hello")
        #esta es la funcion que se ejecuta
        print("aqyu si")
        robot_x80_x , robot_x80_y ,robot_x80_tareas,robot_x80_pro_x , robot_x80_pro_y ,robot_x80_pro_tareas,cordenadas,cordenadas2=sacar_datos_para_el_robot_2_parte(self.posiciones_robot1)

        #ROBOT haciendo esto quuitamos el usp de la varuiable global
        #
        print("aqui esta el man")
        robot_x80_x=robot_x80_x
        robot_x80_y=robot_x80_y
        robot_x80_pro_x=robot_x80_pro_x
        robot_x80_pro_y=robot_x80_pro_y




        self.robot_x80=robot()
        self.robot_x80.id=0

        self.robot_x80_pro = robot()
        self.robot_x80_pro.id = 1
        #establecemos puntos iniciales robots
        #
        self.robot_x80.x=robot_x80_x[0]
        self.robot_x80.y=robot_x80_y[0]
        print(" ")
        print(" self.robot_x80.x", self.robot_x80.x)
        print(" self.robot_x80_pro.y", self.robot_x80_pro.y)

        self.robot_x80_pro.x=robot_x80_pro_x[0]
        self.robot_x80_pro.y=robot_x80_pro_y[0]

        #establemcemos la meta
        self.RoboX80meta=( (robot_x80_x[-1],robot_x80_y[-1] ))
        self.RoboX80Prometa = ((robot_x80_pro_x[-1],robot_x80_pro_y[-1] ))
        print(" ")
        print("metas")
        print(self.RoboX80meta)
        print(self.RoboX80Prometa)

        print("atnes del hilo")

        robot_x80_x.pop(0)
        robot_x80_y.pop(0)
        robot_x80_pro_x.pop(0)
        robot_x80_pro_y.pop(0)
        print("puntos A* X,Y robot 1",robot_x80_x,robot_x80_y)
        print("puntos A* X,Y robot 2", robot_x80_pro_x, robot_x80_pro_y)


        #establecesmos los hilos
        self.worker = WorkerThread(robot_x80_x , robot_x80_y ,robot_x80_tareas,self.RoboX80meta,robot_x80_pro_x , robot_x80_pro_y ,robot_x80_pro_tareas,self.RoboX80Prometa,self.robot_x80,self.robot_x80_pro)
        self.worker2 = WorkerThread2(robot_x80_x, robot_x80_y, robot_x80_tareas, self.RoboX80meta, robot_x80_pro_x,robot_x80_pro_y, robot_x80_pro_tareas, self.RoboX80Prometa, self.robot_x80,self.robot_x80_pro)
        self.workerThread = QtCore.QThread()
        self.workerThread2 = QtCore.QThread()
        self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup (optional)
        self.workerThread2.started.connect(self.worker2.run)
        self.worker.signalExample.connect(self.signalExample)  # Connect your signals/slots#cada vez que se recive una senal se ejecuta la funcion
        self.worker2.signalExample2.connect(self.signalExample2)
        self.worker.moveToThread(self.workerThread)  # Move the Worker object to the Thread object
        self.worker2.moveToThread(self.workerThread2)  # Move the Worker object to the Thread object

        self.workerThread2.start()
        self.workerThread.start()

        print("papi HABLALO")

    def signalExample2(self, x):

        global cordenadas_lineas2,cordenadas_obs_encontrados2

        camino_recorrido,sensores,con,obs_encontrados=x
        #print(x)
        #print(z)
        print("dentro del signal", x)
        #WIDGETS X80PRO
        self.labelslrobotx80pro_1.setText(str(sensores[0]))
        self.labelslrobotx80pro_2.setText(str(sensores[1]))
        self.labelslrobotx80pro_3.setText(str(sensores[2]))
        self.labelslrobotx80pro_4.setText(str(sensores[3]))
        self.labelslrobotx80pro_5.setText(str(sensores[4]))
        self.labelslrobotx80pro_6.setText(str(sensores[5]))
        #
        self.Ux80pro_1.setValue(sensores[0])
        self.Ux80pro_2.setValue(sensores[1])
        self.Ux80pro_3.setValue(sensores[2])
        self.Ux80pro_4.setValue(sensores[3])
        self.Ux80pro_5.setValue(sensores[4])
        self.Ux80pro_6.setValue(sensores[5])
        self.lcdX80pro.display(1)
        #WIDGETS X80

        time.sleep(0.1)
        print("camino recorrido XD XD",camino_recorrido)
        #cordenadas_lineas=camino_recorrido

        cordenadas_lineas2=camino_recorrido
        cordenadas_obs_encontrados2=obs_encontrados
        #cordenadas_obs_encontrados=obs_encontrados
        #print("cordenadas_obs_encontrados",cordenadas_obs_encontrados)
        #print(" ")
        #print("Cordenadas lineas",cordenadas_lineas)
        #print(" ")
        #ruta
        #drawLine(intx1, inty1, intx2, inty2)

        self.CellGrid.repaint()


        if con==True:
            self.CellGrid.repaint()
            self.workerThread2.terminate()

            #lo que hace esto es destruir el hilo para que finalizae pq si no queda ahi colgando




        #self.workerThread.msleep(80)
    def signalExample(self, x):

        global cordenadas_lineas,cordenadas_obs_encontrados

        camino_recorrido,sensores,con,obs_encontrados=x
        #print(x)
        #print(z)
        print("dentro del signal", x)
        #WIDGETS X80PRO
        # self.labelslrobotx80pro_1.setText(str(z))
        # self.labelslrobotx80pro_2.setText(str(z))
        # self.labelslrobotx80pro_3.setText(str(z))
        # self.labelslrobotx80pro_4.setText(str(z))
        # self.labelslrobotx80pro_5.setText(str(z))
        # self.labelslrobotx80pro_6.setText(str(z))
        #
        # self.Ux80pro_1.setValue(z)
        # self.Ux80pro_2.setValue(z)
        # self.Ux80pro_3.setValue(z)
        # self.Ux80pro_4.setValue(z)
        # self.Ux80pro_5.setValue(z)
        # self.Ux80pro_6.setValue(z)
        # self.lcdX80pro.display(z)
        #WIDGETS X80
        self.labelslrobotx80_1.setText(str(sensores[0]))
        self.labelslrobotx80_2.setText(str(sensores[1]))
        self.labelslrobotx80_3.setText(str(sensores[2]))

        self.Ux80_1.setValue(sensores[0])
        self.Ux80_2.setValue(sensores[0])
        self.Ux80_3.setValue(sensores[0])
        self.lcdX80.display(1)
        time.sleep(0.1)
        print("camino recorrido XD XD",camino_recorrido)
        #cordenadas_lineas=camino_recorrido
        self.CellGrid.ruta=camino_recorrido
        cordenadas_lineas=camino_recorrido
        cordenadas_obs_encontrados=obs_encontrados
        print("CORDENADAS OBS" , cordenadas_obs_encontrados)
        #print(" ")
        #print("Cordenadas lineas",cordenadas_lineas)
        #print(" ")
        #ruta
        #drawLine(intx1, inty1, intx2, inty2)

        self.CellGrid.repaint()


        if con==True:
            self.CellGrid.repaint()
            self.workerThread.terminate()

            #lo que hace esto es destruir el hilo para que finalizae pq si no queda ahi colgando




        #self.workerThread.msleep(80)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Robotico De Servicio "))
        self.Run.setText(_translate("MainWindow", "Run Path Planning"))
        self.Delete.setText(_translate("MainWindow", "Delete Path"))
        self.X80Group.setTitle(_translate("MainWindow", "Robot X80"))
        self.label_10.setText(_translate("MainWindow", "WiFi mobile robot"))
        self.label_9.setText(_translate("MainWindow", "RobotX80"))

        self.camera_sensorsX80_Group.setTitle(_translate("MainWindow", "Control ON-OFF"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Camera"))
        self.cameraX80On.setText(_translate("MainWindow", "On Camera"))
        self.cameraX80Off.setText(_translate("MainWindow", "Off Camera"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Sensors"))
        self.sensorX80On.setText(_translate("MainWindow", "On Sensors"))
        self.sensorX80Off.setText(_translate("MainWindow", "Off Sensors"))
        self.sensorsX80_Group.setTitle(_translate("MainWindow", "Sensors"))
        self.labelslrobotx80_1.setText(_translate("MainWindow", "0"))
        self.labelslrobotx80_2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Ultrasonic 2nd"))
        self.label_5.setText(_translate("MainWindow", "Ultrasonic 1st"))
        self.labelslrobotx80_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Ultrasonic 3rd"))
        self.X80PROGroup.setTitle(_translate("MainWindow", "Robot X80 Pro"))

        self.label_23.setText(_translate("MainWindow", "RobotX80 Pro"))
        self.label_24.setText(_translate("MainWindow", "WiFi mobile robot Pro"))
        self.sensorsX80PRO_Group.setTitle(_translate("MainWindow", "Sensors"))
        self.label_16.setText(_translate("MainWindow", "Ultrasonic 1st"))
        self.labelslrobotx80pro_1.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Ultrasonic 2nd"))
        self.label_6.setText(_translate("MainWindow", "Ultrasonic 3rd"))
        self.labelslrobotx80pro_2.setText(_translate("MainWindow", "0"))
        self.labelslrobotx80pro_3.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Ultrasonic 4th"))
        self.labelslrobotx80pro_4.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Ultrasonic 5th"))
        self.labelslrobotx80pro_5.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Ultrasonic 6th"))
        self.labelslrobotx80pro_6.setText(_translate("MainWindow", "0"))
        self.groupBox.setTitle(_translate("MainWindow", "Control ON-OFF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sensors"))
        self.sensorX80proOn.setText(_translate("MainWindow", "On Sensors"))
        self.sensorX80proOff.setText(_translate("MainWindow", "Off Sensors"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Camera"))
        self.cameraX80proOn.setText(_translate("MainWindow", "On Camera"))
        self.cameraX80proOff.setText(_translate("MainWindow", "Off Camera"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Mouse Events"))
        self.label_38.setText(_translate("MainWindow", "RobotX80"))
        self.label_28.setText(_translate("MainWindow", "Mouse Click: Task & Obstacle Assigment"))

        self.label_30.setText(_translate("MainWindow", "Middle Click"))

        self.label_33.setText(_translate("MainWindow", "Obstacles"))
        self.label_29.setText(_translate("MainWindow", "Left Click"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.Reset.setStatusTip(_translate("MainWindow", "Reset The Obs"))
        self.Reset.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionsas.setText(_translate("MainWindow", "sas"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Exit.setStatusTip(_translate("MainWindow", "Exit Program"))
        self.Exit.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
