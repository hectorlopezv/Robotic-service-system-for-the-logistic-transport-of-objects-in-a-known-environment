

import socket

import socket
def leer_ultrasonido_robot_1(ip,port,robotid):#da el ultimo dato obtenido se bloquea momentaneamente el codigo

    print("PADRE NUESTRO 2")
    print("rid",robotid)
    print(" ")
    print("Puerto",port)
    datis=[]
    #sock1=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock1:
        sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock1.bind(('', port))

        i = 0
        sensor_datos = []
        while i < 5:
            # print("PAPI HERMOSITO")

            data, addr = sock1.recvfrom(1024)
            data = data.hex()
            addi, puertico = addr
            if   addi=="192.168.0.201"  and robotid==0 and len(data)==190:
                i += 1
                sensor_datos.append(data)
            if   addi=="192.168.0.202"  and robotid==1 and len(data)==190:
                i += 1
                sensor_datos.append(data)
        return sacar_datos_ultrasonido(sensor_datos)


def sacar_datos_ultrasonido(data):
    data=data[-1]
    if len(data) == 190:
        data = data[:98]
        #print(data)
        # print(data)
        data = data[12:]
       # print(data)
        # dato 1
        sensorH = data[:2]
        sensorH = int(sensorH, 16)
        #print(sensorH)
        # dato 2
        sensorI = data[2:4]
        sensorI = int(sensorI, 16)
        #print(sensorI)
        # dato 3
        sensorJ = data[4:6]
        sensorJ = int(sensorJ, 16)
        #print(sensorJ)
        # dato 4
        sensorK = data[6:8]
        sensorK = int(sensorK, 16)
        #print(sensorK)
        # dato 5
        sensorL = data[8:10]
        sensorL = int(sensorL, 16)
        #print(sensorL)
        # dato 6
        sensorM = data[10:12]
        sensorM = int(sensorM, 16)
        x1=data[12:14]
        x1=int(x1,16)
        x1=str(x1)
        x2=data[14:16]
        x2=int(x2,16)
        x2=str(x2)

        x3=data[16:18]
        x3=int(x3,16)
        x3=str(x3)
        x4=data[18:20]
        x4=int(x4,16)
        x4=str(x4)

        x5=data[20:22]
        x5=int(x5,16)
        x5=str(x5)
        x6=data[22:24]
        x6=int(x6,16)
        x6=str(x6)

        x7=data[24:26]
        x7=int(x7,16)
        x7=str(x7)
        x8=data[26:28]
        x8=int(x8,16)
        x8=str(x8)
        #print(sensorM)
        x_spacio="                   "
        #sensor humano


    return (sensorH,sensorI,sensorJ,sensorK,sensorL,sensorM,x_spacio,x1+x2,x3+x4,x5+x6,x7+x8)