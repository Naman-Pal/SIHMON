import time
import board
import busio
import adafruit_adxl34x
import RPi.GPIO as GPIO
import threading
# setup adxl i2c functions
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
# Set up the LED and GPIO pins
led_pin = 21 # GPIO pin number used for the LED circuit
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
def adxl_senses():
while True:
print("%f %f %f"%accelerometer.acceleration)
time.sleep(1)
def blink_led():
while True:
GPIO.output(led_pin, GPIO.HIGH)
print("LED ON")
time.sleep(0.5)
GPIO.output(led_pin, GPIO.LOW)
print("LED OFF")
time.sleep(0.5)
try:
# Create and start the LED blinking thread
led_thread = threading.Thread(target=blink_led)
led_thread.start()
# Create and start the accelerometer thread
adxl_thread = threading.Thread(target=adxl_senses)
adxl_thread.start()
# Wait for both threads to finish (which will not happen in this case)
led_thread.join()
adxl_thread.join()
except KeyboardInterrupt:
# Clean up GPIO on keyboard interrupt
GPIO.cleanup()
