import convert


# byte_data3=0x08
# packet=[RID,reservet,DID,lengh,byte_data1,byte_data2]
def checksum(RID, reservet, DID, lengh, byte_data):
    data = convert.div_data(byte_data)
    packet = [RID, reservet, DID, lengh]

    for i in range(len(data)):
        packet.append(data[i])

    for i in range(len(packet)):
        packet[i] = convert.str2Hex(packet[i])

    s_reg = 0
    nsize = len(packet)
    for i in range(nsize):
        v = packet[i]
        for j in range(8):
            data_bit = v & 0x01
            sr = s_reg & 0x01
            fb = (sr ^ data_bit) & 0x01
            s_reg = s_reg >> 1
            if fb == 1:
                s_reg = s_reg ^ 0x8c
            v = v >> 1

    return convert.hex2str(s_reg)
