from flask import Flask, redirect, render_template
from datetime import timedelta,datetime



#CREO L'APP E SETTO UNA SECRET KEY
app = Flask(__name__)
app.config['SECRET_KEY'] = 'TestFlaskAPI'
app.permanent_session_lifetime = timedelta(minutes=60)


#SALVO LA PORTA BASE SU CUI RUNNARE IL SERVER E IL PATH DI BASE A CUI COLLEGARE LE MIE RISORSE
BASE_PATH = "/api/iot/inventory/"


#REGISTRO LE VIEW PER DIALOGARE CON LE MIE RISORSE
from FlaskView.DeviceView import DeviceView
#REGISTRO LA VIEW PER DIALOGARE CON LA RISORSA: DEVICE
DeviceView.register(app,route_prefix=BASE_PATH)



if __name__ == "__main__":
    SERVER_PORT = 8081
    app.run(port=SERVER_PORT)

