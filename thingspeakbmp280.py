import machine, network, time, urequests
from machine import Pin, I2C
from bmp280 import *

ssid = 'CAMBIA POR TU SSID' 
password = '**TU PASSWORD**'
url = "https://api.thingspeak.com/update?api_key=TU API"

red = network.WLAN(network.STA_IF)

red.active(True)
red.connect(ssid, password)

while red.isconnected() == False:
  pass

print('Conexión correcta')
print(red.ifconfig())

ultima_peticion = 0
intervalo_peticiones = 30

bus = I2C(0, sda=Pin(0), scl=Pin(1))
bmp = BMP280(bus)

def reconectar():
    print('Fallo de conexión. Reconectando...')
    time.sleep(10)
    machine.reset()

while True:
    try:
        if (time.time() - ultima_peticion) > intervalo_peticiones:
            temperatura = (bmp.temperature) 
            presion = (bmp.pressure)
            temp = round(temperatura, 1)
            pres = round(presion/100, 1)
            print(bmp.temperature)
            print(bmp.pressure)
            respuesta = urequests.get(url + "&field1=" + str(temp) + "&field2=" + str(pres))
            print ("Respuesta: " + str(respuesta.status_code))
            respuesta.close ()
            ultima_peticion = time.time()
    except OSError as e:
        reconectar()
