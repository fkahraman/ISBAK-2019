from pylab import *
import pandas as pd
from math import fabs

minData = [0,0,0,0,0]
maxData = [0,0,0,0,0]
farkDegerleri = [0]
minFarkToplam = []

def max(data):

    ct = 4
    rangeData = len(data)

    for i in range(rangeData-5):

        degerDizisi = [data[ct], data[ct-1], data[ct-2], data[ct-3], data[ct-4]]
        degerDizisi.sort()
        cikisDegeri = degerDizisi[4]
        maxData.append(cikisDegeri)
        ct+=1

    DataSetMax = list(zip(maxData))
    df = pd.DataFrame(data=DataSetMax, columns=None)
    df.to_csv('maxDegerleri.txt', index=False, header=False)

def min(data):

    ct = 4
    rangeData = len(data)

    for i in range(rangeData-5):

        degerDizisi = [data[ct], data[ct-1], data[ct-2], data[ct-3], data[ct-4]]
        degerDizisi.sort()
        cikisDegeri = degerDizisi[0]
        minData.append(cikisDegeri)
        ct+=1

    DataSetMin = list(zip(minData))
    df = pd.DataFrame(data=DataSetMin, columns=None)
    df.to_csv('minDegerleri.txt', index=False, header=False)

def fark(data):

    rangeData = len(data)

    ct = 1

    for i in range(rangeData-1):

        araDeger = data[ct] - data[ct-1]
        araDeger = fabs(araDeger)
        farkDegerleri.append(araDeger)
        ct = ct+1

    DataSetFark = list(zip(farkDegerleri))
    df = pd.DataFrame(data=DataSetFark, columns=None)
    df.to_csv('farkDegerleri.txt', index=False, header=False)

if __name__ == '__main__':



    df = pd.read_excel('Clio test grafikleriPy.xlsx', sheet_name='TEST4', header=None)

    sensorToplam = df[7]    # 3 eksen toplam değerler

    sensorToplam = sensorToplam[2:1330]
    sensorToplam = list(sensorToplam)


    fark(sensorToplam)
    min(sensorToplam)
    max(sensorToplam)

    # # # Sensör Degerlerinden EMA,SMA degerlerinin çıkarılması ve kaydedilmesi # # #

    DataSetSensor = list(zip(sensorToplam))
    df = pd.DataFrame(data=DataSetSensor, columns=None)
    df.to_csv('SensorValue.txt', index=False, header=False)
    Location = r'C:\Users\fatih\PycharmProjects\untitled\AFTER ISBAK 2019\ClioTest\Test1\SensorValue.txt'







