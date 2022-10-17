import json
from Service.device import Device


class DeviceDataManager:
    """La classe si occupa di gestire le operazioni di lettura/scrittura sul db dei dispositivi noto"""
    def __init__(self,FILE_PATH="DB/content.json"):
        self.FILE_PATH = FILE_PATH

    def loadAllDevices(self):
        """Ritorno una lista di Json rappresentanti n- Device, se non trovo nulla ritorno una lista vuota"""
        with open(self.FILE_PATH,"r") as jsonFileContent:
            jsonList = json.load(jsonFileContent)
            if len(jsonList)==0:
                return []
            else:
                return [dev for dev in jsonList]

    def loadDevice(self,uuid):
        """Ritorno un singolo device in formato json in una lista fotnito un ID, se il device non è presente ritorno una lista vuota"""
        with open(self.FILE_PATH, "r") as jsonFileContent:
            jsonList = json.load(jsonFileContent)
            if len(jsonList) == 0:
                return []
            else:
                return [dev for dev in jsonList if dev['uuid']==uuid]

    def addDevice(self,deviceObj):
        """Fornito un device lo inserisco nel mio file, controllo ovviamente che l'uuid dell'oggetto non sia già esistente.
        Viene ritornata una lista, se vuota non è stato creato l'oogetto, se invece contiene l'oggetto passato ho aggiornato correttamente il database"""
        deviceSearch = self.loadDevice(deviceObj.uuid)
        if len(deviceSearch)==0:
            #SALVO IL VECCHIO CONTENUTO
            deviceList = []
            with open(self.FILE_PATH, "r") as jsonFileContent:
                deviceList = json.load(jsonFileContent)
            #AGGIORNO IL VECCHIO CONTENUTO
            deviceList.append(deviceObj.toJson())
            #RICARICO IL CONTENUTO NEL DATABASE
            with open(self.FILE_PATH, 'w') as f:
                json.dump(deviceList, f, indent=4)

            return [deviceObj]
        else:
            return []

    def removeDevice(self,uuid):
        """Fornito un oggetto, risalendo al suo uuid, viene rimosso l'oggetto. Viene ritornata una lista vuota se non ho trovato l'oogetto da rimuovere.
        Se ho rimosso un oggetto allora ritorno una lista con l'elemento Device corrispondente"""
        try:
            deviceSearch = self.loadAllDevices()
            if len(deviceSearch) > 0:
                # SALVO IL VECCHIO CONTENUTO
                deviceList = []
                with open(self.FILE_PATH, "r") as jsonFileContent:
                    deviceList = json.load(jsonFileContent)
                # AGGIORNO IL VECCHIO CONTENUTO
                for idx, obj in enumerate(deviceList):
                    if obj['uuid'] == uuid:
                        deviceList.pop(idx)
                # RICARICO IL CONTENUTO NEL DATABASE
                with open(self.FILE_PATH, 'w') as f:
                    json.dump(deviceList, f, indent=4)
                return [uuid]
            else:
                return []
        except Exception as e:
            return []

    def updateDevice(self,deviceObj):
        """L'update si compone della funzione di add e di remove combinate assieme. Aggiorno l'elemento se presente, in caso contrario lo creo"""
        found = len(self.loadDevice(deviceObj.uuid))
        if not found:
            return self.addDevice(deviceObj)
        else:
            self.removeDevice(deviceObj.uuid)
            return self.addDevice(deviceObj)

"""TESTS"""
"""print("Test lettura tutti i device: "+str([dev for dev in DeviceDataManager().loadAllDevices()]))
print("Test di lettura del singolo device: "+str([dev for dev in DeviceDataManager().loadDevice('device9')]))
print("Test di creazione di un device già esistente: "+str(DeviceDataManager().addDevice(Device(
    uuid="device9"
))))
print("Test di creazione di un device che manca (dopo prima exe diventa esistente): "+str(DeviceDataManager().addDevice(Device(
    uuid="device1000",
    type="HUMIDITY_SENSOR",
    manufacturer="TOSHIBA",
    softwareVersion="1.11.19"
))))
print("Test di aggiornamento di un device: "+str(DeviceDataManager().updateDevice(Device(
    uuid="device1000",
    type="HUMIDITY_SENSOR",
    manufacturer="TOSHIBA",
    softwareVersion="1.11.20"
))))
print("Test di rimozione di un device: "+str(DeviceDataManager().removeDevice(Device(
    uuid="device1000",
    type="HUMIDITY_SENSOR",
    manufacturer="TOSHIBA",
    softwareVersion="1.11.20"
))))"""


