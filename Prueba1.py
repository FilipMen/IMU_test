import serial
import time
import os

IMUs = serial.Serial('COM8',115200)
listID = []
listData = []

try:
    while(True):
        if IMUs.isOpen():
            while IMUs.in_waiting:  # Or: while ser.inWaiting():
                datos = IMUs.readline().decode("utf-8").rstrip('\r\n')

                Aux = datos.split(' ')
                Aux1 = datos.split(':')
                if(Aux[0]=='Extended'):
                    #print(datos)
                    ID = Aux[2]
                    data = Aux1[-1]
                    if (ID not in listID):
                        listID.append(ID)
                        listData.append(data)
                    for i, item in enumerate(listID):
                        if item == ID:
                            listData[i] = data
                        print('ID: {} Data: {}'.format(item,listData[i]))
                    time.sleep(0.1)
                    os.system('cls')
                else:
                    print(datos)

except KeyboardInterrupt:
    IMUs.close()

print('Programa terminado')