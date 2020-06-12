import RPi.GPIO as GPIO
import time
from datetime import datetime
import requests
import json
import urllib.request
import socket
import os
import sys

ahora = datetime.now()
current_time = ahora.strftime("%H:%M:%S, %d-%m-%y") #hora actual
channel = 21  #bomba conectada al pin 21
tiempo=30     #tiempo que esta activa la bomba de agua por defecto
#  Inicializa GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
try:
	print ('Parametro de riego:', str(sys.argv[1]))
	tiempo = int(sys.argv[1])
	def motor_on(pin):
		GPIO.output(pin, GPIO.HIGH)  # ENCIENDE BOMBA DE AGUA

	def motor_off(pin):
		GPIO.output(pin, GPIO.LOW)  # PARA BOMA DE AGUA
	if __name__ == '__main__':
		try:
			motor_on(channel)
			time.sleep(tiempo)
			motor_off(channel)
			time.sleep(1)
			GPIO.cleanup()
			print("Riego OK a las "+ current_time) 
		except KeyboardInterrupt:
			GPIO.cleanup()
except:
	print("Sin parametro! No se riega.")
