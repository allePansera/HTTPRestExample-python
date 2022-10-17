import requests, json

data_create = {"uuid":"device1001",
        "softwareVersion":"10.10.9",
        "type":"LIGHT_SENSOR",
        "manufacturer":"TOSHIBA"}

#CREAZIONE DI UN DEVICE
URL = "http://127.0.0.1:8081/api/iot/inventory/device"
data = requests.post(URL,json=json.dumps(data_create))
print(data.content)

#LETTURA DATI DI UN DEVICE
URL = "http://127.0.0.1:8081/api/iot/inventory/device/device1001"
data = requests.get(URL)
print(data.content)

#MODIFICA DI UN DEVICE
URL = "http://127.0.0.1:8081/api/iot/inventory/device/device1001"
data = requests.put(URL,json=json.dumps(data_create))
print(data.content)

#CANCELLAZIONE DI UN DEVICE
URL = "http://127.0.0.1:8081/api/iot/inventory/device/device1001"
data = requests.delete(URL)
print(data.content)


