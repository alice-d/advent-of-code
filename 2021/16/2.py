import math

hex = "C200B40A82"
hex = "04005AC33890"
hex = "880086C3E88112"
hex = "CE00C43D881120"
hex = "D8005AC2A8F0"
hex = "F600BC2D8F"
hex = "9C005AC2F8F0"
hex = "9C0141080250320F1802104A08"

hex  = "420D50000B318100415919B24E72D6509AE67F87195A3CCC518CC01197D538C3E00BC9A349A09802D258CC16FC016100660DC4283200087C6485F1C8C015A00A5A5FB19C363F2FD8CE1B1B99DE81D00C9D3002100B58002AB5400D50038008DA2020A9C00F300248065A4016B4C00810028003D9600CA4C0084007B8400A0002AA6F68440274080331D20C4300004323CC32830200D42A85D1BE4F1C1440072E4630F2CCD624206008CC5B3E3AB00580010E8710862F0803D06E10C65000946442A631EC2EC30926A600D2A583653BE2D98BFE3820975787C600A680252AC9354FFE8CD23BE1E180253548D057002429794BD4759794BD4709AEDAFF0530043003511006E24C4685A00087C428811EE7FD8BBC1805D28C73C93262526CB36AC600DCB9649334A23900AA9257963FEF17D8028200DC608A71B80010A8D50C23E9802B37AA40EA801CD96EDA25B39593BB002A33F72D9AD959802525BCD6D36CC00D580010A86D1761F080311AE32C73500224E3BCD6D0AE5600024F92F654E5F6132B49979802129DC6593401591389CA62A4840101C9064A34499E4A1B180276008CDEFA0D37BE834F6F11B13900923E008CF6611BC65BCB2CB46B3A779D4C998A848DED30F0014288010A8451062B980311C21BC7C20042A2846782A400834916CFA5B8013374F6A33973C532F071000B565F47F15A526273BB129B6D9985680680111C728FD339BDBD8F03980230A6C0119774999A09001093E34600A60052B2B1D7EF60C958EBF7B074D7AF4928CD6BA5A40208E002F935E855AE68EE56F3ED271E6B44460084AB55002572F3289B78600A6647D1E5F6871BE5E598099006512207600BCDCBCFD23CE463678100467680D27BAE920804119DBFA96E05F00431269D255DDA528D83A577285B91BCCB4802AB95A5C9B001299793FCD24C5D600BC652523D82D3FCB56EF737F045008E0FCDC7DAE40B64F7F799F3981F2490"

packet =""
for h in hex:
    packet += bin(int(h,16))[2:].zfill(4)
# print(packet)

def processLiteralValPacket(content):
    literal =""
    for i in range(0,len(content),5):
        val = content[i]
        literal += content[i+1:i+5]
        if val == "0":
            break
    literalNum = int(literal,2)
    # print("literal: ", literalNum)
    return literalNum, content[i+5:]

def readSubsOfLen(packet, values):
    value, remaining = processPacket(packet)
    values += [value]
    if len(remaining)>0:
        return readSubsOfLen(remaining, values)
    else:
        return values
       
def readNumOfSubs(packet, num):
    values = []
    while num>0:
        value, packet = processPacket(packet)
        num-=1
        values.append(value)
    return values, packet

def processPacket(packet):
    global versionSum
    version = int(packet[:3],2)
    # print("verison: ", version)
    type = int(packet[3:6],2)
    # print("type: ", type)

    if type==4:
        result, remainingPacket = processLiteralValPacket(packet[6:])
    else:
        # print("operator")
        lenType = int(packet[6])
        # print("lenType: ",lenType)

        if lenType == 0:
            #15 bit with lenght of bits
            subLen = int(packet[7:22],2)
            # print("bits in sub packets: ",subLen)
            values = readSubsOfLen(packet[22:22+subLen], [])
            remainingPacket = packet[22+subLen:]
            
        elif lenType == 1:
            #11 bits with number of bits
            numOfSubPackets = int(packet[7:18],2)
            values, remainingPacket = readNumOfSubs(packet[18:], numOfSubPackets)

        if type == 0:
            result = sum(values)
        elif type==1:
            result = math.prod(values)
        elif type ==2:
            result = min(values)
        elif type==3:
            result = max(values)
        elif type==5:
            result = 1 if values[0] > values[1] else 0
        elif type==6:
            result = 1 if values[0] < values[1] else 0
        elif type==7:
            result = 1 if values[0] == values[1] else 0
      
    return result, remainingPacket

res, _ = processPacket(packet)

print(res)
