# All library imports
import can
from can import Message
import time

# Setup array's for all diferent data types
shift = 0
calcVal = []
buffer = []
valArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msgContain = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msgForm = [256, 257, 258, 259, 260, 261, 262, 263, 512, 513, 514, 515, 768, 769, 770, 771, 1024, 1025, 1026, 1027]

# Setup the CAN-bus interface from the Pi Hat
bus = can.interface.Bus(chanel='can0', bustype='socketcan_native')

# Repeating loop for receiving and displaying data
while True:

    # Write all incomming data 2 times in the buffer
    shift = 0
    buffer = []
    while shift < 40:
        buffer.append(bus.recv(None))
        shift += 1

    # Pull all little arrays and sort them by ID in the main message container
    shift = 0
    while shift < 40:
        for a in range(19):
            if buffer[shift].arbitration_id == msgForm[a]:
                msgContain[a] = list(buffer[shift].data)
            else:
                msgContain[a] = msgContain[a]
        shift += 1

    # Calculate all the values to floats and write error msg in place of empty spaces
    shift = 0
    calcVal = []
    while shift < 20:
        if msgContain[shift] == 0:
            valArray[shift] = "Receive-error"
        else:
            calcVal.append(str(msgContain[shift][0]) + str(msgContain[shift][1]) + str(".") + str(msgContain[shift][2]) + str(msgContain[shift][3]))
            valArray[shift] = calcVal[shift]
        shift += 1

    for i in range(20):
        if i <= 7:
            print("Temp-" + str(i+1) + ": " + str(valArray[i]))
        if i > 7 and i <= 11:
            print("Delta-" + str(i-7) + ": " + str(valArray[i]))
        if i > 11 and i <= 14:
            print("Flow-" + str(i-11) + ": " + str(valArray[i]))
        if i > 14 and i <= 15:
            print("Flow-H2: " + str(valArray[i]))
        if i > 15:
            print("Power-" + str(i-15) + ": " + str(valArray[i]))

    print()
    shift = 0
    buffer = []
    calcVal = []
    msgContain = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    time.sleep(60)

