from pylab import *
import pandas as pd
from math import sqrt

def stdSapma(startDay, stdCounter, data):

    if(stdCounter > startDay):
        return

    toplam = 0
    karetoplam = 0
    ct = 0

    while(stdCounter > 0):

        toplam = toplam + data[startDay - stdCounter]
        stdCounter -= 1
        ct += 1

    ortalama = toplam/ct

    while(ct > 0):

        karetoplam = (data[startDay-ct] - ortalama)**2 + karetoplam
        ct -= 1
        stdCounter += 1

    return sqrt(karetoplam/(stdCounter-1))

def SMA(startDay, smaCounter, data):

    toplam = 0
    startCounter = smaCounter

    while(smaCounter > 0):

        smaValue = int(data[startDay - smaCounter])
        toplam = toplam + smaValue
        smaCounter -= 1

    return int(toplam / startCounter)

def EMA(startDay, emaCounter, data):

    k1 = 1 #ilk indis
    k2 = 1 #ikinci indis

    ema = int(data[startDay - emaCounter])

    emaValue = ema
    emaCounter -= 1

    while(emaCounter > 1):

        emaValue = (2/(2+k1)) * data[startDay - emaCounter] + ((0+k2)/(2+k2)) * emaValue

        k1 += 1
        k2 += 1
        emaCounter -= 1

    return emaValue


if __name__ == '__main__':

    emaDatalari = []
    smaDatalari = []
    sapmaDatalari = []
    sapmaSMA = []


    df = pd.read_excel('Büyük araç test grafikleri py.xlsx', sheet_name='TEST3', header=None)

    #aracDurum = df[8]   # Şahsi değerler
    sensorToplam = df[6]    # 3 eksen toplam değerler

    sensorToplam = sensorToplam[2:837]

    day = 15

    for j in range(820):

        emaDatalari.append(EMA(day, 5, sensorToplam))
        day += 1

    day = 15

    for h in range(820):

        smaDatalari.append(SMA(day, 5, sensorToplam))
        day += 1

    day = 15

    for n in range(820):

        sapmaDatalari.append(stdSapma(day, 5, sensorToplam))
        day += 1

    sensorToplam = sensorToplam[15:820]

    day = 10

    for i in range(810):

        sapmaSMA.append(SMA(day, 3, sapmaDatalari))
        day += 1

    dizi = [0,0,0,0,0,0,0,0,0,0]

    sapmaSMA = dizi + sapmaSMA
    print(sapmaSMA)

    # # # Sensör Degerlerinden EMA,SMA degerlerinin çıkarılması ve kaydedilmesi # # #

    DataSetSensor = list(zip(sensorToplam))
    df = pd.DataFrame(data=DataSetSensor, columns=None)
    df.to_csv('SensorValue.txt', index=False, header=False)
    Location = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\BuyukAracTest\Test3\SensorValue.txt'
    #DATASensor = pd.read_csv('SensorValue.txt', header=None, names=['Sensor_Degerleri'])

    DataSetEMA = list(zip(emaDatalari))
    df = pd.DataFrame(data=DataSetEMA, columns=None)
    df.to_csv('EMAValue.txt', index=False, header=False)
    Location2 = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\BuyukAracTest\Test3\EMAValue.txt'
    #DATAEMA = pd.read_csv('EMAValue.txt', header=None, names=['EMA_Degerleri'])

    DataSetSMA = list(zip(smaDatalari))
    df = pd.DataFrame(data=DataSetSMA, columns=None)
    df.to_csv('SMAValue.txt', index=False, header=False)
    Location3 = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\BuyukAracTest\Test3\SMAValue.txt'
    #DATASMA = pd.read_csv('SMAValue.txt', header=None, names=['SMA_Degerleri'])

    DataSetSapma = list(zip(sapmaDatalari))
    df = pd.DataFrame(data=DataSetSapma, columns=None)
    df.to_csv('SapmaValue.txt', index=False, header=False)
    Location4 = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\BuyukAracTest\Test3\SapmaValue.txt'

    DataSetSapmaSMA = list(zip(sapmaSMA))
    df = pd.DataFrame(data=DataSetSapmaSMA, columns=None)
    df.to_csv('SapmaSMAValue.txt', index=False, header=False)
    Location5 = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\BuyukAracTest\Test3\SapmaSMAValue.txt'



