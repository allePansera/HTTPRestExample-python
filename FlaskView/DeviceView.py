import sys, json, socket
from flask import render_template, request, make_response, url_for, Response
from flask_classful import FlaskView, route
from DataManager.DeviceDataManager import DeviceDataManager
from Service.device import Device



class DeviceView(FlaskView):

    default_methods = ['GET', 'POST', 'PUT', 'DELETE']
    @route('/', methods=default_methods)
    def index(self):
        """Risposta ad una chiamata all'uri: http://127.0.0.1:8081/*/device"""
        try:
            if request.method == "GET":
                #RESTUTITUIRE LA LISTA DI TUTTI I DEVICE
                deviceFullList = DeviceDataManager().loadAllDevices()
                if len(deviceFullList)==0:
                    return Response(status=404, headers=None, mimetype=None,
                                    content_type="application/json")
                else:
                    return Response(response=json.dumps(deviceFullList), status=200, headers=None, mimetype=None,
                                content_type="application/json")
            elif request.method == "POST":
                #CREAZIONE DI UN NUOVO DEVICE
                deviceCreated = DeviceDataManager().addDevice(Device(dictForm=json.loads(request.get_json(force=True))))
                if len(deviceCreated)==0:
                    return Response(status=409, mimetype=None,
                                    content_type="application/json")
                else:
                    headers = {"location": f'http://172.0.0.1:{8081}/api/device/{deviceCreated[0].uuid}'}
                    return Response(status=201, headers=headers, mimetype=None,
                                    content_type="application/json")
            else:
                msg = {"error": f'Metodo {request.method} non supportato'}
                return Response(response=json.dumps(msg), status=405, headers=None, mimetype=None,
                                content_type="application/json")
        except Exception as e:
            msg = {"error": str(e)}
            return Response(response=json.dumps(msg), status=500, headers=None, mimetype=None,
                            content_type="application/json")

    @route('/<device_id>', methods=default_methods)
    def device_id(self, device_id):
        """Risposta ad una chiamata all'uri: http://127.0.0.1:8081/*/device/<device_id>"""
        try:
            if request.method == "GET":
                #LETTURA DEI DATI DEL DEVICE RICERCATO PER ID
                deviceFound = DeviceDataManager().loadDevice(device_id)
                if len(deviceFound)==0:
                    return Response(status=404, headers=None,
                                    mimetype=None,
                                    content_type="application/json")
                else:
                    return Response(response=json.dumps(deviceFound[0]), status=200, headers=None, mimetype=None,
                                content_type="application/json")

            elif request.method == "PUT":
                #AGGIORNAMENOT DEI DATI DEL DEVICE PER UN ID FORNITO
                device = Device(dictForm=json.loads(request.get_json(force=True)))
                found = len(DeviceDataManager().loadDevice(device_id))
                if not found:
                    return Response(status=204, headers=None, mimetype=None,
                                    content_type="application/json")
                DeviceDataManager().updateDevice(device)
                return Response(status=200, headers=None, mimetype=None,
                                content_type="application/json")

            elif request.method == "DELETE":
                #CANCELLAZIONE DEL DEVICE FORNITO IL SUO ID
                # AGGIORNAMENOT DEI DATI DEL DEVICE PER UN ID FORNITO
                found = len(DeviceDataManager().loadDevice(device_id))
                if not found:
                    return Response(status=204, headers=None, mimetype=None,
                                    content_type="application/json")
                DeviceDataManager().removeDevice(device_id)
                return Response(status=200, headers=None, mimetype=None,
                                content_type="application/json")
            else:
                msg = {"error": f'Metodo {request.method} non supportato'}
                return Response(response=json.dumps(msg), status=405, headers=None, mimetype=None,
                                content_type="application/json")

        except Exception as e:
            msg = {"error": str(e)}
            return Response(response=json.dumps(msg), status=500, headers=None, mimetype=None,
                            content_type="application/json")