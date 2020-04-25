import os
import sys
import signal
import RPi.GPIO as GPIO
from time import sleep



pin = 18
maxTMP = 55.0



def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp = (res.replace("temp=","").replace("'C\n",""))
    print("temp is {0}".format(temp))
    return temp

def fanON():
    GPIO.output(pin, False)
    print("fanOn")
    return()
def fanOFF():
    GPIO.output(pin, True)
    print("fanOff")
    return()

def checkTemperature():
    CPU_temp = float(getCPUtemperature())
    print(str(CPU_temp) + " vs " + str(maxTMP))
    if CPU_temp > maxTMP:
        fanON()
    else:
        fanOFF()
    return()



try:
    setup() 
    while True:
        checkTemperature()
        sleep(60)
except KeyboardInterrupt:
    GPIO.cleanup()
