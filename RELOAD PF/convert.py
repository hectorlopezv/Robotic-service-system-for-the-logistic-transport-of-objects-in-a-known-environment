def hex2byte(num):
    numHe = hex(num)
    if num > 0x09:
        numHe = numHe[2:4]
        numByte = bytes.fromhex(numHe)
    else:
        numHe = numHe[2:3]
        numByte = bytes.fromhex('0' + numHe)

    return numByte


def div_data(data):
    L = len(data)
    datadiv = []
    for i in range(0, L, 2):
        datadiv.append(data[i:i + 2])
    return datadiv


def hex2str(num):
    numHe = hex(num)
    if num > 0x09:
        numHe = numHe[2:4]
    else:
        numHe = '0' + numHe[2:3]

    return numHe


def numhex(numhe):
    if numhe == '0':
        nume = 0
    elif numhe == '1':
        nume = 1
    elif numhe == '2':
        nume = 2
    elif numhe == '3':
        nume = 3
    elif numhe == '4':
        nume = 4
    elif numhe == '5':
        nume = 5
    elif numhe == '6':
        nume = 6
    elif numhe == '7':
        nume = 7
    elif numhe == '8':
        nume = 8
    elif numhe == '9':
        nume = 9
    elif numhe == 'a':
        nume = 10
    elif numhe == 'b':
        nume = 11
    elif numhe == 'c':
        nume = 12
    elif numhe == 'd':
        nume = 13
    elif numhe == 'e':
        nume = 14
    elif numhe == 'f':
        nume = 15

    return nume


def str2Hex(cadena):
    num = numhex(cadena[0]) * 16 + numhex(cadena[1])
    return num



