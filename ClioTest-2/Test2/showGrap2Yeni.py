from pylab import *
import pandas as pd

if __name__ == '__main__':

    #   #   #   Verilerin Okunmasu  #   #   #

    DATASensor = pd.read_csv('SensorValue.txt', header=None, names=['Sensor'])
    DATAFark = pd.read_csv('farkDegerleri.txt', header=None, names=['Fark'])
    DATAMin = pd.read_csv('minDegerleri.txt', header=None, names=['Min'])
    DATAMax = pd.read_csv('maxDegerleri.txt', header=None, names=['Max'])

    #   #   #   ALGORİTMA   #   #   #

    ct = 0

    parkData = []
    parkCikisData = []
    parkSayisi = 0
    parkDurumu = False
    parkCikisBekleme = True
    parkKey = False

    while(ct < 2100):

        if parkKey == False:

            if DATAFark.Fark[ct] + 100 > DATAMax.Max[ct] or DATAFark.Fark[ct] + 100 > DATASensor.Sensor[ct]:

                if DATAFark.Fark[ct] > 200:

                    parkKey = True
                    ct+=2

        else:

            if parkDurumu == False:

                donguSayac = 0
                donguDizisi = []
                while(DATAFark.Fark[ct] > 150):

                    ct += 1
                    donguSayac += 1

                    if donguSayac == 7:
                        parkKey = False
                        break

                if parkKey == True:

                    ct += 3

                    for i in range(3):

                        if DATAFark.Fark[ct] < DATAMin.Min[ct]:

                            if DATAFark.Fark[ct] < DATAMax.Max[ct]:

                                if DATAFark.Fark[ct] < DATASensor.Sensor[ct]:

                                    donguDizisi.append(1)

                                else:
                                    parkKey = False

                            else:
                                parkKey = False

                        else:
                            parkKey = False

                        ct+=1

                    if len(donguDizisi) == 3:

                        if DATASensor.Sensor[ct] > 300:

                            parkSayisi+=1
                            parkData.append(ct)
                            parkDurumu = True


                        else:
                            parkKey = False

                        ct+=1

                    else:
                        parkKey = False

            if parkDurumu == True:

                if DATAFark.Fark[ct] + 50 > DATASensor.Sensor[ct]:

                    parkDurumu = False
                    parkKey = False
                    parkCikisData.append(ct)

        ct +=1


    print(parkSayisi)
    print(parkData)
    print(parkCikisData)

    #   #   #   Grafiksel Kısım   #   #   #

    grid = True
    title("Araç Park Sistemi Giriş-Çıkış Grafiği")
    xlabel("Time")
    ylabel("Giriş-Çıkış")

    x = arange(0, 2103, 1)
    y = array(DATASensor[0:2103])

    x_fark = arange(0, 2103, 1)
    y_fark = array(DATAFark[0:2103])

    x_min = arange(0, 2103, 1)
    y_min = array(DATAMin[0:2103])

    x_max = arange(0, 2103, 1)
    y_max = array(DATAMax[0:2103])

    plot(x, y, "-o",label='Sensör Grafiği')
    plot(x_fark, y_fark, "-o",label='Fark Grafiği')
    plot(x_min, y_min, "-o",label='Min Grafiği')
    plot(x_max, y_max, "-o",label='Max Grafiği')

    legend()
    show()


