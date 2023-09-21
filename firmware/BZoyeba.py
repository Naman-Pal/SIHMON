import time 
import board 
import busio 
import adafruit_tmp006 
import RPi.GPIO as GPIO 
import threading 
# Define a function to convert Celsius to Fahrenheit. 
def c_to_f(c): 
return c * 9.0 / 5.0 + 32.0 
# Set up the LED and GPIO pins 
led_pin = 21 # Change this to the GPIO pin number you used for the LED circuit 
threshold_temp = 30.0 # Set the threshold temperature in Celsius 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(led_pin, GPIO.OUT) 
# Create library object using our Bus I2C port 
i2c = busio.I2C(board.SCL, board.SDA) 
sensor = adafruit_tmp006.TMP006(i2c, address=0x40) 
blinking = True 
# Function for LED blinking 
def blink_led(): 
while blinking: 
GPIO.output(led_pin, GPIO.HIGH) 
time.sleep(0.2) 
GPIO.output(led_pin, GPIO.LOW) 
time.sleep(0.2) 
# Start the LED blinking function in a separate thread 
blink_thread = threading.Thread(target=blink_led) 
blink_thread.start() 
try: 11 

while True: 
obj_temp = sensor.temperature 
print("Object temperature: {:.3F}*C / {:.3F}*F".format(obj_temp, c_to_f(obj_temp))) 
if obj_temp > threshold_temp: 
blinking = False 
GPIO.output(led_pin, GPIO.HIGH) # Turn on the LED (solid light) 
else: 
blinking = True 
time.sleep(0.2) 
except KeyboardInterrupt: 
blinking = False 
GPIO.cleanup()
