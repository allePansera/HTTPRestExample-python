"""Lo script serve a generare un DB di test con dei dati riutilizzabili per i vari test.
I dati andaranno salvati un file JSON per questioni di tempo.
Data structure:
    1 {
    2 " uuid ": " device00002 ",
    3 " type ": " iot : demosensor ",
    4 " softwareVersion ": " v0 .0.0.1" ,
    5 " manufacturer ": " Acme - Inc "
    6 }
    """
import json, random
from Service.device import Device

FILE_PATH = "../DB/content.json"
DEVICE_NUMBER = 10


#DEFINISCO I METODI UTILI A CREARE DEI VALORI CASUALI DA INSERIERE DENTRO LA MIA LISTA DI DEVICE
def randUuid(deviceList):
    randomNum = 1
    if len(deviceList)==0:
        return "device" + str(randomNum)
    while("device"+str(randomNum) in [dev['uuid'] for dev in deviceList]):
        randomNum = random.randint(0,50)
    return "device"+str(randomNum)

def randType():
    TYPE = ["HUMIDITY_SENSOR","TEMPERATURE_SENSOR","DEMO_SENSOR"]
    return TYPE[random.randint(0,2)]

def randSwVersion():
    return f'{random.randint(0, 10)}.{random.randint(0, 4)}.{random.randint(0, 15)}'

def randManufacturer():
    MANUFACTURER_LIST = ["HUAWEI", "XIAOMI", "BOSCH", "TEAXS INSTRUMENT", "TOYOTA", "FOXCOMM"]
    return MANUFACTURER_LIST[random.randint(0, 5)]


#CREAZIONE DELLA VARIABILE PER GESTIRE LA LISTA DEI DEVICE CREATI
deviceList = []
#CREAZIONE DEI n-DISPOSITIVI
for index in range(0,DEVICE_NUMBER):
    deviceList.append(
        Device(uuid=randUuid(deviceList),type=randType(),manufacturer=randManufacturer(),softwareVersion=randSwVersion())
            .toJson()
    )

#SALAVATGGIO DELLA LISTA DEI DISPOSITIVI DENTRO AD UN FILE JSON DI PROVA
with open(FILE_PATH, 'w') as f:
    json.dump(deviceList, f,  indent=4)

