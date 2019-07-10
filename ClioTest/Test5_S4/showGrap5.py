from pylab import *
import pandas as pd

parkData = []

if __name__ == '__main__':

    #   #   #   Verilerin Okunmasu  #   #   #

    DATAEMA = pd.read_csv('EMAValue.txt', header=None, names=['EMA'])
    DATASMA = pd.read_csv('SMAValue.txt', header=None, names=['SMA'])
    DATASensor = pd.read_csv('SensorValue.txt', header=None, names=['Sensor'])
    DATASapma = pd.read_csv('SapmaValue.txt', header=None, names=['Sapma'])
    DATASapmaSMA = pd.read_csv('SapmaSMAValue.txt', header=None, names=['SapmaSMA'])

    #   #   #   PARK ALGORİTMASI #  #   #

    ct = 0
    parkSayisi = 0

    park = False
    parkcikisbekleme = False

    while(ct < 850):

        if parkcikisbekleme == False:

            if park == False:

                if (DATASapmaSMA.SapmaSMA[ct] > DATASapma.Sapma[ct]):

                    if (DATASapmaSMA.SapmaSMA[ct] > 50):

                        if (DATASapmaSMA.SapmaSMA[ct] < DATASMA.SMA[ct]):

                            if(DATASapmaSMA.SapmaSMA[ct] < DATASensor.Sensor[ct]):

                                parkSayisi += 1
                                parkData.append(ct)
                                park = True

            else:

                if (DATASapmaSMA.SapmaSMA[ct] > DATASapma.Sapma[ct]):

                    if (DATASapmaSMA.SapmaSMA[ct] > 100):

                        if (DATASapmaSMA.SapmaSMA[ct] > DATASMA.SMA[ct]):

                            park = False
                            parkcikisbekleme = True
        else:

            if(DATASapmaSMA.SapmaSMA[ct] < 50):

                parkcikisbekleme = False

        ct += 1

    print("Ct:" , ct)
    print("Park Sayısı: ",parkSayisi)
    print(parkData)

    #   #   #

    parkDataY = []

    sayac = 0

    #   #   #   Grafiksel Kısım   #   #   #

    grid = True
    title("Araç Park Sistemi Giriş-Çıkış Grafiği")
    xlabel("Time")
    ylabel("Giriş-Çıkış")

    x = arange(0, 850, 1)
    y = array(DATASensor[0:850])

    #xS = arange(0, 850, 1)
    #yS = array(DATAEMA[0:850])

    x_sma = arange(0, 850, 1)
    y_sma = array(DATASMA[0:850])

    x_sapma = arange(0,850,1)
    y_sapma = array(DATASapma[0:850])

    x_sapmaSMA = arange (0,850,1)
    y_sapmaSMA = array(DATASapmaSMA[0:850])

    plot(x, y, "-o",label='Sensör Grafiği')
    #plot(xS, yS, "-o",label="EMA Grafiği")
    plot(x_sma, y_sma, "-o",label="SMA Grafiği")
    plot(x_sapma, y_sapma, "-o",label="Standart Sapma")
    plot(x_sapmaSMA, y_sapmaSMA, "-o", label="Sapma SMA")

    legend()
    show()


