import RPi.GPIO as GPIO
import time

servoPIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

initialPos = 12.5
finalPos = 2.5
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(initialPos) # Initialization
#def open():
p.ChangeDutyCycle(finalPos)
time.sleep(0.5)
p.ChangeDutyCycle(0)
time.sleep(5)
#def close():
p.ChangeDutyCycle(initialPos)
time.sleep(0.5)
p.ChangeDutyCycle(0)

#def close():
p.stop()
GPIO.cleanup()
	
"""try:
  #while True:
  p.ChangeDutyCycle(initialPos)
  time.sleep(0.5)
  p.ChangeDutyCycle(0)
  time.sleep(5)
  p.ChangeDutyCycle(finalPos)
  time.sleep(0.5)
  GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
"""
