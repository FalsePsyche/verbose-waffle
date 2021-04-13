import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
Mister = 17
GPIO.setup(Mister, GPIO.OUT) # GPIO Assign mode
GPIO.output(Mister, GPIO.LOW) # out
# GPIO.output(Mister, GPIO.HIGH) # on


def mister_on():
	GPIO.output(Mister, GPIO.HIGH)
	time.sleep(10)
	GPIO.output(Mister, GPIO.LOW)
	time.sleep(600)

def get_time():
	return datetime.now().time()

while get_time().hour > 7 and get_time().hour < 9:
	mister_on()

while get_time().hour > 10 and get_time().hour < 12:
	mister_on()

while get_time().hour > 14 and get_time().hour < 16:
	mister_on()
