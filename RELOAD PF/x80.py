import socket
import checksum
import time
from datetime import datetime,timedelta

# ESTA ES LA "LIBRERIA" DEL ROBOT SOLO ES INCLUIR TODAS LAS FUNCIONES AQUÍ E IMPORTARLA EN UN ARCHIVO Y YA.


UDP_IP = "192.168.0.202"
UDP_PORT = 10001
STX = "5e02"
RID = "01"
ETX = "5e0d"
reservet = "00"


def setIP(robot):
    # "CALL" GLOBAL VARIABLES
    global UDP_IP
    global UDP_PORT
    # CHECK ROBOT AND SET IP & PORT
    if robot == 0:#pro
        UDP_IP = "192.168.0.201"
        UDP_PORT = 10001
    if robot == 1:#Normal
        UDP_IP = "192.168.0.202"
        UDP_PORT = 10001


def enableMotorServo(robot, sw):
    # "CALL" GLOBAL VARIABLES
    global STX
    global RID
    global ETX
    global reservet
    # FUNCTION LOCAL VARIABLES
    DID = "1e"
    lengh = "01"
    # SWITCH FOR DATA
    if sw == 0:
        data = '00'
    else:
        data = '01'
    # CHECKSUM AND PACKET FOR TX
    check = checksum.checksum(RID, reservet, DID, lengh, data)
    packet = bytes.fromhex(STX + RID + reservet + DID + lengh + data + check + ETX)
    # IP SET AND SENDING
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',10001))

    s.sendto(packet, (UDP_IP, 10001))

    return 10001


def turn90(robot, lr):
    if lr == 0:
        # DERECHA
        pack = bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
    else:
        # IZQUIERDA
        pack = bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')

    # pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 10001))


    s.sendto(pack, (UDP_IP, 10001))
    s.close()
    time.sleep(1)
    stop(robot)
    time.sleep(0.5)
    s.close()
    return  10001


def turn45(robot, lr):
    if lr == 0:
        # DERECHA
        pack = bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
    else:
        # IZQUIERDA
        pack = bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')

    # pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 10001))
    s.sendto(pack, (UDP_IP, 10001))
    s.close()
    time.sleep(0.5)
    stop(robot)
    time.sleep(0.5)

    return 10001

def stop(robot):
    velData = '00000000'
    startOfPack = '5e 02 01 00 1b 0c'
    endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
    pack = bytes.fromhex(startOfPack + velData + endOfPack)
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 10001))

    s.sendto(pack, (UDP_IP, 10001))

    return 10001
def forward2(robot, distance):
    # SWITCH FOR DATA
    velData = 'd4fe2c01'
    startOfPack = '5e 02 01 00 1b 0c'
    endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
    pack = bytes.fromhex(startOfPack + velData + endOfPack)
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',10001))
    s.sendto(pack, (UDP_IP, 10001))
    F=s.getsockname()
    print(F)


    time.sleep(1.6 * distance)
    #time.sleep(0.1 * distance)
    stop(robot)


    return 10001



def forwardL(robot, distance):
    # SWITCH FOR DATA
    velData = 'd4fe2c01'
    startOfPack = '5e 02 01 00 1b 0c'
    endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
    pack = bytes.fromhex(startOfPack + velData + endOfPack)
    setIP(robot=robot)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 10001))
    s.sendto(pack, (UDP_IP, 10001))

    time.sleep(2.263 * distance)
    stop(robot)
    s.close()
    return 10001



#
# # izquierda()
#
#
# puerto=enableMotorServo(0,1)
# puerto=turn90(1,1)
# print("Puerto",puerto)