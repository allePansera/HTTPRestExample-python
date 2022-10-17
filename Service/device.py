import json


class Device:
    """
    Data structure:
    1 {
    2 " uuid ": " device00002 ",
    3 " type ": " iot : demosensor ",
    4 " softwareVersion ": " v0 .0.0.1" ,
    5 " manufacturer ": " Acme - Inc "
    6 }
    """
    def __init__(self, uuid = None, type=None, softwareVersion=None, manufacturer=None, dictForm = None):
        self.uuid = uuid
        self.type = type
        self.softwareVersion = softwareVersion
        self.manufacturer = manufacturer
        if dictForm is not None:
            self.fromJson(dictForm)
        if self.uuid is None or "":
            raise TypeError("L'uuid del dispositivo deve essere diverso da None & '' ")

    def toJson(self):
        return self.__dict__

    def fromJson(self,dictionary):
        self.uuid = dictionary.get("uuid","")
        self.type = dictionary.get("type","")
        self.softwareVersion = dictionary.get("softwareVersion","")
        self.manufacturer = dictionary.get("manufacturer","")

    def __str__(self):
        return self.__dict__
